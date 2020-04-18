import sys
from test import *
from test import Ui_MainWindow
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PyQt5 import QtCore, QtGui, QtWidgets

def okno2():
    if v.get() == '':
        messagebox.showerror("Ошибка", "Пользователь не выбран")
    else:
        tk.destroy()
tk = Tk()
tk.title("Мастер ДАП ver. 1.0.04.20")
w = tk.winfo_screenwidth()
h = tk.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 200
h = h - 100
tk.geometry('400x200+{}+{}'.format(w, h))

label = Label(text='\n Выберите пользователя:\n', font=20)
label.pack()
btn = Button(tk, text="Далее", height=2, width=20, command=okno2)
btn.pack(side=BOTTOM)
v = StringVar()
combobox = ttk.Combobox(tk, textvariable=v, values=(
    "М.В. Дубровина", "Н.В. Задорожная",
    "А.П. Зайцев", "А.Г. Левина",
    "О.А. Петрушева", "Е.Н. Сажина",
    "Э.В. Степанов", "Е.В. Трунина",
    "А.С. Хлыбов", "Е.В. Шумилина",
    "А.В. Яльтиков"), height = 11)
combobox['state'] = 'readonly'
combobox.pack()

tk.mainloop()