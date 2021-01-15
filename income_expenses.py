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
            self.automatic_date_in = time.strftime('%d/%m/%y')
            self.add_date_in.insert(0,self.automatic_date_in)
        elif parameter == 'expenses':
            self.automatic_date_ex = time.strftime('%d/%m/%y')
            self.add_date_ex.insert(0,self.automatic_date_ex)

    def add_button(self, parameter, width, height, text, type_word, size_word, relief, x, y):
        if parameter == 'incomes':
            self.add_buttons_in = Button(self.frame_in, width = width, height = height)
            self.add_buttons_in.config(font = (type_word, size_word), text = text, command = self.add_in, relief = relief)
            self.add_buttons_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_buttons_ex = Button(self.frame_ex, width = width, height = height)
            self.add_buttons_ex.config(font = (type_word, size_word), text = text, command = self.add_ex, relief = relief)
            self.add_buttons_ex.place(x = x, y = y)
        elif parameter == 'db':
            self.add_buttons_db = Button(self.frame_in, width = width, height = height)
            self.add_buttons_db.config(font = (type_word, size_word), text = text, command = self.data_base, relief = relief)
            self.add_buttons_db.place(x = x, y = y)

    def add_in(self):
        value_in = True
        for element in self.add_amount_in.get():
            if element == ',':
                value_in = False
                break
            else:
                continue

        if value_in == False:
            messagebox.showinfo('Notification', 'Do not use comma please')
                
        else:
            self.incomes_conection = sqlite3.connect('data_base.db')
            self.incomes_cursor = self.incomes_conection.cursor()
            self.income_data = [
                (
                    self.add_date_in.get(),
                    self.add_amount_in.get(),
                    self.add_text_in.get('1.0','end-1c')
                )
            ]
            self.incomes_cursor.executemany('INSERT INTO INCOMES VALUES(NULL, ?,?,?)', self.income_data)
            self.incomes_conection.commit()
            messagebox.showinfo('Notification','You have saved the information correctly')

    def add_ex(self):
        value_ex = True
        for element in self.add_amount_ex.get():
            if element == ',':
                value_ex = False
                break
            else:
                continue

        if value_ex == False:
            messagebox.showinfo('Notification', 'Do not use comma please')
        
        else:
            self.expenses_conection = sqlite3.connect('data_base.db')
            self.expenses_cursor = self.expenses_conection.cursor()
            self.expenses_data = [
                (
                    self.add_date_ex.get(),
                    self.add_amount_ex.get(),
                    self.combobox_ex.get(),
                    self.add_text_ex.get('1.0','end-1c')
                )
            ]
            self.expenses_cursor.executemany('INSERT INTO EXPENSES VALUES(NULL, ?,?,?,?)', self.expenses_data)
            self.expenses_conection.commit()
            messagebox.showinfo('Notification','You have saved the information correctly')


        
    def data_base(self):
        try:
            self.conection = sqlite3.connect('data_base.db')
            self.cursor = self.conection.cursor()
            self.cursor.execute('''
                CREATE TABLE INCOMES(
                    N INTEGER PRIMARY KEY AUTOINCREMENT,
                    DATE VARCHAR(200),
                    AMOUNT REAL,
                    DESCRIPTION VARCHAR(200)
                )
                '''    
            ),
            self.cursor.execute('''
                CREATE TABLE EXPENSES(
                    N INTEGER PRIMARY KEY AUTOINCREMENT,
                    DATA VARCHAR(200),
                    AMOUNT REAL,
                    CATEGORY VARCHAR(20),
                    DESCRIPTION VARCHAR(200)
                )
                '''
            )
        except:
            messagebox.showinfo('Notification', 'There is already a database created')


    def add_combobox(self, width, type_word, size_word, x, y, value1, value2, value3):
        self.combobox_ex = ttk.Combobox(self.frame_ex, width = width, font = (type_word, size_word))
        self.combobox_ex.place(x = x, y = y)
        self.combobox_ex['values'] = (value1, value2, value3)
        self.combobox_ex.config(state = 'readonly')

    def add_menu(self, width, height):
        self.menu_bar = Menu(self.root)
        self.tabs = Menu(self.menu_bar, tearoff = 0)
        
        self.tabs.add_command(label = 'Data', command = self.data)
        self.tabs.add_separator()
        self.tabs.add_command(label = 'Exit', command = self.exit)
        self.menu_bar.add_cascade(label = 'File', menu = self.tabs)

        self.root.config(menu = self.menu_bar)

    def exit(self):
        self.root.destroy()

    def data(self):
        self.root.destroy()
        from amounts import main_amount
        main_amount()



def main_ie():
    i_e = I_E(tk.Tk(), '470x550', 'Incomes and Expenses')
    i_e.add_menu(300, 300)
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
    i_e.add_button('db', 10, 2, 'Create \nData Base', 'Arial', 12, 'groove', 60, 450)

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

    i_e.main_loop()

if __name__ == '__main__':
    main_ie()