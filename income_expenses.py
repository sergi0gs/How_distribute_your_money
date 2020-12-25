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

        if parameter == 'expenses':
            self.frame_ex = Label(self.root, width = width, height = height)
            self.frame_ex.config(bg = bg)
            self.frame_ex.place(x = x, y = y)

    def label_frames(self, parameter, size_border, width, height , type_word, size_word, head, relief, bg, x, y):
        if parameter == 'incomes':
            self.lf_in = LabelFrame(self.frame_in, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.lf_in.config(text = head, relief = relief, bg = bg)
            self.lf_in.place(x = x, y = y)

        if parameter == 'expenses':
            self.lf_ex = LabelFrame(self.frame_ex, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.lf_ex.config(text = head, relief = relief, bg = bg)
            self.lf_ex.place(x = x, y = y)
        

def main():
    i_e = I_E(tk.Tk(), '1250x600', 'Incomes and Expenses')
    #INCOMES
    i_e.frame_s('incomes', 10, 10, 'blue', 80, 38 )
    i_e.frame_s('incomes', 650, 10, 'red', 80, 38 )
    i_e.label_frames('incomes', 2, 100, 100, 'Arial', 12, 'Incomes', 'ridge')

    i_e.main_loop()

if __name__ == '__main__':
    main()