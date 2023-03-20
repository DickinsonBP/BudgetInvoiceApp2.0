import os, sys, datetime
#Database import
import sqlite3
from sqlite3 import Error
#Pyside6 import
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QDialogButtonBox, QLabel,QVBoxLayout
from PySide6.QtCore import Qt
import json


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
            box.setStandardButtons(QMessageBox.Ok)
            box.setIcon(QMessageBox.Critical)
            button = box.exec()

    except Exception as e:
        print_log("ERRO! No se ha podido enseñar la ventana de mensaje. Error --> "+str(e))


def create_json(d_type, user_data, data_vals, d_number):
    try:
        path = "res/data/"+d_type+"s/"
        file_path = path +d_type+"_"+str(d_number)+".json"

        #check
        if(not os.path.isdir(path)): os.makedirs(path)
        if(os.path.isfile(file_path)): message_box("critical","Este presupuesto ya existe!")


        json_data = {
            "header":
            [
                {
                    d_type+"_number":d_number,
                    "client": [
                        {
                            "name":str(user_data[2]),
                            "nif":str(user_data[1]),
                            "address":str(user_data[4])
                        }
                    ]
                }
            ]
        }

        
        """aux = {
            "type":QComboBox(),
            "desc":QLineEdit(),
            "price":QLineEdit()
        }"""

        item = 0
        for i in data_vals:
            for key, data in i.items():
                if(key == "type") and (data.currentText() == "Titulo") and (not 'body' in json_data):
                    
                    #create body in json 
                    json_data.setdefault("body",[])
                    json_data["body"].append({})

                    json_data["body"][item].setdefault("title",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Titulo") and ('body' in json_data):
                    
                    #body in json
                    json_data["body"].append({})
                    item +=1
                    json_data["body"][item].setdefault("title",i['desc'].text())
                    
                elif(key == "type") and (data.currentText() == "Subtitulo") and (not 'body' in json_data):
                    
                    json_data.setdefault("body",[])
                    json_data["body"].append({})
                    json_data["body"][item].setdefault("subtitle",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Subtitulo") and ('body' in json_data):
                    
                    json_data["body"][item].setdefault("subtitle",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Texto normal") and (not 'body' in json_data):
                    
                    json_data.setdefault("body",[])
                    json_data["body"].append({})
                    json_data["body"][item].setdefault("text",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Texto normal") and ('body' in json_data):
                    
                    json_data["body"][item].setdefault("text",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Nota") and (not 'body' in json_data):
                    
                    json_data.setdefault("body",[])
                    json_data["body"].append({})
                    json_data["body"][item].setdefault("note",i['desc'].text())

                elif(key == "type") and (data.currentText() == "Nota") and ('body' in json_data):
                    
                    json_data["body"][item].setdefault("note",i['desc'].text())

        json_obj = json.dumps(json_data)
        with open(file_path,'w')as f:
            f.write(json_obj)

        return file_path
    except Exception as e:
        print_log("ERROR! No se ha podido generar un json para el presupuesto. Error --> "+str(e))
        message_box("critical","ERROR: "+str(e))