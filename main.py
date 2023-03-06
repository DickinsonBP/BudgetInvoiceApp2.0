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
from UI.ui_main import Ui_MainWindow

# IMPORT APP FUNCTIONS
from UI.functions import AppFunctions

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
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/DBP_DB.db'))
        
        #Run main function to create the database and the table
        AppFunctions.main(dbFolder)

        #Display all users
        AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))

        self.ui.btn_adduser.clicked.connect(lambda: AppFunctions.addUser(self,dbFolder))
        self.ui.btn_deleteuser.clicked.connect(lambda: AppFunctions.deleteUser(self,dbFolder))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())