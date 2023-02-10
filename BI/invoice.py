from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QFormLayout, QPushButton, QDateEdit
)

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class UI_Invoice(QLabel):
    def __init__(self):
        super().__init__()
        #self.setText(f"Hola has entrado en: {text}")
        self.setStyleSheet("background-color: white; background-image: url('res/img/logo.png');  background-position: center;")

        #Create some widgets for the page
        invoice_page = QWidget(self)
        layout = QFormLayout()
        invoice_page.setLayout(layout)
        layout.addRow('Nombre de la factura:', QLineEdit(self))
        layout.addRow('Cliente:', QLineEdit(self))
        layout.addRow('Fecha:', QDateEdit(self))

        invoice_page.show()