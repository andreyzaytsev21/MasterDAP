from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from files.ManageDeals import runManageDeals

def runEmployeeSelection():
    def okno2():
        employee = v.get()
        if employee == '':
            messagebox.showerror("Ошибка", "Пользователь не выбран")
        else:
            tk.destroy()

            #runManageDeals()
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

    with open('dap.json', 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    listOfEmployee = []
    for l in dapJson['executors'].keys():
        listOfEmployee.append(l)


    combobox = ttk.Combobox(tk, textvariable=v, values= listOfEmployee, height = 11)
    combobox['state'] = 'readonly'
    combobox.pack()


    tk.mainloop()