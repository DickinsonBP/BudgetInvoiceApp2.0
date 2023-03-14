from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from .ui_edituser import Ui_EditUserWindow
#from Data.books import insert_book, select_book_by_id
import shutil
import os


from Database.db_functions import select_user_by_id, update_user

class EditUserWindow(QWidget, Ui_EditUserWindow):

    def __init__(self, parent=None, _id = None):

        self._id = _id
        super().__init__(parent)

        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.populate_inputs()

        self.btn_saveuser.clicked.connect(self.update_user)
        self.btn_cancel.clicked.connect(self.close)


    def populate_inputs(self):
        data = select_user_by_id(self._id)

        self.line_nif.setText(data[1])
        self.line_name.setText(data[2])
        self.line_email.setText(data[3])
        self.line_address.setText(data[4])
        self.line_phone.setText(data[5])

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
    
    def update_user(self):

        nif = self.line_nif.text()
        name = self.line_name.text()
        email = self.line_email.text()
        phone = self.line_phone.text()
        address = self.line_address.text()


        if(self.check_inputs()):
            
            data = (nif,name,email,address,phone)

            if (update_user(self._id,data)):
                self.clean_inputs()
                self.parent.refresh_user_table_from_child_window()
                self.close()
        else:
            msg = QMessageBox.critical(
                    self,
                    "Cuidado!",
                    "Revisa los datos que has introducido, ni el nombre ni el telefono pueden estar vacios!",
                    buttons = QMessageBox.Ok,
                    defaultButton=QMessageBox.Ok
                )
    
    def clean_inputs(self):
        self.line_nif.clear()
        self.line_name.clear()
        self.line_email.clear()
        self.line_phone.clear()
        self.line_address.clear()