from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk 

class Amount():
    def __init__(self, root, dimensions, title):
        self.root = root
        self.root.geometry(dimensions)
        self.root.title(title)

    def main_loop(self):
        self.root.mainloop()

    def add_frames(self, parameter, width, height, bg, x, y):
        if parameter == 'amounts':
            self.add_frame_amounts = Frame(self.root, width = width, height = height)
            self.add_frame_amounts.config(bg = bg)
            self.add_frame_amounts.place(x = x, y = x)

    def add_label_frames(self, text, size_border, width, height, type_word, size_word, relief, bg, x, y):
            self.add_labframe = LabelFrame(self.add_frame_amounts, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.add_labframe.config(text = text, relief = relief, bg = bg) 
            self.add_labframe.place(x = x, y = y)

    def add_entrys(self, parameter, type_enter, width, height, type_word, size_word, x, y):
        if parameter == 'needs':
            self.add_entry_need = Entry(self.add_frame_amounts, textvariable = type_enter)

def main_amount():
    amount = Amount(tk.Tk(), '400x450', 'Amounts')
    amount.add_frames('amounts', 170, 400, 'honeydew', 10, 10 )
    amount.add_label_frames('Needs', 2, 120, 80, 'Arial', 12, 'ridge', 'honeydew', 5, 5)
    amount.add_label_frames('Wants', 2, 120, 80, 'Arial', 12, 'ridge', 'honeydew', 5, 90) 
    amount.add_label_frames('Needs', 2, 120, 80, 'Arial', 12, 'ridge', 'honeydew', 5, 180)  

    amount.main_loop()

if __name__ == '__main__':
    main_amount()