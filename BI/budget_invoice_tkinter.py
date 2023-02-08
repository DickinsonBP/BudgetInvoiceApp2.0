import tkinter as tk
from tkinter import ttk
import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    #print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

master = tk.Tk()
master.title("Generador de presupuestos")

class BudgetInvoice():
    def start(self):
        print('Started!!')
        setupMainWindow()

def switch_frames(page):
    page()

def home_page():
    home_frame = tk.Frame(master)

    lb = tk.Label(home_frame, text = 'Home page', font=('Bold', 10))
    lb.pack()

    home_frame.pack(pady = 20)

def setupMainWindow():
    #screen size
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    master.geometry("%dx%d" % (screen_width, screen_height))

    options_frame = tk.Frame(master, bg ='#c3c3c3') #frame for master window

    options_frame.pack(side = tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width = 300, height = screen_height)

    main_frame = tk.Frame(master, highlightbackground = 'black', highlightthickness = 2,)
    main_frame.pack(side = tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width = screen_width - 300, height = screen_height)

    indicate = tk.Label(options_frame, text = '', bg='#158aff')
    indicate.place(x = 2, y = 50, width = 5, height = 780)

    home_btn = tk.Button(options_frame, text= 'Inicio', font = ('Bold', 30), fg = '#158aff', bd = 0, bg ='white', command = switch_frames(home_page))
    home_btn.place(x = 20, y = 100)


    budget_btn = tk.Button(options_frame, text= 'Presupuestos', font = ('Bold', 30), fg = '#158aff', bd = 0, bg ='white')
    budget_btn.place(x = 20, y = 300)
    invoice_btn = tk.Button(options_frame, text= 'Facturas', font = ('Bold', 30), fg = '#158aff', bd = 0, bg ='white')
    invoice_btn.place(x = 20, y = 500)
    clients_btn = tk.Button(options_frame, text= 'Clientes', font = ('Bold', 30), fg = '#158aff', bd = 0, bg ='white')
    clients_btn.place(x = 20, y = 700)


    master.mainloop()


