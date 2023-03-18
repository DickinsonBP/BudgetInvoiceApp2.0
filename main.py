################################################################################
##
## BY: DICKINSON BEDOYA PEREZ
## PROJECT MADE WITH: Qt Designer and PySide6
## V: 1.0.0
##
################################################################################

import os, sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

# GUI FILE
from views.ui_main import Ui_MainWindow

# IMPORT APP FUNCTIONS
from views.support_functions import *
from Database.db_functions import *

from Custom_Widgets.Widgets import *

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        my_icon = QIcon()
        my_icon.addFile('res/img/logo.png')

        self.setWindowIcon(my_icon)
        self.setWindowTitle("Servicios Bedoya")


        # APPLY JSON STYLESHEET
        loadJsonStyle(self, self.ui)

        ## SHOW MAIN WINDOW

        self.show()

        QAppSettings.updateAppSettings(self)
        
        #MAIN CONFIGURATIONS
        #START DATABASE
        init_tables()

        #RELOAD TABLES
        self.populate_user_table(select_all_users())
        self.populate_budget_table(select_all_budgets())
        self.populate_invoice_table(select_all_invoices())

        #BUTTONS CONFIGURATIONS 

        #CLIENTS
        self.ui.btn_adduser.clicked.connect(self.open_new_user_window)
        self.ui.btn_edituser.clicked.connect(self.open_edit_user_window)
        self.ui.btn_updateUserTable.clicked.connect(lambda: self.populate_user_table(select_all_users()))
        self.ui.btn_deleteuser.clicked.connect(self.remove_user)

        #BUDGETS
        self.ui.btn_addbudget.clicked.connect(self.open_new_budget_window) 
        self.ui.btn_updateBudgetTable.clicked.connect(lambda: self.populate_budget_table(select_all_budgets()))
        #self.ui.btn_editbudget.clicked.connect(self.open_edit_budget_window) 
        self.ui.btn_deletebudget.clicked.connect(self.remove_budget)

        #INVOICES
        self.ui.btn_addinvoice.clicked.connect(self.open_new_invoice_window)
        self.ui.btn_deleteinvoice.clicked.connect(self.remove_invoice)

        #delete DB
        self.ui.btn_deletebd.clicked.connect(self.destroybd)

    def populate_user_table(self, data):
        """
        It takes a list of lists (data) and populates a QTableWidget with the data. 
        
        The first line of the function sets the number of rows in the table to the number of lists in the
        data list. 
        
        The second line loops through the data list. 
        
        The third line loops through each list in the data list. 
        
        The fourth line populates the table with the data. 
        
        The fifth line calls the users_qty function. 
        
        The users_qty function is defined below.
        
        :param data: list of lists
        """
        self.ui.table_users.setRowCount(len(data))

        for index_row,row in enumerate(data):
            for index_cell, cell in enumerate(row):
                self.ui.table_users.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.users_qty()

    def populate_budget_table(self, data):

        self.ui.table_budgets.setRowCount(len(data))

        for index_row,row in enumerate(data):
            for index_cell, cell in enumerate(row):
                if(index_cell == 4):
                    #get user name
                    usr_name = select_user_by_id(cell)[2]
                    #print_log("User name: "+str(usr_name))
                    self.ui.table_budgets.setItem(index_row, index_cell, QTableWidgetItem(usr_name))
                else:
                    #regular data 
                    self.ui.table_budgets.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.budgets_qty()

    def populate_invoice_table(self, data):

        self.ui.table_invoices.setRowCount(len(data))

        for index_row,row in enumerate(data):
            for index_cell, cell in enumerate(row):
                if(index_cell == 4):
                    #get user name
                    usr_name = select_user_by_id(cell)[2]
                    #print_log("User name: "+str(usr_name))
                    self.ui.table_invoices.setItem(index_row, index_cell, QTableWidgetItem(usr_name))
                else:
                    #regular data 
                    self.ui.table_invoices.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        
        self.invoices_qty()

    def refresh_user_table_from_child_window(self):
        data = select_all_users()
        self.populate_user_table(data)

    def refresh_budget_table_from_child_window(self):
        data = select_all_budgets()
        self.populate_budget_table(data)

    def refresh_invoice_table_from_child_window(self):
        self.populate_invoice_table(select_all_invoices())

    def remove_user(self):
        """
        It removes a user from the database and the table widget
        """
        selected_row = self.ui.table_users.selectedItems()

        if selected_row:
            user_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_user(user_id):
                self.ui.table_users.removeRow(row)

        self.users_qty()

    def remove_budget(self):
        selected_row = self.ui.table_budgets.selectedItems()
        if selected_row:
            butget_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_budget(butget_id):
                self.ui.table_budgets.removeRow(row)

        self.budgets_qty()

    def remove_invoice(self):
        selected_row = self.ui.table_invoices.selectedItems()
        if selected_row:
            invoice_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_invoice(invoice_id):
                self.ui.table_invoices.removeRow(row)

        self.invoices_qty()

    def users_qty(self):
        """
        It counts the number of rows in a table and displays the result in a label.
        """
        qty_rows = str(self.ui.table_users.rowCount())
        self.ui.clients_qty.setText(qty_rows)

    def budgets_qty(self):
        qty_rows = str(self.ui.table_budgets.rowCount())
        self.ui.budget_qty.setText(qty_rows)
    
    def invoices_qty(self):
        qty_rows = str(self.ui.table_invoices.rowCount())
        self.ui.invoices_qty.setText(qty_rows)

    def open_new_user_window(self):
        from views.newUserWindow import NewUserWindow
        window = NewUserWindow(self)
        window.show()

    def open_new_budget_window(self):
        from views.newBudgetWindow import NewBudgetWindow
        window = NewBudgetWindow(self)
        window.show()
    
    def open_data_budget_window(self):
        from views.BudgetData import BudgetData
        window = BudgetData(self)
        window.show()


    def open_new_invoice_window(self):
        from views.newInvoiceWindow import NewInvoiceWindow
        window = NewInvoiceWindow(self)
        window.show()
    
    def open_edit_user_window(self):
        from views.editUserWindow import EditUserWindow
        selected_row = self.ui.table_users.selectedItems()

        if selected_row:
            user_id = int(selected_row[0].text())
            window = EditUserWindow(self, user_id)
            window.show()

        self.ui.table_users.clearSelection()


    def destroybd(self):
        msg = QMessageBox.critical(
                    self,
                    "Cuidado!",
                    "Estas seguro que quieres borrar todos los datos de la base de datos?",
                    buttons = QMessageBox.Ok | QMessageBox.Cancel,
                    defaultButton=QMessageBox.Ok
                )
        if msg == QMessageBox.Ok:
            print("BORRAR BASE DE DATOS :O")
            remove_db()
            init_tables()
        elif msg == QMessageBox.Cancel:
            print("NO SE BORRA LA BD, MENOS MAL 0.o")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())