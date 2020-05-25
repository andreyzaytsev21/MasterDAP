from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from utils.storage.ResourcesManager import ResourcesProvider
from utils.tkinter.DialogUtils import destroy_dialog, create_dialog
from utils.tkinter.JsonToStrVarBind import JsonToStrVarBind


def save_deal(resources_provider: ResourcesProvider, deal_number="", deal_json=None):
    if deal_json is None:
        deal_json = {}

    def close_window():
        dialog.destroy()

    def show_message():
        if deal_number_cont.get() == '' or next((x for x in bindings if x.get_str_var().get() == ''), None) is not None:
            messagebox.showerror("Ошибка", "Заполните все поля")
        else:
            for x in bindings:
                x.update_json()
            resources_provider.put_deal(deal_number_cont.get(), deal_json)
            messagebox.showinfo("Сохранено", "Добавлено/изменено дело об АП\n\n10418000-" + deal_number_cont.get() + "/2020\n")
            destroy_dialog(dialog)

    dialog = create_dialog("Добавить/Изменить ДАП", 510, 580, 255, 300)
    dialog.configure(bg='#bdf0d4')
    deal_number_cont = StringVar(value=deal_number)
    bindings = []

    Label(text='10418000-', bg='#bdf0d4').place(x=10, y=10, height=20)
    entry_number = Entry(textvariable=deal_number_cont)
    entry_number.place(x=70, y=10, width=50, height=20)
    entry_number.focus_force()
    Label(text='/2020', bg='#bdf0d4').place(x=120, y=10, height=20)

    Label(text='дата возбуждения', bg='#bdf0d4').place(x=10, y=40, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "day_init", bindings)).place(x=120, y=40, width=30, height=20)
    dap_config = resources_provider.load_config()

    ttk.Combobox(dialog, textvariable=_make_json_str_bind(deal_json, "month_init", bindings), values=[*dap_config['months']],
                 height=12, state = 'readonly').place(x=160, y=40, width=80, height=20)

    Label(text='2020 года', bg='#bdf0d4').place(x=240, y=40, height=20)

    Label(text='часть', bg='#bdf0d4').place(x=10, y=70, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "code_part", bindings)).place(x=50, y=70, width=30, height=20)
    Label(text='статьи', bg='#bdf0d4').place(x=85, y=70, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "code_art", bindings)).place(x=130, y=70, width=60, height=20)
    Label(text='КоАП РФ', bg='#bdf0d4').place(x=195, y=70, height=20)

    Label(text='юридическое лицо', bg='#bdf0d4').place(x=10, y=100, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.name", bindings)).place(x=130, y=100, width=370, height=20)

    Label(text='ОГРН', bg='#bdf0d4').place(x=10, y=130, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.ogrn", bindings)).place(x=60, y=130, width=150, height=20)

    Label(text='ИНН', bg='#bdf0d4').place(x=10, y=160, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.inn", bindings)).place(x=60, y=160, width=150, height=20)

    Label(text='КПП', bg='#bdf0d4').place(x=10, y=190, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.kpp", bindings)).place(x=60, y=190, width=150, height=20)

    Label(text='дата государственной регистрации ЮЛ', bg='#bdf0d4').place(x=10, y=220, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.date_reg", bindings)).place(x=240, y=220, width=90, height=20)

    Label(text='юридический адрес', bg='#bdf0d4').place(x=10, y=250, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.address.index", bindings)).place(x=130, y=250, width=80, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.address.state", bindings)).place(x=220, y=250, width=280, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.address.city", bindings)).place(x=10, y=280, width=235, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.address.street", bindings)).place(x=255, y=280, width=245, height=20)

    Label(text='законный представитель', bg='#bdf0d4').place(x=10, y=310, height=20)

    ttk.Combobox(dialog, textvariable=_make_json_str_bind(deal_json, "company.representative.position", bindings),
                 values=[*dap_config['actionerPositions']], height=2, state = 'readonly').place(x=160, y=310, width=150, height=20)

    Label(text='инициалы, фамилия', bg='#bdf0d4').place(x=10, y=340, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.representative.name", bindings)).place(x=140, y=340, width=160, height=20)

    Label(text='электронная почта ЮЛ', bg='#bdf0d4').place(x=10, y=370, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "company.email", bindings)).place(x=150, y=370, width=350, height=20)

    Label(text='№ ДТ', bg='#bdf0d4').place(x=10, y=400, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "number_dt", bindings)).place(x=50, y=400, width=200, height=20)

    Label(text='дата протокола об АП', bg='#bdf0d4').place(x=10, y=470, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "day_protokol", bindings)).place(x=140, y=470, width=30, height=20)

    ttk.Combobox(dialog, textvariable=_make_json_str_bind(deal_json, "month_protokol", bindings), values=[*dap_config['months']],
                 height=12, state = 'readonly').place(x=180, y=470, width=80, height=20)

    Label(text='2020 года', bg='#bdf0d4').place(x=260, y=470, height=20)



    Label(text='дата рассмотрения', bg='#bdf0d4').place(x=10, y=500, height=20)
    Entry(textvariable=_make_json_str_bind(deal_json, "day_rassm", bindings)).place(x=140, y=500, width=30, height=20)
    dap_config = resources_provider.load_config()

    ttk.Combobox(dialog, textvariable=_make_json_str_bind(deal_json, "month_rassm", bindings), values=[*dap_config['months']],
                 height=12, state = 'readonly').place(x=180, y=500, width=80, height=20)

    Label(text='2020 года', bg='#bdf0d4').place(x=260, y=500, height=20)

    Button(text="Сохранить", command=show_message).place(relx=.5, rely=.95, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")

    Label(text='« - Alt + 0171, » - Alt + 0187', bg='#bdf0d4').place(x=260, y=130, height=20)

    dialog.focus_force()
    dialog.attributes('-topmost',True)

    dialog.mainloop()


def _make_json_str_bind(json_obj, dict_path, container: list):
    bind = JsonToStrVarBind(json_obj, dict_path)
    container.append(bind)
    return bind.get_str_var()