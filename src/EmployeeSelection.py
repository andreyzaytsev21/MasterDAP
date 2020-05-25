from tkinter import StringVar

import sys

from utils.storage.ResourcesManager import ResourcesProvider
from utils.tkinter.DialogUtils import create_dialog, create_label, create_button, wait_dialog_mainloop, create_combobox, \
    destroy_dialog
from utils.tkinter.MessageBoxUtils import show_error


def run_employee_selection(resources_provider: ResourcesProvider):
    dialog = create_dialog("МастерДАП", 400, 200, 200, 130)

    selected_employee_reference = StringVar()

    create_label(dialog, '\n Выберите пользователя:\n')

    def button_click_callback():
        if not selected_employee_reference.get():
            show_error("Ошибка", "Пользователь не выбран")
        else:
            destroy_dialog(dialog)

    create_button(dialog, button_click_callback)

    list_of_employees = load_employees(resources_provider)
    create_combobox(dialog, selected_employee_reference, list_of_employees)

    wait_dialog_mainloop(dialog)

    if not selected_employee_reference.get():
        sys.exit()

    return selected_employee_reference.get()


def load_employees(resources_provider: ResourcesProvider):
    return [*resources_provider.load_config()['employeesOar']]
