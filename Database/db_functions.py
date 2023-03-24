from sqlite3 import Error
import sqlite3
import os
import json
import datetime

from views.support_functions import print_log

tables = {
    "USER":" CREATE TABLE IF NOT EXISTS Users (USER_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,USER_NIF TEXT,USER_NAME TEXT,USER_EMAIL TEXT,USER_ADDRESS TEXT,USER_PHONE TEXT) ",
    "BUDGET":" CREATE TABLE IF NOT EXISTS Budgets (BUDGET_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,BUDGET_NUMBER INT NOT NULL,BUDGET_TITLE TEXT, BUDGET_DATE DATE, BUDGET_ADDRESS TEXT, USER_ID INTEGER NOT NULL, BUDGET_PATH TEXT, CONSTRAINT FK_USER_ID FOREIGN KEY (USER_ID) REFERENCES User (USER_ID)) ",
    "INVOICE":" CREATE TABLE IF NOT EXISTS Invoices (INVOICE_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,INVOICE_NUMBER INT NOT NULL,INVOICE_TITLE TEXT, INVOICE_DATE DATE, INVOICE_ADDRESS TEXT, USER_ID INTEGER NOT NULL,BUDGET_ID INTEGER,INVOICE_PATH TEXT, CONSTRAINT FK_USER_ID FOREIGN KEY (USER_ID) REFERENCES User (USER_ID),CONSTRAINT FK_BUDGET_ID FOREIGN KEY (BUDGET_ID) REFERENCES Budget (BUDGET_ID)) "
}

insert_tables = {
    "USER": f""" INSERT INTO Users (USER_NIF, USER_NAME, USER_EMAIL, USER_ADDRESS, USER_PHONE) 
                    VALUES(?, ?, ?, ?, ?)
        """,
    "BUDGET":f""" INSERT INTO Budgets (BUDGET_NUMBER,BUDGET_TITLE, BUDGET_DATE, USER_ID, BUDGET_PATH, BUDGET_ADDRESS) 
                    VALUES(?, ?, ?, ?, ?, ?)
        """,
    "INVOICE":f""" INSERT INTO Invoices (INVOICE_NUMBER,INVOICE_TITLE, INVOICE_DATE, USER_ID, INVOICE_PATH, INVOICE_ADDRESS) 
                    VALUES(?, ?, ?, ?, ?, ?)
        """
}


def create_connection(where):

    try:
        data = json.load(open('json/credentials.json'))
        conn = sqlite3.connect(data['dbFile'])
        #print_log(f"CONEXION CON LA BD DESDE {where.upper()} OK")
        return conn
    except Error as e:
        print_log(f"ERROR! No se ha podido conectar a la base de datos desde {where}: "+ str(e))

def init_tables():
    conn = create_connection("init tables")
    if conn is not None:
        for table, sql in tables.items():
            create_table(conn, table, sql)
        #print_log("TABLAS CREADAS OK")
    else:
        print_log("Error! No se ha podido crear conexcion con la BD")

def create_table(conn, table, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        #print_log(f"CREAR TABLA {table} OK")
    except Error as e:
        print_log(f"ERROR! No se ha podido crear la tabla {table}: "+str(e))

def insert_data(data, table):
    conn = create_connection("insert_data")
    sql = insert_tables[table.upper()]

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        #print_log(f"INSERT {table} OK. DATA: "+str(data)+" SQL: "+str(sql))
        return True, cur.lastrowid
    except Error as e:
        print_log(f"ERROR! No se ha podido hacer el insert {sql}. Error --> "+str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def update_user(_id, data):
    conn = create_connection("update_user")

    sql = f""" UPDATE Users SET  
                            USER_NIF = ?,
                            USER_NAME = ?,
                            USER_EMAIL = ?,
                            USER_ADDRESS = ?,
                            USER_PHONE = ?
            WHERE USER_ID = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        #print_log("USUARIO ACTUALIZADO")
        return True
    except Error as e:
        print_log("ERROR! No se ha podido actualizar los datos del usuario: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_user(_id):
    conn = create_connection("delete_user")
    sql = f"DELETE FROM Users WHERE USER_ID = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        #print_log("USUARIO ELIMINADO")
        return True
    except Error as e:
        print_log("ERROR! No se ha podido eliminar al usuario: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_budget(_id):
    conn = create_connection("delete_budget")
    sql = f"DELETE FROM Budgets WHERE BUDGET_ID = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        #print_log("PRESUPUESTO ELIMINADO")
        return True
    except Error as e:
        print_log("ERROR! No se ha podido eliminar el presupuesto: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_invoice(_id):
    conn = create_connection("delete_invoice")
    sql = f"DELETE FROM Invoices WHERE INVOICE_ID = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        #print_log("FACTURA ELIMINADA")
        return True
    except Error as e:
        print_log("ERROR! No se ha podido eliminar la factura: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_users():
    conn = create_connection("select_all_users")
    sql = "SELECT * FROM Users"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        #print_log("SELECCIONAR TODOS LOS USUARIOS OK")
        return books
    except Error as e:
        print_log("ERROR! No se ha podido seleccionar todos los usuarios: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_budgets():
    conn = create_connection("select_all_budgets")
    sql = "SELECT * FROM Budgets"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        #print_log("SELECCIONAR TODOS LOS PRESUPUESTOS OK")
        return books
    except Error as e:
        print_log("ERROR! No se ha podido seleccionar todos los presupuestos: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_invoices():
    conn = create_connection("select_all_invoices")
    sql = "SELECT * FROM Invoices"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        #print_log("SELECCIONAR TODAS LAS FACTURAS OK")
        return books
    except Error as e:
        print_log("ERROR! No se ha podido seleccionar todas las facturas. Error --> " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_user_by_id(_id):
    conn = create_connection("select_user_by_id")
    sql = f"SELECT * FROM Users WHERE USER_ID = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        usr = cur.fetchone()
        #print_log(f"SELECCIONAR EL USUARIO CON ID {_id} OK")
        return usr
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar el usuario con id {_id}: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_budget_by_id(_id):
    conn = create_connection("select_budget_by_id")
    sql = f"SELECT * FROM Budgets WHERE BUDGET_ID = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        bg = cur.fetchone()
        #print_log(f"SELECCIONAR EL USUARIO CON ID {_id} OK")
        return bg
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar el presupuesto con id {_id}: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_user_by_name(name):
    conn = create_connection("select_user_by_name")
    sql = f"SELECT * FROM Users WHERE USER_NAME LIKE '%{name}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        user = cur.fetchone()
        #print_log(f"SELECCIONAR EL USUARIO CON NOMBRE {name} OK")
        return user
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar el usuario con nombre {name}: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_user_by_phone(phone):
    conn = create_connection("select_user_by_phone")
    sql = f"SELECT * FROM Users WHERE USER_PHONE LIKE '%{phone}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        #print_log(f"SELECCIONAR EL USUARIO CON TELEFONO {phone} OK")
        return books
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar el usuario con telefono {phone}: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def get_next_invoice_id():
    conn = create_connection("get_next_invoice_id")
    sql = f"SELECT INVOICE_ID FROM Invoices"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ids = cur.fetchall()
        #print_log(f"SELECCIONAR LOS ID's DE FACTURAS OK. ID's: "+str(ids))
        if(not ids): return 1
        else: return int(ids[-1][-1]) + 1
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar los id de las facturas: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def get_next_budget_id():
    conn = create_connection("get_next_invoice_id")
    sql = f"SELECT BUDGET_ID FROM Budgets"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        ids = cur.fetchall()
        #print_log(f"SELECCIONAR LOS ID's DE PRESUPUESTOS OK. ID's: "+str(ids))
        if(not ids): return 1
        else: return int(ids[-1][-1]) + 1
    except Error as e:
        print_log(f"ERROR! No se ha podido seleccionar los id de los presupuestos: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def remove_db():
    date = datetime.datetime.now().strftime("%d_%m_%Y")
    src = 'Database/DBP_DB.db'
    dest = 'Database/DBP_DB.db_'+str(date)
    os.popen(f'copy {src} {dest}')
    os.remove(src)
    