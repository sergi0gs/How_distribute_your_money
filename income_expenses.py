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
        elif parameter == 'amounts':
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
            self.add_labels_in = Label(self.frame_in, text = text)
            self.add_labels_in.config(font = (type_word, size_word))
            self.add_labels_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_labels_ex = Label(self.frame_ex, text = text)
            self.add_labels_ex.config(font = (type_word, size_word))
            self.add_labels_ex.place(x = x, y = y)
    
    def add_entry(self, parameter, type_variable, width, type_word, size_word, relief, x, y):
        if parameter == 'date_in':
            self.add_date_in = Entry(self.frame_in, textvariable = type_variable, width = width)
            self.add_date_in.config(font = (type_word,size_word), relief = relief)
            self.add_date_in.place(x = x, y = y)
        elif parameter == 'amount_in':
            self.add_amount_in = Entry(self.frame_in, textvariable = type_variable, width = width)
            self.add_amount_in.config(font = (type_word,size_word), relief = relief)
            self.add_amount_in.place(x = x, y = y)
        if parameter == 'date_ex':
            self.add_date_ex = Entry(self.frame_ex, textvariable = type_variable, width = width)
            self.add_date_ex.config(font = (type_word,size_word), relief = relief)
            self.add_date_ex.place(x = x, y = y)
        elif parameter == 'amount_ex':
            self.add_amount_ex = Entry(self.frame_ex, textvariable = type_variable, width = width)
            self.add_amount_ex.config(font = (type_word,size_word), relief = relief)
            self.add_amount_ex.place(x = x, y = y)

    def add_texts(self, parameter, width, height, x, y):
        if parameter == 'incomes':
            self.add_text_in = Text(self.frame_in, width = width, height = height, relief = 'solid')
            self.add_text_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_text_ex = Text(self.frame_ex, width = width, height = height, relief = 'solid')
            self.add_text_ex.place(x = x, y = y)

    def add_actual_date(self, parameter):
        if parameter == 'incomes':
            self.automatic_date = time.strftime('%d/%m/%y')
            self.add_date_in.insert(0,self.automatic_date)
        elif parameter == 'expenses':
            self.automatic_date = time.strftime('%d/%m/%y')
            self.add_date_ex.insert(0,self.automatic_date)

    def add_button(self, parameter, width, height, text, type_word, size_word, relief, x, y):
        if parameter == 'incomes':
            self.add_buttons_in = Button(self.frame_in, width = width, height = height)
            self.add_buttons_in.config(font = (type_word, size_word), text = text, command = self.add_in, relief = relief)
            self.add_buttons_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_buttons_ex = Button(self.frame_ex, width = width, height = height)
            self.add_buttons_ex.config(font = (type_word, size_word), text = text, command = self.add_ex, relief = relief)
            self.add_buttons_ex.place(x = x, y = y)

    def add_in(self):
        pass

    def add_ex(self):
        pass
    
    def add_combobox(self, width, type_word, size_word, x, y, value1, value2, value3):
        self.combobox_ex = ttk.Combobox(self.frame_ex, width = width, font = (type_word, size_word))
        self.combobox_ex.place(x = x, y = y)
        self.combobox_ex['values'] = (value1, value2, value3)
        self.combobox_ex.config(state = 'readonly')


def main():
    i_e = I_E(tk.Tk(), '1250x600', 'Incomes and Expenses')
    #INCOMES
    i_e.frame_s('incomes', 5, 10, 'honeydew', 30, 40 )
    i_e.label_frames('incomes', 2, 200, 410, 'Arial', 12, 'INCOMES', 'ridge', 'honeydew', 10, 10)
    i_e.add_label('incomes', 'Date: ', 'Arial', 12, 15, 35)
    i_e.add_entry('date_in', tk.StringVar(), 9, 'Arial', 12, 'solid', 15, 60)
    i_e.add_actual_date('incomes')
    i_e.add_label('incomes', 'Amount: ', 'Arial', 12, 15, 90)
    i_e.add_entry('amount_in', tk.StringVar(), 15, 'Arial', 12, 'solid', 15, 115)
    i_e.add_label('incomes', 'Description:  ', 'Arial', 12, 15, 145)
    i_e.add_texts('incomes', 23, 10, 15, 170)
    i_e.add_button('incomes', 10, 2, 'Add', 'Arial', 12, 'groove', 60, 350)

    #EXPENSES
    i_e.frame_s('expenses', 240, 10, 'honeydew', 30, 40)
    i_e.label_frames('expenses', 2, 200, 480, 'Arial', 12, 'EXPENSES', 'ridge', 'honeydew', 10, 10)
    i_e.add_label('expenses', 'Date: ', 'Arial', 12, 15, 35)
    i_e.add_entry('date_ex', tk.StringVar(), 9, 'Arial', 12, 'solid', 15, 60)
    i_e.add_actual_date('expenses')
    i_e.add_label('expenses', 'Amount: ', 'Arial', 12, 15, 90)
    i_e.add_entry('amount_ex', tk.StringVar(), 15, 'Arial', 12, 'solid', 15, 115)
    i_e.add_label('expenses', 'Category:', 'Arial', 12, 15, 145)
    i_e.add_combobox(13, 'Arial', 12, 15, 170, 'Needs', 'Wants', 'Savings')
    i_e.add_label('expenses', 'Description:  ', 'Arial', 12, 15, 200)
    i_e.add_texts('expenses', 23, 10, 15, 225)
    i_e.add_button('expenses', 10, 2, 'Add', 'Arial', 12, 'groove', 60, 400)

########
    i_e.frame_s('amounts', 475, 10, 'red', 30, 40)
    #NEEDS
   # i_e.label_frames('expenses', 2, 200, 480, 'Arial', 12, 'EXPENSES', 'ridge', 'honeydew', 10, 10)
    #WANTS
    #SAVINGS
    i_e.main_loop()

if __name__ == '__main__':
    main()