from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from .ui_newuser import Ui_NewUserWindow
#from Data.books import insert_book, select_book_by_id
import shutil
import os


from views.functions import AppFunctions

class NewUserWindow(QWidget, Ui_NewUserWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.btn_saveuser.clicked.connect(self.addUser)
        self.btn_cancel.clicked.connect(self.close)

    def check_inputs(self):
        nif = self.line_nif.text()
        name = self.line_name.text()
        email = self.line_email.text()
        phone = self.line_phone.text()
        address = self.line_address.text()

        errors_count = 0
        
        if name == "":
            print("El campo nombre es obligatorio")
            errors_count += 1
        if phone == "":
            print("El campo telefono es obligatorio")
            errors_count +=1
        
        return (errors_count == 0)
    
    def addUser(self):

        nif = self.line_nif.text()
        name = self.line_name.text()
        email = self.line_email.text()
        phone = self.line_phone.text()
        address = self.line_address.text()


        if(self.check_inputs()):
            
            
            if AppFunctions.insert_user_data("Database/DBP_DB.db",(nif,name,email,phone,address)):
                self.clean_inputs()


    
    def clean_inputs(self):
        self.line_nif.clear()
        self.line_name.clear()
        self.line_email.clear()
        self.line_phone.clear()
        self.line_address.clear()