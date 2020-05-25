from tkinter import *
from tkinter import ttk


def create_dialog(title: str, width: int, height: int, x_offset: int, y_offset: int):
    dialog = Tk()
    dialog.title(title)
    x = dialog.winfo_screenwidth() // 2 - x_offset
    y = dialog.winfo_screenheight() // 2 - y_offset
    dialog.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    return dialog


def create_withdraw_dialog():
    dialog = Tk()
    dialog.withdraw()
    return dialog


def destroy_dialog(dialog: Tk):
    dialog.destroy()


def create_label(dialog: Tk, text: str):
    label = Label(dialog, text=text, font=20)
    label.pack()


def create_button(dialog: Tk, callback: callable):
    btn = Button(dialog, text="Далее", height=2, width=20, command=callback)
    btn.focus_force()
    btn.pack(side=BOTTOM)


def create_combobox(dialog: Tk, selection_reference: StringVar, selection_list: list):
    cmbx = ttk.Combobox(
        dialog,
        textvariable=selection_reference,
        values=selection_list,
        height=len(selection_list),
        state='readonly'
    )
    cmbx.pack()


def wait_dialog_mainloop(dialog: Tk):
    dialog.mainloop()
