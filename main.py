# This is a sample Python script.
from tkinter import *
from browse_employees import BrowseEmployee
from browse_departments import BrowseDepartments
from grid_example import LoginForm
from table_view import TreeView

main_window = Tk()
entry_frame = Frame()
commands_frame = Frame(relief=RAISED, borderwidth=1)

def clear_frame():
    for widget in entry_frame.winfo_children():
        widget.destroy()

def show_employees():
    clear_frame()
    employee_frame = BrowseEmployee(master=entry_frame)
    employee_frame.pack(expand=True, fill="both")

def show_table():
    clear_frame()
    table_frame = TreeView(master=entry_frame)
    table_frame.pack(expand=True, fill="both")

def show_departments():
    clear_frame()
    department_frame = BrowseDepartments(master=entry_frame)
    department_frame.pack(expand=True, fill="both")

def show_login():
    clear_frame()
    login_form = LoginForm(master=entry_frame)
    login_form.pack(expand=True, fill="both")

def main():
    main_window.geometry("600x500")
    btn_employees = Button(master=commands_frame, text="Employees", command=show_employees)
    btn_departments = Button(master=commands_frame, text="Departments", command=show_departments)
    btn_login = Button(master=commands_frame, text="Login", command=show_login)
    btn_table = Button(master=commands_frame, text="Table", command=show_table)
    btn_employees.pack(side=LEFT)
    btn_departments.pack(side=LEFT)
    btn_login.pack(side=LEFT)
    btn_table.pack(side=LEFT)

    entry_frame.pack(fill="both", expand=True)
    employee_frame = BrowseEmployee(master=entry_frame)
    employee_frame.pack(expand=True, fill="both")
    commands_frame.pack(side=BOTTOM, expand=False, fill="both")
    main_window.mainloop()

if __name__ == '__main__':
    main()