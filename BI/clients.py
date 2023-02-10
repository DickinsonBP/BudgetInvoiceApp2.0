from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, 
    QGridLayout, QFormLayout, QPushButton, QDateEdit, QListWidget, QListWidgetItem
)

from PySide6 import QtGui
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from BI.constants import CLIENTS

import os

# It's a class that has three attributes (nombre, direccion, nif) and three methods (getNombre,
# getDireccion, getNif) that return the value of the attributes
class Client(object):
    def __init__(self, nombre, direccion, nif):
        self.nombre = nombre
        self.direccion = direccion
        self.nif = nif
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getNif(self):
        return self.nif


class UI_Client(QLabel):
    def __init__(self):
        super().__init__()
        #self.setText(f"Hola has entrado en: {text}")
        self.setStyleSheet("background-color: white; background-image: url('res/img/logo.png');  background-position: center;")

        #Create some widgets for the page
        client_page = QWidget(self)

        new_client = QPushButton("Nuevo cliente?")
        new_client.clicked.connect(self.add_client)
        #layout = QFormLayout()
        #client_page.setLayout(layout)
        #layout.addRow('Nombre y apellidos:', QLineEdit(self))
        #layout.addRow('NIF:', QLineEdit(self))
        #layout.addRow('Direccion:', QLineEdit(self))


        
        layout = QVBoxLayout()
        layout.addStretch(1)

        client_page.setLayout(layout)

        layout.addWidget(new_client)
        
        #read clients
        if os.stat(CLIENTS).st_size == 0: 
            print("No hay clientes")
        else:
            lista = QListWidget()

            lista.setAlternatingRowColors(True)

            item = None
            index = 0
            with open(CLIENTS, "r") as clients_file:
                #print(clients_file.read())
                line = clients_file.readline()
                while line != '':
                    client_data = line.split(';')
                    client = Client(client_data[0],client_data[1],client_data[2])
                    print("Client N°: "+str(index)+" --> "+client.getNombre()+" "+client.getNif())
                    index += 1
                    item = QListWidgetItem(client.getNombre()+" "+client.getNif(), lista)
                    item.setIcon(QIcon("res/img/icons/user.png"))
                    lista.addItem(item)

                    line = clients_file.readline()

            layout.addWidget(lista)

        client_page.move(QtGui.QGuiApplication.primaryScreen().availableGeometry().center() - client_page.frameGeometry().center())
        client_page.show()


    def add_client(self):
        print("Hola")
        


            
        

