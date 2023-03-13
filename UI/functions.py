import os, sys
#Database import
import sqlite3
from sqlite3 import Error
#Pyside6 import
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QDialogButtonBox, QLabel,QVBoxLayout

class AppFunctions():
    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("CONNECTION OK!")
        except Error as e:
            print(e)
        
        return conn
    
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            print("TABLE CREATED OK")
        except Error as e:
            print("FAILED CREATING TABLE")
            print(e)

    def main(dbFolder):
        tables = [
            " CREATE TABLE IF NOT EXISTS Users (USER_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,USER_NIF TEXT,USER_NAME TEXT,USER_EMAIL TEXT,USER_ADDRESS TEXT,USER_PHONE TEXT) ",
            " CREATE TABLE IF NOT EXISTS Budgets (BUDGET_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, BUDGET_NAME TEXT, USER_ID INTEGER NOT NULL,CONSTRAINT FK_USER_ID FOREIGN KEY (USER_ID) REFERENCES User (USER_ID)) "
        ]
        conn = AppFunctions.create_connection(dbFolder)

        if conn is not None:
            print("MAIN CONNECTION")
            for table in tables:
                AppFunctions.create_table(conn, table)
        else:
            print("Error! Cannot create the database connection.")
    
    def getAllUsers(dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

        get_all_users = "SELECT * FROM Users;"

        try:
            c = conn.cursor()
            c.execute(get_all_users)
            print("GET ALL USERS OK")
            #print("Users: "+str(c.fetchall()))
            return c
        except Error as e:
            print("ERROR! Get all users has failed")
            print(e)
    
    
    def displayUsers(self, rows):
        for row in rows:
            rowPos = self.ui.tableWidget.rowCount()

            #skip rows that have already been loaded to table
            if rowPos+1 > row[0]:
                continue

            itemCount = 0
            #new table row
            self.ui.tableWidget.setRowCount(rowPos + 1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPos, qtablewidgetitem)

            #add items to row

            for item in row:
                #print("Item: "+str(item))
                self.qtablewidgetitem = QTableWidgetItem()
                self.qtablewidgetitem.setText(str(item))
                self.ui.tableWidget.setItem(rowPos, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPos, itemCount)
                itemCount = itemCount + 1
            
            rowPos = rowPos + 1
            
    def addUser(self, dbFolder):

        conn = AppFunctions.create_connection(dbFolder)

        nif = self.ui.nif.text()
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phone = self.ui.phone.text()
        address = self.ui.address.text()

        if nif != '' and userName !=  '':
            add_user = f"""INSERT INTO Users (USER_NIF, USER_NAME, USER_EMAIL, USER_ADDRESS, USER_PHONE) VALUES('{nif}','{userName}','{email}','{phone}','{address}')"""

            if not conn.cursor().execute(add_user):
                print("Error! Could not insert person data")
            else:
                print("ADD USER OK!")
                conn.commit()
                #clear from input
                self.ui.nif.setText("")
                self.ui.userName.setText("")
                self.ui.email.setText("")
                self.ui.phone.setText("")
                self.ui.address.setText("")

                AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))
        else:
            print("ERROR! Empty User Input")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Borrar usuario?")
            dlg.setText("Por favor introduce un dato valido")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)

            dlg.exec()
    
    def deleteUser(self, dbFolder):
        conn = AppFunctions.create_connection(dbFolder)

        nif = self.ui.nif_2.text()

        if nif != '':
            
            select_user=f"SELECT USER_NAME FROM Users WHERE USER_NIF='{nif}'"

            c = conn.cursor()
            
            # the user exists
            if c.execute(select_user):

                name = c.fetchall()[0][0]

                dlg = QMessageBox(self)
                dlg.setWindowTitle("Borrar usuario?")
                dlg.setText(f"Seguro que quieres borrar a {name}??")
                dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg.setIcon(QMessageBox.Question)

                btn = dlg.exec()

                if btn == QMessageBox.Yes:
                    delete_user = f"DELETE FROM Users WHERE USER_NIF='{nif}'"

                    if not conn.cursor().execute(delete_user):
                        print("ERROR! Could not delete user")
                        dlg.setText("No se ha podido borrar el usuario")
                        dlg.setStandardButtons(QMessageBox.Ok)
                        dlg.setIcon(QMessageBox.Warning)
                    else:
                        print("DELETE USER OK!")
                        dlg2 = QMessageBox(self)
                        dlg2.setText("El usuario se ha borrado correctamente, se actualizará cuando reinicies la aplicación")
                        dlg2.setStandardButtons(QMessageBox.Ok)
                        dlg2.setIcon(QMessageBox.Information)
                        dlg2.exec()
                        conn.commit()
                        #clear from input
                        self.ui.nif_2.setText("")

                else:
                    print(f"CONTIUNE! The user {name} will not be deleted")
            else:
                print("ERROR! The user does not exist!")
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Borrar usuario?")
                dlg.setText("El usuario introducido no existe en la base de datos")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Warning)

                btn = dlg.exec()
        else:
            print("Empty Input")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Borrar usuario?")
            dlg.setText("Por favor introduce un dato valido")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Warning)

            dlg.exec()
        
        #Always show the users 
        AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))

    def addBudget(self,dbFolder):
        print("PRESUPUESTO")

    def addBudgetTemplate(self,dbFolder):
        print("PRESUPUESTO PLANTILLA")

    