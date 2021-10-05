# -*- coding: utf-8 -*-
import tkinter as tk

class LookupDialog(tk.Toplevel):
    def __init__(self, parent, prompt):
        super().__init__(parent)
        self.parent = parent
        self.var = tk.StringVar()
        self.transient()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.label = tk.Label(self, text=prompt)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x")
        self.ok_button.pack(side="right")

        self.entry.bind("<Return>", self.on_ok)

    def on_ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.protocol("WM_DELETE_WINDOW", self.on_ok) # intercept close button
        self.transient(self.parent)   # dialog window is related to main
        self.wait_visibility() # can't grab until window appears, so we wait
        self.grab_set()        # ensure all input goes to our window
        self.wait_window()
        return self.var.get()
