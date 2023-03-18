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
        self.num_rows = 1

        self.widgets = {}
        self.description_vars = {}
        self.type_vars = {}
        self.price_vars = {}

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
        #self.btn_save.clicked.connect(self.addBudget)

    def set_next_window_budget_number(self):
        self.budget_number.setText(self.b_number)

    def add_row(self):
        self.num_rows += 1
        #create a new widget and a layout
        new_widget = QWidget(self.description_widget)
        new_horizontalLayout = QHBoxLayout(new_widget)

        new_type_combobox = QComboBox()
        new_type_combobox.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Tipo", None))
        self.type_vars.setdefault("type_"+str(self.num_rows),new_type_combobox)
        new_horizontalLayout.addWidget(new_type_combobox)

        new_desc_line = QLineEdit(self.description_widget)
        new_desc_line.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Descripci\u00f3n", None))
        self.description_vars.setdefault("desc_"+str(self.num_rows),new_desc_line)
        new_horizontalLayout.addWidget(new_desc_line)

        new_price_line = QLineEdit(self.description_widget)
        new_price_line.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Precio", None))
        self.price_vars.setdefault("price_"+str(self.num_rows),new_price_line)
        new_horizontalLayout.addWidget(new_price_line,0,Qt.AlignRight)

        self.verticalLayout_6.addWidget(new_widget)

        self.populate_type_combobox()

    def populate_type_combobox(self):
        types = ["Titulo","Subtitulo","Texto normal","Nota"]

        #start with the initial comobox
        for item in types:
            self.combobox_type_1.addItem(item)

        #continue with all the comobox at the dictionary
        for name, comobox in self.type_vars.items():
            for item in types:
                comobox.addItem(item)

    def set_client_addres(self):
        try:
            user = self.user_comobox.currentText()
            #get client address
            address = select_user_by_name(user)[4]
            self.line_address.setText(str(address))
        except Exception as e:
            print_log("ERROR! No se ha podido seleccionar la dirección del usuario en presupuesto. Error --> "+str(e))

    def populate_invoiceNum(self):
        try:
           
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
                
                user_id = select_user_by_name(user)[0]

                path = self.create_budget_json()
                data = (self.budget_number,title,date,address,user_id,path)
                if(insert_data(data, "Budget")):
                    self.clean_inputs()
                    self.parent.refresh_budget_table_from_child_window()
                    self.close()
                else:
                    message_box("CRITICAL","Algo ha fallado al guardar el presupuesto, revisa los datos y vuelve a intentar")
            else:
                message_box("CRITICAL", "Revisa los datos que has introducido, ni el titulo ni la fecha pueden estar vacios!")
        except Exception as e:
            print_log("ERROR! No se ha podido añadir el nuevo presupuesto. Error --> "+str(e))

    def open_new_user_window(self):
        self.parent.open_new_user_window()
        self.populate_comobox()

    def clean_inputs(self):
        self.line_title.clear()
        self.user_combobox.clear()
        self.line_address.clear()

    def create_budget_json(self):
        path = 'res/data/budgets/'
        file_path = path +"presupuesto_"+str(self.b_number)+".json"

        #check
        if(not os.path.exists(path)): os.mkdir(path)
        if(os.path.exists(file_path)): message_box("critical","Este presupuesto ya existe!")
            