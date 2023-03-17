from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from .ui_newbudget import Ui_NewBudgetWindow
#from Data.books import insert_book, select_book_by_id
import shutil
import os
import datetime

from views.support_functions import *

from Database.db_functions import insert_budget, select_all_users, select_user_by_name

class NewBudgetWindow(QWidget, Ui_NewBudgetWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.populate_comobox()
        self.populate_dateedit()

        self.btn_savebudget.clicked.connect(self.addBudget)
        self.btn_cancel.clicked.connect(self.close)

        self.btn_newuser.clicked.connect(self.open_new_user_window)
        self.btn_clientaddress.clicked.connect(self.set_client_addres)


    def set_client_addres(self):
        try:
            user = self.user_comobox.currentText()
            #get client address
            address = select_user_by_name(user)[4]
            self.line_address.setText(str(address))
            print_log(f"La direccion del usuario {user} para presupuesto es {address}, todo ok")
        except Exception as e:
            print_log("ERROR! No se ha podido seleccionar la dirección del usuario. Error --> "+str(e))

    def populate_dateedit(self):
        try:
            date = QDate.currentDate()
            self.budget_date.setDate(date)
            print_log(f"Put date time to the QDateEdit {date}")
        except Exception as e:
            print_log("ERROR! No se ha podido actualizar la fecha en el QDateEdit de los presupuestos. Error --> "+str(e))

    def populate_comobox(self):

        for usr in select_all_users():
            self.user_comobox.addItem(usr[2])
        
    def check_inputs(self):
        title = self.line_title.text()
        date = self.budget_date.text()
        user = self.user_comobox.currentText()
        address = self.line_address.text()

        errors_count = 0
        
        if title == "":
            print_log("El campo titulo es obligatorio")
            errors_count += 1
        if date == "" : 
            print_log("El campo fecha es obligatorio")
            errors_count +=1
        
        return (errors_count == 0)
    
    def addBudget(self):

        try:
            title = self.line_title.text()
            date = self.budget_date.text()
            user = self.user_comobox.currentText()

            address = self.line_address.text()


            if(self.check_inputs()):
                
                user_id = select_user_by_name(user)[0]

                print_log("El usuario para el presupuesto es: "+user+" y su id es :"+str(user_id))

                data = (title,date,address,user_id)

                if (insert_budget(data)):
                    self.clean_inputs()
                    self.parent.refresh_budget_table_from_child_window()
                    self.close()
            else:
                msg = QMessageBox.critical(
                        self,
                        "Cuidado!",
                        "Revisa los datos que has introducido, ni el titulo ni la fecha pueden estar vacios!",
                        buttons = QMessageBox.Ok,
                        defaultButton=QMessageBox.Ok
                    )
        except Exception as e:
            print_log("ERROR! No se ha podido añadir el nuevo presupuesto. Error --> "+str(e))

    def open_new_user_window(self):
        self.parent.open_new_user_window()

    def open_new_date_window(self):
        self.parent.open_new_date_window()

    def clean_inputs(self):
        self.line_title.clear()
        self.budget_date.clear()
        self.user_comobox.clear()
        self.line_address.clear()