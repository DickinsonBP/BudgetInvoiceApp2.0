from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from .ui_newinvoice import Ui_NewInvoiceWindow
#from Data.books import insert_book, select_book_by_id
import shutil
import os
import datetime

from views.support_functions import *

from Database.db_functions import insert_data, select_all_users, select_user_by_name, get_next_invoice_id

invoices_path = r"C:\Users\dicki\Desktop\Salida\Facturas"

class NewInvoiceWindow(QWidget, Ui_NewInvoiceWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.populate_comobox()
        self.populate_dateedit()
        self.populate_invoiceNum()

        self.btn_saveinvoice.clicked.connect(self.addInvoice)
        self.btn_cancel.clicked.connect(self.close)

        self.btn_newuser.clicked.connect(self.open_new_user_window)
        self.btn_clientaddress.clicked.connect(self.set_client_addres)

    def set_client_addres(self):
        try:
            user = self.user_comobox.currentText()
            #get client address
            address = select_user_by_name(user)[4]
            self.line_address.setText(str(address))
        except Exception as e:
            print_log("ERROR! No se ha podido seleccionar la dirección del usuario en factura. Error --> "+str(e))

    def populate_invoiceNum(self):
        try:
            year = datetime.datetime.now().strftime("%Y")
            next_id = get_next_invoice_id()


            if(len(str(next_id)) > 1): invoice_number = year[2:]+"0"+str(next_id)
            else: invoice_number = year[2:]+"00"+str(next_id)

            self.line_invoicenumber.setText(invoice_number)

        except Exception as e:
            print_log("ERROR! No se ha podido actualizar el ID de la nueva factura. Error --> "+str(e))

    def populate_dateedit(self):
        try:
            date = QDate.currentDate()
            self.budget_date.setDate(date)
        except Exception as e:
            print_log("ERROR! No se ha podido actualizar la fecha en el QDateEdit de los presupuestos. Error --> "+str(e))

    def populate_comobox(self):

        for usr in select_all_users():
            self.user_comobox.addItem(usr[2])
        
    def check_inputs(self):
        invoice_number = self.line_invoicenumber.text()
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
        if invoice_number == "" : 
            print_log("El campo numero es obligatorio")
            errors_count +=1
        
        return (errors_count == 0)
    
    def addInvoice(self):

        try:
            invoice_number = self.line_invoicenumber.text()
            title = self.line_title.text()
            date = self.budget_date.text()
            user = self.user_comobox.currentText()

            address = self.line_address.text()


            if(self.check_inputs()):
                
                user_data = select_user_by_name(user)

                json_path = create_json("factura",user_data,address,[],invoice_number, title, 21, 1234.32)
                create_pdf("factura",json_path,invoices_path)
                if(json_path):
                    data = (invoice_number,title,date,user_data[0],invoices_path,address)

                    if (insert_data(data,"Invoice")):
                        self.clean_inputs()
                        self.parent.refresh_invoice_table_from_child_window()
                        self.close()
                    else:
                        message_box("CRITICAL","Algo ha fallado al guardar la factura, revisa los datos y vuelve a intentar")
            else:
                message_box("warning", "Revisa los datos que has introducido, ni el titulo ni la fecha pueden estar vacios!")

        except Exception as e:
            print_log("ERROR! No se ha podido añadir el nuevo presupuesto. Error --> "+str(e))


    def open_new_user_window(self):
        self.parent.open_new_user_window()
        self.populate_comobox()

    def clean_inputs(self):
        self.line_title.clear()
        self.user_comobox.clear()
        self.line_address.clear()

    def download_invoice(self):
        pass