from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QFormLayout, QPushButton, QDateEdit
)

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from BI.clients import Client
from BI.invoice import Invoice
from BI.budget import Budget

        

class Tab2(QWidget):
    def __init__(self):
        super().__init__()

class Tab3(QWidget):
    def __init__(self):
        super().__init__()

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
        tabs.addTab(Budget(),"Presupuestos")
        tabs.addTab(Invoice(),"Facturas")
        tabs.addTab(Client(),"Clientes")

        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        self.setCentralWidget(tabs)

        #lo.addWidget(tabs)
        #self.setLayout(lo)


    def presupuesto(parent):
        budget_tab = QWidget(parent)
        layout = QVBoxLayout()
        purpose = QLabel("Holaa")

        layout.addWidget(purpose)
        budget_tab.setLayout(layout)
        budget_tab.show()