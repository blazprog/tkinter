# -*- coding: utf-8 -*-
import tkinter as tk

class BrowseDepartments(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_ui()

    def make_ui(self):
        label_department_name = tk.Label(master=self, text="Department name")
        self.entry_department_name = tk.Entry(master=self)
        label_manager = tk.Label(master=self, text="Department manager")
        self.entry_manager = tk.Entry(master=self)
        btn_action = tk.Button(master=self, text="Show Entries", command=self.make_action)
        btn_action.pack()
        label_department_name.pack()
        self.entry_department_name.pack()
        label_manager.pack()
        self.entry_manager.pack()

    def make_action(self):
        print('Acction from button')
        print("You entered departement {} {}".format(self.entry_department_name.get(), self.entry_manager.get()))
