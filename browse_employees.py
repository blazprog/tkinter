# -*- coding: utf-8 -*-
import tkinter as tk

class BrowseEmployee(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_ui()

    def make_ui(self):
        label_first_name = tk.Label(master=self, text="First name")
        self.entry_first_name = tk.Entry(master=self)
        label_last_name = tk.Label(master=self, text="Last name")
        self.entry_last_name = tk.Entry(master=self)
        btn_action = tk.Button(master=self, text="Show Entries", command=self.make_action)
        btn_action.pack()
        label_first_name.pack()
        self.entry_first_name.pack()
        label_last_name.pack()
        self.entry_last_name.pack()

    def make_action(self):
        print('Acction from button')
        print("You entered person {} {}".format(self.entry_last_name.get(), self.entry_first_name.get()))
