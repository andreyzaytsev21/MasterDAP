from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from ManageDeals import runManageDeals
from ResourcesProvider import ResourcesProvider

def runEmployeeSelection(resourcesProvider: ResourcesProvider):
    def buttonClickCallback():
        employee = selectedEmployee.get()
        if employee == '':
            messagebox.showerror("Ошибка", "Пользователь не выбран")
        else:
            tk.destroy()
            runManageDeals(resourcesProvider, employee)
    tk = Tk()
    tk.title("МастерДАП")
    w = tk.winfo_screenwidth()
    h = tk.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 200
    h = h - 130
    tk.geometry('400x200+{}+{}'.format(w, h))

    label = Label(text='\n Выберите пользователя:\n', font=20)
    label.pack()
    btn = Button(tk, text="Далее", height=2, width=20, command=buttonClickCallback)
    btn.pack(side=BOTTOM)
    selectedEmployee = StringVar()

    with open(resourcesProvider.getConfigPath(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    listOfEmployee = []
    for l in dapJson['executors'].keys():
        listOfEmployee.append(l)

    combobox = ttk.Combobox(tk, textvariable=selectedEmployee, values= listOfEmployee, height = len(listOfEmployee))
    combobox['state'] = 'readonly'
    combobox.pack()

    tk.mainloop()
    return selectedEmployee.get()