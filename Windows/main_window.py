from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QFormLayout, QPushButton, QDateEdit
)

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from BI.clients import UI_Client
from BI.invoice import UI_Invoice
from BI.budget import UI_Budget


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Generador de Presupuestos y Facturas")
        self.setWindowIcon(QIcon("res/img/logo.png"))

        #window size        
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().availableGeometry())
        
    
        #create the layout for the tabs
        tabs = QTabWidget()

        #Add some tabs
        tabs.addTab(UI_Client(),"Clientes")
        tabs.addTab(UI_Budget(),"Presupuestos")
        tabs.addTab(UI_Invoice(),"Facturas")

        #tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        self.setCentralWidget(tabs)