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
from views.functions import AppFunctions
from Database.db_functions import select_all_users, delete_user

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

        ## TOGGLE/BURGUER MENU
        ########################################################################
        #self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

              # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        #settings.setValue("THEME", "Default-Dark")
            
        # RE APPLY THE NEW SETINGS
        # CompileStyleSheet might also work
        # CompileStyleSheet.applyCompiledSass(self)
        #QAppSettings.updateAppSettings(self)

        # DataBase Folder
        #dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/DBP_DB.db'))
        
        #Run main function to create the database and the table
        AppFunctions.main()

        #Display all users
        #AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))

        self.populate_user_table(select_all_users())
        self.ui.btn_updateUserTable.clicked.connect(lambda: self.populate_user_table(select_all_users()))
        self.ui.btn_adduser.clicked.connect(self.open_new_user_window)
        self.ui.btn_edituser.clicked.connect(self.open_edit_user_window)
        self.ui.btn_deleteuser.clicked.connect(self.remove_user)


        #self.ui.btn_addbudget.clicked.connect(lambda: AppFunctions.addBudget(self,dbFolder))
        #self.ui.btn_addbudgettemplate.clicked.connect(lambda: AppFunctions.addBudgetTemplate(self,dbFolder))



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

    def refresh_user_table_from_child_window(self):
        data = select_all_users()
        self.populate_user_table(data)
        
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

    def users_qty(self):
        """
        It counts the number of rows in a table and displays the result in a label.
        """
        qty_rows = str(self.ui.table_users.rowCount())
        self.ui.clients_qty.setText(qty_rows)

    def open_new_user_window(self):
        from views.newUserWindow import NewUserWindow
        window = NewUserWindow(self)
        window.show()
    
    def open_edit_user_window(self):
        from views.editUserWindow import EditUserWindow
        selected_row = self.ui.table_users.selectedItems()

        if selected_row:
            user_id = int(selected_row[0].text())
            window = EditUserWindow(self, user_id)
            window.show()

        self.ui.table_users.clearSelection()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())