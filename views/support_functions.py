import os, sys, datetime
#Database import
import sqlite3
from sqlite3 import Error
#Pyside6 import
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QDialogButtonBox, QLabel,QVBoxLayout
from PySide6.QtCore import Qt



def check_cif(cif):

    not_allowed = '/[\'^£$%&*()}{@#~?><>,|=_+¬-]/'
    dni_nie_word = "TRWAGMYFPDXBNJZSQVHLCKE"
    word_res = "JABCDEFGHI"
    other_cif = ["P","Q","R","S","W"]


    cif = cif.upper()
    first = cif[0]
    
    if(len(cif) > 9):
        return (False, "La longitud del CIF es incorrecta, sobran datos")
    elif(len(cif) < 9):
        return (False, "La longitud del CIF es incorrecta, faltan datos")
    else:
        if any(c in not_allowed for c in cif):
            #ERROR. Not allowed characters
            return (False, "No se permiten los siguientes caracteres en el CIF: "+not_allowed)
        else:
            if(type(first) == int):
                #DNI
                num = int(cif[:8])
                letter = cif[-1]

                if(dni_nie_word[num % 23] == letter):
                    return (True, "")
                else:
                    return (False, "El numero del DNI esta mal, por favor revisa y vuelve a introducirlo correctamente")

            elif(first == "X" or first == "Y"):
                #NIE
                num = int(cif[1:8])
                letter = cif[-1]

                if(dni_nie_word[num % 23] == letter):
                    return (True, "")
                else:
                    return (False, "El numero del NIE esta mal, por favor revisa y vuelve a introducirlo correctamente")
            else:
                #CIF
                num = int(cif[1:8])
                last = cif[-1]

                total = int(num[1]) + int(num[3]) + int(num[5])

                odd_val = [
                    str(int(num[0])*2),
                    str(int(num[2])*2),
                    str(int(num[4])*2),
                    str(int(num[6])*2)
                ]

                for val in odd_val:
                    if(len(val) > 1):
                        total = total + int(val[0]) + int(val[1])
                    else:
                        total = total + int(val[0])
                
                total = 10 - total[1]

                if(first in other_cif):
                    if(word_res[total] == last): return (True, "")
                    else: return (False, "La letra de control del CIF (la ultima) esta mal, por favor revisa y vuelve a introducirlo correctamente")
                else:
                    if(total == last): return (True, "")
                    else: return (False, "El numero de control del CIF (el ultimo) esta mal, por favor revisa y vuelve a introducirlo correctamente")

def print_log(msg):
    try:
        actual_date = datetime.datetime.now().strftime("%d_%m_%Y")
        file_path = "./logs/log_"+actual_date+".log"
        date_and_hour = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        if (os.path.isfile(file_path)):log = open(file_path, "a")
        else: log = open(file_path, "w")
        
        log.write(f"[{date_and_hour}]"+str(msg)+"\n")
        print(f"[{date_and_hour}]"+str(msg))
        log.close()
    except Exception as e:
        print(f"[{date_and_hour}]: Error! No se ha podido añadir el mensaje: "+str(msg)+" error --> "+str(e))