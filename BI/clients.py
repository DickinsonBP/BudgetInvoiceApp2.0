from PySide6.QtWidgets import (
    QMainWindow, QLabel, QTabWidget, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout,
    QGridLayout, QFormLayout, QPushButton, QDateEdit, QListWidget, QListWidgetItem,
    QToolButton, QRadioButton, QTableView, QMessageBox, QDialog, QDialogButtonBox,
    QScrollArea
)

from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt, QPoint

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
        self.setStyleSheet("background-image: url('res/img/logo.png');  background-position: center;")

        #Create some widgets for the page
        self.client_page = QWidget(self)

        self.setup_frame()
        self.client_page.show()


    def setup_frame(self):
        # add client button
        print("Setup frame")
        new_client = QPushButton()
        new_client.setFixedSize(250, 64)
        new_client.setText("Nuevo cliente")
        new_client.setIcon(QIcon("res/img/icons/add.png"))
        new_client.setIconSize(new_client.size())
        new_client.setStyleSheet(" border: 0; font-size: 25px; ")
        new_client.clicked.connect(self.add_client)

        self.scroll_area = QScrollArea(widgetResizable=True)
        self.scroll_area.setViewportMargins(0,0,0,0)

        # layout where the widgets will be added
        self.main_layout = QGridLayout()
        self.main_layout.maximumSize().setHeight(500)

        self.client_page.setLayout(self.main_layout)

        self.main_layout.addWidget(new_client,0,0)
        self.main_layout.addWidget(self.scroll_area, 0, 3)
        
        self.readClients()

        #lista.setStyleSheet("icon-size: 50px; font-size: 20px; background-image: url('res/img/bg_yellow.png');")
        #self.main_layout.addWidget(client_list, 1, 0)


    def readClients_bak(self):
        print("Read Clients")
        #read clients
        if os.stat(CLIENTS).st_size == 0: 
            print("No hay clientes")
        else:

            lista = QListWidget()

            lista.setAlternatingRowColors(True)
            lista.setFixedHeight(800)
            lista.setFixedWidth(1850)

            item = None
            index = 0
            color_index = 0
            with open(CLIENTS, "r") as clients_file:
                print("File readin")
                line = clients_file.readline()
                while line != '':
                    client_data = line.split(';')
                    client = Client(client_data[0],client_data[1],client_data[2])
                    print("Client N°: "+str(index)+" --> "+client.getNombre()+" "+client.getNif())
                    item = QListWidgetItem(client.getNombre()+" "+client.getNif()+" "+client.getDireccion(), lista)
                    #item.setBackground(QColor(colors[color_index]))
                    item.setIcon(QIcon("res/img/icons/user.png"))
                    item.setTextAlignment(Qt.AlignLeft)
                    lista.addItem(item)
                    line = clients_file.readline()
                    
                    index += 1
                    color_index = (color_index + 1) % 2

            return lista

    def readClients(self):
        print("Read Clients")
        if os.stat(CLIENTS).st_size == 0:
            print("No hay clientes")
        else:
            
            name = QLabel("Nombre")
            address = QLabel("Direccion")
            nif = QLabel("NIF")

            name.setStyleSheet("icon-size: 50px; font-size: 40px; background-color: gray; background-attachment: fixed;")
            address.setStyleSheet("icon-size: 50px; font-size: 40px; background-color: gray;background-attachment: fixed;")
            nif.setStyleSheet("icon-size: 50px; font-size: 40px;background-color: gray; background-attachment: fixed;")
            
            self.main_layout.addWidget(name, 1, 0)
            self.main_layout.addWidget(address, 1, 1)
            self.main_layout.addWidget(nif, 1, 2)

            index = 2
            with open(CLIENTS, "r") as clients_file:
                line = clients_file.readline()
                while line != '':
                    client_data = line.split(';')
                    #client = Client(client_data[0],client_data[1],client_data[2])
                    #print("Client N°: "+str(index)+" --> "+client.getNombre()+" "+client.getNif())

                    for col in range(3):
                        cl = QLabel(client_data[col])
                        cl.setStyleSheet(
                                        """

                                            icon-size: 50px; font-size: 30px; 
                                            background-image: url('res/img/bg_yellow.png'); 
                                            background-position: center;
                                            background-attachment: fixed;    
                                        """)

                        self.main_layout.addWidget(cl, index, col)
                                    
                    index += 1
                    line = clients_file.readline()


    def add_client(self):

        resp = QMessageBox.warning(self, "Añadir un nuevo cliente", "¿Quieres añadir un nuevo cliente?", QMessageBox.Ok | QMessageBox.Cancel)
        
        if(resp == QMessageBox.Ok):
            print("Añadir")

            self.dialog = QDialog()
            self.dialog.setWindowTitle("Añadir un nuevo cliente")
            self.dialog.setWindowIcon(QIcon("res/img/logo.png"))
            self.dialog.setMinimumSize(700,200)     

            myButton = QDialogButtonBox(QDialogButtonBox.Ok)            
            myButton.accepted.connect(self.guardar)            
            layout = QFormLayout()
            msg = QLabel("Añadir un nuevo cliente")
            msg.setStyleSheet("font-size: 15px;")           
            layout.addWidget(msg)   

            self.clientName = QLineEdit()
            self.direccion = QLineEdit()
            self.nif = QLineEdit()

            layout.addRow('Nombre del cliente:', self.clientName)
            layout.addRow('Direccion:', self.direccion)
            layout.addRow('NIF:', self.nif)            
            layout.addWidget(myButton)
            self.dialog.setLayout(layout)

            self.dialog.exec()


        else: print("Continuar")

    def guardar(self):
        """
        It opens a file, writes some text to it, closes the file, and then calls a function
        """
        print("Guardar")

        with open(CLIENTS, "a") as clients_file:
            text = "\n"+self.clientName.text()+";"+self.direccion.text()+";"+self.nif.text()
            clients_file.write(text)

        self.dialog.close()
        self.readClients()


class UI_Client_bak(QLabel):
    def __init__(self):
        super().__init__()
        #self.setText(f"Hola has entrado en: {text}")
        self.setStyleSheet("background-image: url('res/img/logo.png');  background-position: center;")

        #Create some widgets for the page
        self.client_page = QWidget(self)

        self.setup_frame()
        self.client_page.show()

    def setup_frame(self):
        # add client button
        print("Setup frame")
        new_client = QPushButton()
        new_client.setFixedSize(250, 64)
        new_client.setText("Nuevo cliente")
        new_client.setIcon(QIcon("res/img/icons/add.png"))
        new_client.setIconSize(new_client.size())
        new_client.setStyleSheet(" border: 0; font-size: 25px; ")
        new_client.clicked.connect(self.add_client)

        # layout where the widgets will be added
        self.main_layout = QGridLayout()

        self.client_page.setLayout(self.main_layout)

        self.main_layout.addWidget(new_client,0,0)
        
        lista = self.readClients()

        lista.setStyleSheet("icon-size: 50px; font-size: 20px; background-image: url('res/img/bg_yellow.png');")
        self.main_layout.addWidget(lista, 1, 0)


    def readClients(self):
        print("Read Clients")
        #read clients
        if os.stat(CLIENTS).st_size == 0: 
            print("No hay clientes")
        else:

            lista = QListWidget()

            lista.setAlternatingRowColors(True)
            lista.setFixedHeight(800)
            lista.setFixedWidth(1850)

            item = None
            index = 0
            color_index = 0
            with open(CLIENTS, "r") as clients_file:
                print("File readin")
                line = clients_file.readline()
                while line != '':
                    client_data = line.split(';')
                    client = Client(client_data[0],client_data[1],client_data[2])
                    print("Client N°: "+str(index)+" --> "+client.getNombre()+" "+client.getNif())
                    item = QListWidgetItem(client.getNombre()+" "+client.getNif()+" "+client.getDireccion(), lista)
                    #item.setBackground(QColor(colors[color_index]))
                    item.setIcon(QIcon("res/img/icons/user.png"))
                    item.setTextAlignment(Qt.AlignLeft)
                    lista.addItem(item)
                    line = clients_file.readline()
                    
                    index += 1
                    color_index = (color_index + 1) % 2

            return lista


    def add_client(self):

        resp = QMessageBox.warning(self, "Añadir un nuevo cliente", "¿Quieres añadir un nuevo cliente?", QMessageBox.Ok | QMessageBox.Cancel)
        
        if(resp == QMessageBox.Ok):
            print("Añadir")

            self.dialog = QDialog()
            self.dialog.setWindowTitle("Añadir un nuevo cliente")
            self.dialog.setWindowIcon(QIcon("res/img/logo.png"))
            self.dialog.setMinimumSize(700,200)     

            myButton = QDialogButtonBox(QDialogButtonBox.Ok)            
            myButton.accepted.connect(self.guardar)            
            layout = QFormLayout()
            msg = QLabel("Añadir un nuevo cliente")
            msg.setStyleSheet("font-size: 15px;")           
            layout.addWidget(msg)   

            self.clientName = QLineEdit()
            self.direccion = QLineEdit()
            self.nif = QLineEdit()

            layout.addRow('Nombre del cliente:', self.clientName)
            layout.addRow('Direccion:', self.direccion)
            layout.addRow('NIF:', self.nif)            
            layout.addWidget(myButton)
            self.dialog.setLayout(layout)

            self.dialog.exec()


        else: print("Continuar")
    

    def clearlayout(self):
        children = []
        for i in range(self.main_layout.count()):
            child = self.main_layout.itemAt(i).widget()
            if child:
                children.append(child)
                print(child)

        for child in children:
            child.deleteLater()
            

    def guardar(self):
        """
        It opens a file, writes some text to it, closes the file, and then calls a function
        """
        print("Guardar")

        with open(CLIENTS, "a") as clients_file:
            text = "\n"+self.clientName.text()+";"+self.direccion.text()+";"+self.nif.text()
            clients_file.write(text)

        self.dialog.close()
        self.setup_frame()


            
        

