import os, os.path, sys, datetime,stat
#other libraries import
import json
#for pdf
from jinja2 import Environment
from jinja2 import FileSystemLoader
import pdfkit

#Pyside6 import
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QDialogButtonBox, QLabel,QVBoxLayout
from PySide6.QtCore import Qt


def check_cif(cif):

    not_allowed = '/[\'^£$%&*()}{@#~?><>,|=_+¬-]/'
    dni_nie_word = "TRWAGMYFPDXBNJZSQVHLCKE"
    word_res = "JABCDEFGHI"
    other_cif = ["P","Q","R","S","W"]


    cif = cif.upper()
    first = cif[0]
    
    if(len(cif) > 9):
        return (False, "La longitud del CIF es incorrecta, sobran datos")
    elif(len(cif) < 9):
        return (False, "La longitud del CIF es incorrecta, faltan datos")
    else:
        if any(c in not_allowed for c in cif):
            #ERROR. Not allowed characters
            return (False, "No se permiten los siguientes caracteres en el CIF: "+not_allowed)
        else:
            if(type(first) == int):
                #DNI
                num = int(cif[:8])
                letter = cif[-1]

                if(dni_nie_word[num % 23] == letter):
                    return (True, "")
                else:
                    return (False, "El numero del DNI esta mal, por favor revisa y vuelve a introducirlo correctamente")

            elif(first == "X" or first == "Y"):
                #NIE
                num = int(cif[1:8])
                letter = cif[-1]

                if(dni_nie_word[num % 23] == letter):
                    return (True, "")
                else:
                    return (False, "El numero del NIE esta mal, por favor revisa y vuelve a introducirlo correctamente")
            else:
                #CIF
                num = int(cif[1:8])
                last = cif[-1]

                total = int(num[1]) + int(num[3]) + int(num[5])

                odd_val = [
                    str(int(num[0])*2),
                    str(int(num[2])*2),
                    str(int(num[4])*2),
                    str(int(num[6])*2)
                ]

                for val in odd_val:
                    if(len(val) > 1):
                        total = total + int(val[0]) + int(val[1])
                    else:
                        total = total + int(val[0])
                
                total = 10 - total[1]

                if(first in other_cif):
                    if(word_res[total] == last): return (True, "")
                    else: return (False, "La letra de control del CIF (la ultima) esta mal, por favor revisa y vuelve a introducirlo correctamente")
                else:
                    if(total == last): return (True, "")
                    else: return (False, "El numero de control del CIF (el ultimo) esta mal, por favor revisa y vuelve a introducirlo correctamente")

def print_log(msg):
    try:
        actual_date = datetime.datetime.now().strftime("%d_%m_%Y")
        file_path = "./logs/log_"+actual_date+".log"
        date_and_hour = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        if (os.path.isfile(file_path)):log = open(file_path, "a")
        else: log = open(file_path, "w")
        
        log.write(f"[{date_and_hour}]"+str(msg)+"\n")
        print(f"[{date_and_hour}]"+str(msg))
        log.close()
    except Exception as e:
        print(f"[{date_and_hour}]: Error! No se ha podido añadir el mensaje: "+str(msg)+" error --> "+str(e))

def message_box(case, msg):
    try:

        case = case.upper()

        box = QMessageBox()
        if(case == "CRITICAL"):
            box.setWindowTitle("Cuidado!")
            box.setText(msg)
            box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            box.setIcon(QMessageBox.Critical)

        if(case == "WARNING"):
            box.setWindowTitle("Cuidado!")
            box.setText(msg)
            box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            box.setIcon(QMessageBox.Warning)

        return box.exec()
    except Exception as e:
        print_log("ERRO! No se ha podido enseñar la ventana de mensaje. Error --> "+str(e))

def delete_attached_files(doc_type,_id):
    try:
        json_path = os.path.abspath('res/data/json/'+str(doc_type)+'/'+str(doc_type)+'_'+str(_id)+'.json')
        pdf_path = os.path.abspath('res/data/pdf/'+str(doc_type)+'/'+str(doc_type)+'_'+str(_id)+'.pdf')
        os.remove(json_path)
        os.remove(pdf_path)
    except Exception as e:
        print_log(f"ERROR! No se ha podido borrar el archivo. Error --> "+str(e))

def create_path(ext,d_number,d_type):
    try:
        dir_path = "res/data/"+ext+"/"+d_type+"/"

        match ext:
            case "json":
                file_path = dir_path+d_type+"_"+str(d_number)+".json"
            case "pdf":
                file_path = dir_path+d_type+"_"+str(d_number)+".pdf"

        #check
        if(not os.path.isdir(dir_path)): 
            os.makedirs(dir_path)
            os.chmod(dir_path, stat.S_IRWXO)

        return file_path

    except Exception as e:
        print_log(f"ERROR! No se ha podido generar el path para el documneto de tipo {d_type}. Error --> "+str(e))

def create_json(d_type, user_data, address,data_vals, d_number):
    try:
        
        file_path = create_path("json",d_number,d_type)

        if(os.path.isfile(file_path)): message_box("critical","Este presupuesto ya existe!")
        #example
        #info = {
        #    "doc_number":d_number,
        #    "client_name":str(user_data[2]),
        #    "nif":str(user_data[1]),
        #    "address":str(address),
        #    'desc':[
        #        ['Titulo','Esto es una descripcion de prueba',100,7,700],
        #        ['Texto normal','Esto es una descripcion de prueba 2',200,3,600]
        #    ], 
        #    'subtotal':'123445',
        #    'iva':21,
        #    'invoice_total':'123000,23456'
        #}

        json_data = {'doc_number':d_number,
            'actual_date':datetime.datetime.now().strftime("%d/%m/%Y"),
            'client_name':str(user_data[2]),
            'nif':str(user_data[1]),
            'address':str(address),
            'desc':[]}


        """aux = {
            "type":QComboBox(),
            "desc":QLineEdit(),
            "price":QLineEdit()
        }"""

        #initialize arrays

        index = 0
        for i in data_vals:
            pos = 0
            json_data['desc'].append([])
            for key, data in i.items():
                if(pos == 0): json_data['desc'][index].append(str(data.currentText()))
                if(pos == 1): json_data['desc'][index].append(str(data.text()))
                if(pos == 2): json_data['desc'][index].append(str(data.text()))
                pos += 1
            index +=1

        json_obj = json.dumps(json_data)
        with open(file_path,'w')as f:
            f.write(json_obj)

        return file_path
    except Exception as e:
        print_log("ERROR! No se ha podido generar un json para el presupuesto. Error --> "+str(e))
        message_box("critical","ERROR: "+str(e))



def create_json_old(d_type, user_data, data_vals, d_number):
    try:
        
        file_path = create_path("json",d_number,d_type)

        if(os.path.isfile(file_path)): message_box("critical","Este presupuesto ya existe!")

        info = {
            "doc_number":d_number,
            "client_name":str(user_data[2]),
            "nif":str(user_data[1]),
            "address":str(user_data[4]),
            'desc':[
                ['Titulo','Esto es una descripcion de prueba',100,7,700],
                ['Texto normal','Esto es una descripcion de prueba 2',200,3,600]
            ], 
            'subtotal':'123445',
            'iva':21,
            'invoice_total':'123000,23456'
        }

        json_data = {'doc_number':d_number,
            'actual_date':datetime.datetime.now().strftime("%d/%m/%Y"),
            'client_name':str(user_data[2]),
            'nif':str(user_data[1]),
            'address':str(user_data[4])}


        """aux = {
            "type":QComboBox(),
            "desc":QLineEdit(),
            "price":QLineEdit()
        }"""

        item = 0
        for i in data_vals:
            for key, data in i.items():
                if(key == "type") and (data.currentText() == "Titulo") and (not 'desc' in json_data):

                    #create desc in json 
                    json_data.setdefault("desc",[])
                    json_data["desc"].append([])

                    json_data["desc"][item] = {"title":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Titulo") and ('desc' in json_data):

                    #desc in json
                    json_data["desc"].append([])
                    item +=1
                    json_data["desc"][item] = {"title":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Subtitulo") and (not 'desc' in json_data):

                    json_data.setdefault("desc",[])
                    json_data["desc"].append([])
                    json_data["desc"][item] = {"subtitle":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Subtitulo") and ('desc' in json_data):

                    json_data["desc"][item] = {"subtitle":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Texto normal") and (not 'desc' in json_data):

                    json_data.setdefault("desc",[])
                    json_data["desc"].append([])
                    json_data["desc"][item] = {"text":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Texto normal") and ('desc' in json_data):

                    json_data["desc"][item] = {"text":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Nota") and (not 'desc' in json_data):

                    json_data.setdefault("desc",[])
                    json_data["desc"].append([])
                    json_data["desc"][item] = {"note":i['desc'].text()}

                elif(key == "type") and (data.currentText() == "Nota") and ('desc' in json_data):

                    json_data["desc"][item] = {"note":i['desc'].text()}

        json_obj = json.dumps(json_data)
        with open(file_path,'w')as f:
            f.write(json_obj)

        return file_path
    except Exception as e:
        print_log("ERROR! No se ha podido generar un json para el presupuesto. Error --> "+str(e))
        message_box("critical","ERROR: "+str(e))

def gen_table(description):
    html = "<tr>"
    for desc in description:
        if(desc[0] == "Titulo"):html = html + "<tr><b>"+str(desc[1])+"</b></tr>"
        if(desc[0] == "Subtitulo"):html = html + "<tr><b>"+str(desc[1])+"</b></tr>"
        if(desc[0] == "Texto normal"):html = html + "<tr>"+str(desc[1])+"</tr>"
        if(desc[0] == "Nota"):html = html + "<tr>"+str(desc[1])+"</tr>"

    html = html + "</tr>"
    return html

def create_pdf(doc_type,json_path):

    template_vars = json.load(open(json_path))
    if(doc_type == "presupuesto"): template_path = 'budget_A4.html'
    if(doc_type == "factura"): template_path = 'invoice_A4.html'

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    if(type(template_vars['desc']) == list): template_vars['desc'] = gen_table(template_vars['desc'])
    html_out = template.render(template_vars)
    #path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    #config = configuration(wkhtmltopdf=path_wkhtmltopdf)
    options = {
        "enable-local-file-access": "",
        "encoding":"UTF-8"
    }

    file_content = pdfkit.from_string(
        html_out,
        'out.pdf',
        css='styles/invoice.css',
        options=options
    )