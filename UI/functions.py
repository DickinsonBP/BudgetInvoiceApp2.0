import os, sys
#Database import
import sqlite3
from sqlite3 import Error
#Pyside6 import
from PySide6.QtWidgets import QTableWidgetItem

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
        create_user_table= """ CREATE TABLE IF NOT EXISTS Users (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,USER_NIF TEXT,USER_NAME TEXT,USER_EMAIL TEXT,USER_ADDRESS TEXT,USER_PHONE TEXT) """
        conn = AppFunctions.create_connection(dbFolder)

        if conn is not None:
            print("MAIN CONNECTION")
            AppFunctions.create_table(conn, create_user_table)
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
    
    def addUser(self, dbFolder):

        conn = AppFunctions.create_connection(dbFolder)

        nif = self.ui.nif.text()
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phone = self.ui.phone.text()
        address = self.ui.address.text()


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
    
    def displayUsers(self, rows):
        for row in rows:
            print("AAAAAAAAAAAAAAAAAAA")
            rowPos = self.ui.tableWidget.rowCount()

            #skip rows that have already been loaded to table
            if rowPos > row[0]:
                continue

            itemCount = 0
            #new table row
            self.ui.tableWidget.setRowCount(rowPos + 1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPos, qtablewidgetitem)

            #add items to row

            for item in row:
                print("Item: "+str(item))
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPos, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPos, itemCount)
                self.qtablewidgetitem.setText(str(item))
                itemCount = itemCount + 1
            
            rowPos = rowPos + 1
            
