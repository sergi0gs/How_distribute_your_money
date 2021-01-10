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
            self.add_frame_amounts.place(x = x, y = y)
        if parameter == 'tables':
            self.add_frame_tables = Frame(self.root, width = width, height = height)
            self.add_frame_tables.config(bg = bg)
            self.add_frame_tables.place(x = x, y = y)
        if parameter == 'search':
            self.add_frame_search = Frame(self.root, width = width, height = height)
            self.add_frame_search.config(bg = bg)
            self.add_frame_search.place(x = x, y = y)

    def add_labels(self, parameter, text, type_word, size_word, x, y):
        if parameter == 'tables':
            self.add_label_in = Label(self.add_frame_tables, text = text)
            self.add_label_in.config(font = (type_word, size_word))
            self.add_label_in.place(x = x, y = y)
        elif parameter == 'search':
            self.add_label_in = Label(self.add_frame_search, text = text)
            self.add_label_in.config(font = (type_word, size_word))
            self.add_label_in.place(x = x, y = y)

    def add_label_frames(self, text, size_border, width, height, type_word, size_word, relief, bg, x, y):
            self.add_labframe = LabelFrame(self.add_frame_amounts, bd = size_border, width = width, height = height, font = (type_word, size_word))
            self.add_labframe.config(text = text, relief = relief, bg = bg) 
            self.add_labframe.place(x = x, y = y)

    def add_entrys(self, parameter, type_enter, width, type_word, size_word, x, y):
        if parameter == 'needs':
            self.add_entry_need = Entry(self.add_frame_amounts, textvariable = type_enter, width = width)
            self.add_entry_need.config(font = (type_word, size_word), relief = 'solid')
            self.add_entry_need.place(x = x, y = y)
        elif parameter == 'wants':
            self.add_entry_wants = Entry(self.add_frame_amounts, textvariable = type_enter, width = width)
            self.add_entry_wants.config(font = (type_word, size_word), relief = 'solid')
            self.add_entry_wants.place(x = x, y = y)
        elif parameter == 'savings':
            self.add_entry_savings = Entry(self.add_frame_amounts, textvariable = type_enter, width = width)
            self.add_entry_savings.config(font = (type_word, size_word), relief = 'solid')
            self.add_entry_savings.place(x = x, y = y)
        elif parameter == 'incomes':
            self.add_entry_in = Entry(self.add_frame_search, textvariable = type_enter, width = width)
            self.add_entry_in.config(font = (type_word, size_word), relief = 'solid')
            self.add_entry_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_entry_ex = Entry(self.add_frame_search, textvariable = type_enter, width = width)
            self.add_entry_ex.config(font = (type_word, size_word), relief = 'solid')
            self.add_entry_ex.place(x = x, y = y)

    def add_button(self, parameter,  width, height, text, type_word, size_word, relief, x, y):
        if parameter == 'amount':
            self.add_buttons_amount = Button(self.add_frame_amounts, width = width, height = height)
            self.add_buttons_amount.config(font = (type_word, size_word), text = text, command = self.show_data, relief = relief)
            self.add_buttons_amount.place(x = x, y = y)
        if parameter == 'incomes':
            self.add_buttons_in = Button(self.add_frame_search, width = width, height = height)
            self.add_buttons_in.config(font = (type_word, size_word), text = text, command = self.show_incomes, relief = relief)
            self.add_buttons_in.place(x = x, y = y)
        if parameter == 'expenses':
            self.add_buttons_ex = Button(self.add_frame_search, width = width, height = height)
            self.add_buttons_ex.config(font = (type_word, size_word), text = text, command = self.show_expenses, relief = relief)
            self.add_buttons_ex.place(x = x, y = y)

    def show_data(self):
        messagebox.showinfo('','hola')

    def show_incomes(self):
        messagebox.showinfo('','in')

    def show_expenses(self):
        messagebox.showinfo('', 'ex')

    def add_tables(self, parameter, x, y):
        if parameter == 'incomes':
            self.add_table_in = ttk.Treeview(self.add_frame_tables, selectmode = 'browse')
            self.add_table_in.place (x = x, y = y)
            self.add_table_in['columns'] = ('1','2','3','4')
            self.add_table_in['show'] = 'headings'
            self.add_table_in.column ('1', width = 40, anchor = 'c')
            self.add_table_in.column ('2', width = 80, anchor = 'c')
            self.add_table_in.column ('3', width = 120, anchor = 'c')
            self.add_table_in.column ('4', width = 120, anchor = 'c')

            self.add_table_in.heading ('1', text = 'N°')
            self.add_table_in.heading ('2', text = 'Date')
            self.add_table_in.heading ('3', text = 'Amount')
            self.add_table_in.heading ('4', text = 'Description')
            self.scroll_bar_in = ttk.Scrollbar (self.add_frame_tables, orient = 'vertical', command = self.add_table_in.yview)
            self.scroll_bar_in.place (x = x+370, y= y+90)

        elif parameter == 'expenses':
            self.add_table_ex = ttk.Treeview(self.add_frame_tables, selectmode = 'browse')
            self.add_table_ex.place (x = x, y = y)
            self.add_table_ex['columns'] = ('1','2','3','4','5')
            self.add_table_ex['show'] = 'headings'
            self.add_table_ex.column ('1', width = 40, anchor = 'c')
            self.add_table_ex.column ('2', width = 120, anchor = 'c')
            self.add_table_ex.column ('3', width = 80, anchor = 'c')
            self.add_table_ex.column ('4', width = 120, anchor = 'c')
            self.add_table_ex.column ('5', width = 120, anchor = 'c')

            self.add_table_ex.heading ('1', text = 'N°')
            self.add_table_ex.heading ('2', text = 'Date')
            self.add_table_ex.heading ('3', text = 'Amount')
            self.add_table_ex.heading ('4', text = 'Category')
            self.add_table_ex.heading ('5', text = 'Description')
            self.scroll_bar_ex = ttk.Scrollbar (self.add_frame_tables, orient = 'vertical', command = self.add_table_ex.yview)
            self.scroll_bar_ex.place (x = x+490, y= y+90)

    def add_text_box(self, parameter, width, height, type_word, size_word, x, y):
        if parameter == 'incomes':
            self.add_box_in = Text(self.add_frame_search, width = width, height = height, relief = 'solid')
            self.add_box_in.config(font = (type_word, size_word))
            self.add_box_in.place(x = x, y = y)
        elif parameter == 'expenses':
            self.add_box_in = Text(self.add_frame_search, width = width, height = height, relief = 'solid')
            self.add_box_in.config(font = (type_word, size_word))
            self.add_box_in.place(x = x, y = y)

    def add_menu(self, width, height):
        self.menu_bar = Menu(self.root)
        self.tabs = Menu(self.menu_bar, tearoff = 0)
        
        self.tabs.add_command(label = 'Add', command = self.add)
        self.tabs.add_separator()
        self.tabs.add_command(label = 'Exit', command = self.exit)
        self.menu_bar.add_cascade(label = 'File', menu = self.tabs)

        self.root.config(menu = self.menu_bar)

    def exit(self):
        self.root.destroy()

    def add(self):
        self.root.destroy()
        from income_expenses import main_ie
        main_ie()

def main_amount():
    amount = Amount(tk.Tk(), '1200x400', 'Amounts')
    amount.add_frames('amounts', 170, 400, 'honeydew', 10, 10)
    amount.add_frames('tables', 950, 280, 'honeydew', 150, 10)
    amount.add_frames('search', 950, 100, 'honeydew', 150, 290)

    amount.add_menu(300, 300)

    amount.add_label_frames('Needs', 2, 100, 70, 'Arial', 11, 'ridge', 'honeydew', 5, 10)
    amount.add_entrys('needs', tk.StringVar, 9, 'Arial', 11, 18, 40)
    
    amount.add_label_frames('Wants', 2, 100, 70, 'Arial', 11, 'ridge', 'honeydew', 5, 95) 
    amount.add_entrys('wants', tk.StringVar, 9, 'Arial', 11, 18, 125)
    
    amount.add_label_frames('Savings', 2, 100, 70, 'Arial', 11, 'ridge', 'honeydew', 5, 185) 
    amount.add_entrys('savings', tk.StringVar, 9, 'Arial', 11, 18, 215) 

    amount.add_button('amount', 8, 2, 'Show', 'Arial', 12, 'groove', 15, 285)

    amount.add_labels('tables', 'Income\'s history', 'Arial', 12, 120, 10)
    amount.add_tables('incomes', 10, 30)
    amount.add_labels('tables','Expenses\'s history', 'Arial', 12, 590, 10)
    amount.add_tables('expenses', 430, 30)

    amount.add_labels('search', 'N°:', 'Arial', 12, 10, 10)
    amount.add_entrys('incomes', tk.StringVar, 5, 'Arial', 11, 40, 12) 
    amount.add_button('incomes', 8, 2, 'Search', 'Arial', 12, 'groove', 10, 40)
    amount.add_text_box('incomes', 30, 4,'Arial', 12, 100, 10)

    amount.add_labels('search', 'N°:', 'Arial', 12, 500, 10)
    amount.add_entrys('expenses', tk.StringVar, 5, 'Arial', 11, 530, 12) 
    amount.add_button('expenses', 8, 2, 'Search', 'Arial', 12, 'groove', 500, 40)
    amount.add_text_box('expenses', 30, 4, 'Arial', 12, 600, 10)


    amount.main_loop()

if __name__ == '__main__':
    main_amount()