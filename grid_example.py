# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from lookup_dialog import LookupDialog
class LoginForm(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_ui()

    def make_ui(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=100)

        username_label = ttk.Label(master=self, text="Username is very long label")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(master=self)
        username_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
        username_entry.bind("<F3>", self.lookup)

        password_label = ttk.Label(master=self, text="Password")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(master=self)
        password_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        btn_action = tk.Button(master=self, text="Login", command=self.login)
        btn_action.grid(column=1, row=2, sticky=tk.E, padx=5)

    def login(self):
        print("Logging in")

    def lookup(self, event):
        text = event.widget.get()
        text = LookupDialog(parent=self.winfo_toplevel(), prompt= "Enter something:").show()
        event.widget.insert(0, text)
        print("Looking up {}".format(text))
