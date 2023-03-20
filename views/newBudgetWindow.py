from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from .ui_newbudget import Ui_NewBudgetWindow
#from Data.books import insert_book, select_book_by_id
import os
import datetime
import json

from views.support_functions import *
from Custom_Widgets.Widgets import *

from Database.db_functions import insert_data, select_all_users, select_user_by_name, get_next_budget_id
from .BudgetData import BudgetData

class NewBudgetWindow(QWidget, Ui_NewBudgetWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        #variables
        self.b_number = ""
        self.num_rows = 0
        self.num_types = 0

        self.data_vals = []

        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.populate_comobox()
        self.populate_dateedit()
        self.populate_invoiceNum()
        self.populate_type_combobox()
        
        loadJsonStyle(self.parent,self,jsonFiles = {"json/budgetstyle.json"})

        self.btn_cancel.clicked.connect(self.close)
        self.btn_continue.clicked.connect(self.check_inputs)
        self.btn_newuser.clicked.connect(self.open_new_user_window)
        self.btn_clientaddress.clicked.connect(self.set_client_addres)
        self.btn_newrow.clicked.connect(self.add_row)
        self.btn_save.clicked.connect(self.addBudget)

    def set_next_window_budget_number(self):
        self.budget_number.setText(self.b_number)

    def add_row(self):
        self.num_rows += 1
        #create a new widget and a layout
        new_widget = QWidget(self.description_widget)
        new_horizontalLayout = QHBoxLayout(new_widget)

        new_type_combobox = QComboBox()
        new_type_combobox.setObjectName("combobox_type_"+str(self.num_rows))
        new_type_combobox.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Tipo", None))
        new_horizontalLayout.addWidget(new_type_combobox)
        


        new_desc_line = QLineEdit(self.description_widget)
        new_desc_line.setObjectName("line_desc_"+str(self.num_rows))
        new_desc_line.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Descripci\u00f3n", None))
        new_horizontalLayout.addWidget(new_desc_line)


        new_price_line = QLineEdit(self.description_widget)
        new_price_line.setObjectName("line_price_"+str(self.num_rows))
        new_price_line.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Precio", None))
        new_horizontalLayout.addWidget(new_price_line,0,Qt.AlignRight)

        aux = {
                "type":new_type_combobox,
                "desc":new_desc_line,
                "price":new_price_line
            }

        self.data_vals.append(aux)

        self.verticalLayout_6.addWidget(new_widget)

        self.populate_type_combobox()

    def populate_type_combobox(self):
        types = ["Titulo","Subtitulo","Texto normal","Nota"]

        #continue with all the comobox at the dictionary
        for i in self.data_vals[self.num_rows:]:
            for key,comobox in i.items():
                if(key == 'type'):
                    for item in types:
                        comobox.addItem(item)

        self.num_types += 1

    def set_client_addres(self):
        try:
            user = self.user_combobox.currentText()
            #get client address
            address = select_user_by_name(user)[4]
            self.line_address.setText(str(address))
        except Exception as e:
            print_log("ERROR! No se ha podido seleccionar la dirección del usuario en presupuesto. Error --> "+str(e))

    def populate_invoiceNum(self):
        try:
           
            aux = {
                "type":self.combobox_type_1,
                "desc":self.line_desc_1,
                "price":self.line_price_1
            }
            self.data_vals.append(aux)

            year = datetime.datetime.now().strftime("%Y")
            next_id = get_next_budget_id()

            if(len(str(next_id)) > 1): self.b_number = year[2:]+"0"+str(next_id)
            else: self.b_number = year[2:]+"00"+str(next_id)

            self.line_budgetNumber.setText(self.b_number)
            self.set_next_window_budget_number()
        except Exception as e:
            print_log("ERROR! No se ha podido actualizar el ID del nuevo presupuesto. Error --> "+str(e))

    def populate_dateedit(self):
        try:
            date = QDate.currentDate()
            self.budget_date.setDate(date)
        except Exception as e:
            print_log("ERROR! No se ha podido actualizar la fecha en el QDateEdit de los presupuestos. Error --> "+str(e))

    def populate_comobox(self):
        for usr in select_all_users():
            self.user_combobox.addItem(usr[2])
        
    def check_inputs(self):
        self.b_number = self.line_budgetNumber.text()
        title = self.line_title.text()
        date = self.budget_date.text()
        user = self.user_combobox.currentText()
        address = self.line_address.text()

        errors_count = 0
        
        if title == "":
            print_log("El campo titulo es obligatorio")
            errors_count += 1
        if date == "" : 
            print_log("El campo fecha es obligatorio")
            errors_count +=1
        if self.budget_number == "" : 
            print_log("El campo numero es obligatorio")
            errors_count +=1
        
        return (errors_count == 0)
    
    def addBudget(self):

        try:
            self.b_number = self.line_budgetNumber.text()
            title = self.line_title.text()
            date = self.budget_date.text()
            user = self.user_combobox.currentText()

            address = self.line_address.text()


            if(self.check_inputs()):
                
                user_id = select_user_by_name(user)

                path = self.create_budget_json(user_id)
                if(path):
                    data = (self.budget_number,title,date,address,user_id[0],path)
                    print(data)
                    #if(insert_data(data, "Budget")):
                    #    self.clean_inputs()
                    #    self.parent.refresh_budget_table_from_child_window()
                    #    self.close()
                    #else:
                    #    message_box("CRITICAL","Algo ha fallado al guardar el presupuesto, revisa los datos y vuelve a intentar")
                    #    print_log("ERROR! No se ha podido guardar el nuevo presupuesto")
                else:
                    message_box("CRITICAL","Algo ha fallado al generar el archivo del presupuesto, revisa los datos y vuelve a intentar")
                    print_log("ERROR! No se ha podido generar el archivo del nuevo presupuesto")
            else:
                message_box("CRITICAL", "Revisa los datos que has introducido, ni el titulo ni la fecha pueden estar vacios!")
                print_log("ERROR! Hay datos obligatorios vacios en el presupuesto.")
        except Exception as e:
            print_log("ERROR! No se ha podido añadir el nuevo presupuesto. Error --> "+str(e))

    def open_new_user_window(self):
        self.parent.open_new_user_window()
        self.populate_comobox()

    def clean_inputs(self):
        self.line_title.clear()
        self.user_combobox.clear()
        self.line_address.clear()

    def create_budget_json(self,user_data):
        
        try:
            path = 'res/data/budgets/'
            file_path = path +"presupuesto_"+str(self.b_number)+".json"

            #check
            if(not os.path.isdir(path)): os.makedirs(path)
            if(os.path.isfile(file_path)): message_box("critical","Este presupuesto ya existe!")


            json_data = {
                "header":
                [
                    {
                        "budget_number":self.b_number,
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
            for i in self.data_vals:
                for key, data in i.items():
                    if(key == "type") and (data.currentText() == "Titulo") and (not 'body' in json_data):
                        
                        #create body in json 
                        json_data.setdefault("body",[])
                        json_data["body"].append({})

                        if(item): item +=1
                        json_data["body"][item].setdefault("title",i['desc'].text())

                    elif(key == "type") and (data.currentText() == "Titulo") and ('body' in json_data):
                        
                        #body in json
                        json_data["body"].append({})
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