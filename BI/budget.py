from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QFormLayout, QPushButton, QDateEdit
)

from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class UI_Budget(QLabel):
    def __init__(self):
        super().__init__()
        #self.setText(f"Hola has entrado en: {text}")
        self.setStyleSheet("background-color: white; background-image: url('res/img/logo.png');  background-position: center;")

        #Create some widgets for the page
        budget_page = QWidget(self)
        layout = QFormLayout()
        budget_page.setLayout(layout)
        layout.addRow('Nombre del presupuesto:', QLineEdit(self))
        layout.addRow('Cliente:', QLineEdit(self))
        layout.addRow('Fecha:', QDateEdit(self))

        budget_page.show()