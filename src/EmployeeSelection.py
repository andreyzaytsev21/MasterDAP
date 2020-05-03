import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from ResourcesProvider import ResourcesProvider


def run_employee_selection(resources_provider: ResourcesProvider):
    dialog = create_dialog("МастерДАП")

    selected_employee_reference = StringVar()

    create_label(dialog)
    create_button(selected_employee_reference, dialog)

    list_of_employees = load_employees(resources_provider)
    create_combobox(selected_employee_reference, list_of_employees, dialog)

    dialog.mainloop()

    if not selected_employee_reference.get():
        sys.exit()

    return selected_employee_reference.get()


def create_dialog(title: str):
    dialog = Tk()
    dialog.title(title)
    w = dialog.winfo_screenwidth()
    h = dialog.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 200
    h = h - 130
    dialog.geometry('400x200+{}+{}'.format(w, h))

    return dialog


def create_label(dialog: Tk):
    label = Label(dialog, text='\n Выберите пользователя:\n', font=20)
    label.pack()


def create_combobox(selected_employee_reference: StringVar, list_of_employees: list, dialog: Tk):
    combobox = ttk.Combobox(dialog,
                            textvariable=selected_employee_reference,
                            values=list_of_employees,
                            height=len(list_of_employees))
    combobox['state'] = 'readonly'
    combobox.pack()


def create_button(selected_employee_reference: StringVar, dialog: Tk):
    def button_click_callback():
        if not selected_employee_reference.get():
            messagebox.showerror("Ошибка", "Пользователь не выбран")
        else:
            dialog.destroy()

    btn = Button(dialog, text="Далее", height=2, width=20, command=button_click_callback)
    btn.pack(side=BOTTOM)


def load_employees(resources_provider: ResourcesProvider):
    return [*resources_provider.load_config()['employeesOar']]
