from tkinter import messagebox

def show_error(title: str, message: str):
    messagebox.showerror(title, message)

def show_confirm(message: str):
     return messagebox.askyesno(message=message)

def show_info(title: str, message: str):
    messagebox.showinfo(title, message)