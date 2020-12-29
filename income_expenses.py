from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk 
import time 
import sqlite3

class I_E():
    def __init__(self, root, dimensions, title):
        self.root = root
        self.root.geometry(dimensions)
        self.root.title(title)

    def main_loop(self):
        self.root.mainloop()

    def frame_s(self, parameter,  x, y, bg, width, height):
        if parameter == 'incomes':
            self.frame_in = Label(self.root, width = width, height = height)
            self.frame_in.config(bg = bg)
            self.frame_in.place(x = x, y = y)

        elif parameter == 'expenses':
            self.frame_ex = Label(self.root, width = width, height = height)
            self.frame_ex.config(bg = bg)
            self.frame_ex.place(x = x, y = y)


    def label_frames(self, parameter, size_border, width, height , type_word, size_word, head, relief, bg, x, y):
        if parameter == 'incomes':
            self.lf_in = LabelFrame(self.frame_in, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.lf_in.config(text = head, relief = relief, bg = bg)
            self.lf_in.place(x = x, y = y)

        elif parameter == 'expenses':
            self.lf_ex = LabelFrame(self.frame_ex, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.lf_ex.config(text = head, relief = relief, bg = bg)
            self.lf_ex.place(x = x, y = y)

    def add_label(self, parameter, text, type_word, size_word, x, y):
        if parameter == 'incomes':
            self.add_labels = Label(self.frame_in, text = text)
            self.add_labels.config(font = (type_word, size_word))
            self.add_labels.place(x = x, y = y)
 

def main():
    i_e = I_E(tk.Tk(), '1250x600', 'Incomes and Expenses')
    #INCOMES
    i_e.frame_s('incomes', 5, 10, 'green', 30, 35 )
    i_e.label_frames('incomes', 2, 200, 540, 'Arial', 12, 'INCOMES', 'ridge', 'red', 10, 10)
    i_e.add_label('incomes', 'Monto', 'Arial', 12, 15, 35)
    
    #EXPENSES
    i_e.frame_s('expenses', 295, 10, 'green', 30, 35 )
    i_e.label_frames('expenses', 2, 200, 540, 'Arial', 12, 'EXPENSES', 'ridge', 'blue', 10, 10)

    i_e.main_loop()

if __name__ == '__main__':
    main()