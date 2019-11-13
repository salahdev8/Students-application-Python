import tkinter as tk
from tkinter import ttk
import locale
import StudentApp
import LoginWindow



class StudentView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        result = locale.setlocale(locale.LC_ALL, '')



        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')
        self.initComponents(controller)

    def initComponents(self, controller):

        buttonFrame= tk.Frame(self)







        buttonFrame.grid(column=0, row=0)

