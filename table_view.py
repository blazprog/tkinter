# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

class TreeView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_ui()


    def item_selected(self, event):
        for selected_item in self.tree_view.selection():
            # dictionary
            item = self.tree_view.item(selected_item)
            print(item['values'])
            self.entry_name.delete(0, 'end')
            self.entry_name.insert(0,item["values"][1])
            self.entry_score.delete(0, 'end')
            self.entry_score.insert(0,item["values"][2])

    def show(self):
        tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (name, score) in enumerate(tempList, start=1):
            self.tree_view.insert("", "end", values=(i, name, score))

    def open(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )
        file_name = filedialog.askopenfilename(
            title="Open a file",
            filetypes=filetypes
        )
        if file_name:
            print(file_name)
            i = 1
            for line in open(file_name):
                print(line)
                record = line.split("|")
                self.tree_view.insert("", "end", values=(i, record[0], record[1]))
                i+=1


    def make_ui(self):
        label_title = ttk.Label(master=self, text="Table View",
                                font=("Arial", 30))
        frame_center = tk.Frame(master=self)
        cols = ("Position", "Name", "Score")
        self.tree_view = ttk.Treeview(master=frame_center,
                                 columns=cols,
                                 show="headings")
        self.tree_view.column("Position", stretch=tk.NO, width=100, anchor=tk.CENTER)
        for col in cols:
            self.tree_view.heading(col, text=col)
        label_title.pack(side=tk.TOP, fill="both", anchor=tk.CENTER)
        self.tree_view.pack(side=tk.LEFT, anchor=tk.N)
        frame_data_entry = tk.Frame(master=frame_center)
        lbl_entry = tk.Label(master=frame_data_entry, text="Name")
        self.entry_name = tk.Entry(master=frame_data_entry)
        lbl_score = tk.Label(master=frame_data_entry, text="Score")
        self.entry_score = tk.Entry(master=frame_data_entry)
        lbl_entry.pack()
        self.entry_name.pack()
        lbl_score.pack()
        self.entry_score.pack()
        frame_data_entry.pack(side=tk.LEFT, anchor=tk.N)
        frame_center.pack(expand=True, fill="both")
        btn_show = ttk.Button(master=self, text="Show", command=self.show)
        btn_show.pack(side=tk.BOTTOM)
        btn_open = ttk.Button(master=self, text="Open", command=self.open)
        btn_open.pack(side=tk.BOTTOM)

        # bind events
        self.tree_view.bind('<<TreeviewSelect>>', self.item_selected)
