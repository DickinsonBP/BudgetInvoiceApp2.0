from PySide6.QtWidgets import QApplication, QWidget
from Windows.main_window import MainWindow
from PySide6.QtGui import QFontDatabase
import sys
import os

app = ''

class BudgetInvoice():
    def start(self):
        print('Started!!')
        setupMainWindow()

def setupMainWindow():
    app = QApplication(sys.argv)

    font_db = QFontDatabase()
    font_db.addApplicationFont("res/fonts/Roboto-Black.ttf")
    font_db.addApplicationFont("res/fonts/Roboto-Light.ttf")

    window = MainWindow(app)
    window.show()
    app.exec()