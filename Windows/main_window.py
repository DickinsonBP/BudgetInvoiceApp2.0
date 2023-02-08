from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QToolBar, QStatusBar, QMessageBox, QLabel, QVBoxLayout, QMdiArea
from PySide6.QtCore import QSize
from PySide6 import QtGui
from PySide6.QtGui import QAction, QIcon, QPixmap

from Windows.side_menu import SideMenu
from Windows.content import Content
from Windows.overlay import Overlay

class MdiArea(QMdiArea):
    def __init__(self):
        super(MdiArea,self).__init__()
        self.menu = SideMenu()
        self.content = Content(self)
        self.overlay = Overlay(self)

        self.addSubWindow(self.content)
        self.addSubWindow(self.overlay)
        self.addSubWindow(self.menu)

    def resizeEvent(self, event):
        self.content.resize(self.width(), self.height())
        self.overlay.resize(self.width(), self.height())
        self.menu.resize(270, self.height())


class MainWindow(QMainWindow):
    def __init__ (self, app):
        super().__init__()
        self.app = app      # declare an app member
        self.setWindowTitle("Generador de Presupuestos y Facturas")

        #window size        
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().availableGeometry())

        self.mdi = MdiArea()
        self.setCentralWidget(self.mdi)

        
        ## Menu bar
        menu_bar = self.menuBar()
#
        #file_menu = menu_bar.addMenu("File")
        #quit_action = menu_bar.addAction("Salir")
        #quit_action.triggered.connect(self.button_close)
#
        #budget = menu_bar.addAction("Presupuestos") 
        #budget.triggered.connect(self.button_budget)   
#
        #invoice = menu_bar.addAction("Facturas")   
        #invoice.triggered.connect(self.button_invoice)
#
        #clients = menu_bar.addAction("Clientes")
        #clients.triggered.connect(self.button_clients)
#
        #help = menu_bar.addAction("Ayuda")
        #help.triggered.connect(self.button_help)

        #Working with toolbars
        #toolbar = QToolBar("My main toolbar")  
        #toolbar.setIconSize(QSize(16, 16))
        #self.addToolBar(toolbar)
#
        ##Add the quit action to the toolbar
        ##toolbar.addAction(quit_action)
#
        #action1 = QAction("Some Action", self)
        #action1.setStatusTip("Status message for some action")
        #action1.triggered.connect(self.toolbar_button_click)
        #toolbar.addAction(action1)
#
        #action2 = QAction("Some other action", self)
        #action2.setStatusTip("Status message for some other action")
        #action2.triggered.connect(self.toolbar_button_click)
        ##action2.setCheckable(True)
        #toolbar.addAction(action2)
#
        ## separator
        #toolbar.addSeparator()
        #toolbar.addWidget(QPushButton("Click here"))


        # Working with status bars. This is where the text will show up
        #self.setStatusBar(QStatusBar(self))

        #button1 = QPushButton("BUTTON1")
        #button1.setIcon(QIcon("/logo.png"))
        #button1.clicked.connect(self.button1_clicked)

        #self.setCentralWidget(button1)

        img_label = QLabel()
        img_label.setPixmap(QPixmap("/images/logo.png"))

        layout = QVBoxLayout()
        #layout.addWidget(button1)
        layout.addWidget(img_label)

        self.setLayout(layout)


    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        # the second parameter indicates the time the text will be showed
        self.statusBar().showMessage("Message from my app",3000)

    def button1_clicked(self):
        print("Clicked on the button")

    def button_close(self):
        ret = QMessageBox.warning(self, "Salir", "Seguro que quieres salir?", QMessageBox.Ok | QMessageBox.Cancel)
        if (ret == QMessageBox.Ok):
            print("Quit app")
            self.quit_app()
        else:
            print("Choise Cancel. Continue execution")

    def button_budget(self):
        print("Presupuesto")
    
    def button_invoice(self):
        print("Factura")

    def button_clients(self):
        print("Clientes")
    
    def button_help(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Ayuda")
        message.setText("")
        message.setInformativeText("Necesitas Ayuda?")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if (ret == QMessageBox.Ok):
            print("Help")
            message = QMessageBox()
            message.setMinimumSize(700,200)
            message.setWindowTitle("Ayuda")
            message.setText("Ayuda!!")
            message.setInformativeText("Para usar la aplicacion debes ir al menu de arriba y usar los botones indicados en cada ventana.")
            message.setIcon(QMessageBox.Information)
            message.setStandardButtons(QMessageBox.Help)
            message.setDefaultButton(QMessageBox.Ok)

            #Show the message box
            ret2 = message.exec()
            if ret2 == QMessageBox.Ok : 
                print("User chose OK")
            else : 
                print ("User chose Cancel")
        else:
            print("No help")