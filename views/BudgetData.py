from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from .ui_budgetdata import Ui_BudgetData
#from Data.books import insert_book, select_book_by_id
import shutil
import os
import datetime

from views.support_functions import *

from Database.db_functions import insert_data, select_all_users, select_user_by_name, get_next_budget_id

class BudgetData(QWidget, Ui_BudgetData):

    def __init__(self, number, parent=None):
        super().__init__(parent)
        self.number = number
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #self.populate_budget_number()

    def populate_budget_number(self):
        self.budget_number.setText(self.number)