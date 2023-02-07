import tkinter as tk
from tkinter import ttk
import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

def convertir_temp():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheit = temp_celsius*1.8 + 32
    etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin}")
    etiqueta_temp_fahrenheit.config(
        text=f"Temperatura en ºF: {temp_fahrenheit}")


master = tkinter.Tk()
master.title("Conversor de temperatura")
master.config(width=400, height=300)

etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(text="Convertir", command=convertir_temp)
boton_convertir.place(x=20, y=60)

etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
etiqueta_temp_kelvin.place(x=20, y=120)
etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
etiqueta_temp_fahrenheit.place(x=20, y=160)

master.mainloop()


class BudgetInvoice():
    def start(self):
        print('Started!!')
