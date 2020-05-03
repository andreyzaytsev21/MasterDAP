from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from ResourcesProvider import ResourcesProvider
from utils.JsonToStrVarBind import JsonToStrVarBind


def save_deal(resources_provider: ResourcesProvider, deal_number="", deal_json=None):
    if deal_json is None:
        deal_json = {}

    def close_window():
        dialog.destroy()

    def show_message():
        # todo
        #  1. x.is_empty()
        #  2. Добавить проверку на то, обязательное поле или нет (is_required)
        if deal_number_cont.get() == '' or next((x for x in bindings if x.get_str_var().get() == ''), None) is not None:
            messagebox.showerror("Ошибка", "Заполните все поля")
        else:
            for x in bindings:
                x.update_json()
            update_deals_storage(resources_provider, deal_number_cont.get(), deal_json)
            messagebox.showinfo("Сохранено",
                                "Добавлено новое дело об АП\n\n10418000-" + deal_number_cont.get() + "/2020\n")
            dialog.destroy()

    dialog = create_dialog()
    deal_number_cont = StringVar(value=deal_number)
    bindings = []

    Label(text='10418000-', bg='#bdf0d4').place(x=10, y=10, height=20)
    Entry(textvariable=deal_number_cont).place(x=70, y=10, width=50, height=20)
    Label(text='/2020', bg='#bdf0d4').place(x=120, y=10, height=20)

    Label(text='дата возбуждения', bg='#bdf0d4').place(x=10, y=40, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "dayInit", bindings)).place(x=120, y=40, width=30, height=20)
    dap_config = resources_provider.load_config()

    monthvozb_ = ttk.Combobox(
        dialog,
        textvariable=make_json_str_bind(deal_json, "monthInit", bindings),
        values=[*dap_config['months']],
        height=12
    )
    monthvozb_['state'] = 'readonly'
    monthvozb_.place(x=160, y=40, width=80, height=20)

    Label(text='2020 года', bg='#bdf0d4').place(x=240, y=40, height=20)

    Label(text='часть', bg='#bdf0d4').place(x=10, y=70, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "partCode", bindings))\
        .place(x=50, y=70, width=30, height=20)
    Label(text='статьи', bg='#bdf0d4').place(x=85, y=70, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "articleCode", bindings))\
        .place(x=130, y=70, width=60, height=20)
    Label(text='КоАП РФ', bg='#bdf0d4').place(x=195, y=70, height=20)

    Label(text='юридическое лицо', bg='#bdf0d4').place(x=10, y=100, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.name", bindings))\
        .place(x=130, y=100, width=370, height=20)

    Label(text='ОГРН', bg='#bdf0d4').place(x=10, y=130, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.ogrn", bindings))\
        .place(x=60, y=130, width=150, height=20)

    Label(text='ИНН', bg='#bdf0d4').place(x=10, y=160, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.inn", bindings))\
        .place(x=60, y=160, width=150, height=20)

    Label(text='КПП', bg='#bdf0d4').place(x=10, y=190, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.kpp", bindings))\
        .place(x=60, y=190, width=150, height=20)

    Label(text='дата государственной регистрации ЮЛ', bg='#bdf0d4').place(x=10, y=220, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.registrationDate", bindings))\
        .place(x=240, y=220, width=90, height=20)

    Label(text='юридический адрес', bg='#bdf0d4').place(x=10, y=250, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.address.index", bindings))\
        .place(x=130, y=250, width=80, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.address.state", bindings))\
        .place(x=220, y=250, width=280, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.address.city", bindings))\
        .place(x=10, y=280, width=235, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.address.street", bindings))\
        .place(x=255, y=280, width=245, height=20)

    Label(text='законный представитель', bg='#bdf0d4').place(x=10, y=310, height=20)
    zpPosition_ = ttk.Combobox(
        dialog,
        textvariable=make_json_str_bind(deal_json, "company.representative.position", bindings),
        values=[*dap_config['actionerPositions']],
        height=2
    )
    zpPosition_['state'] = 'readonly'
    zpPosition_.place(x=160, y=310, width=150, height=20)

    Label(text='инициалы, фамилия', bg='#bdf0d4').place(x=10, y=340, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.representative.name", bindings))\
        .place(x=140, y=340, width=160, height=20)

    Label(text='электронная почта ЮЛ', bg='#bdf0d4').place(x=10, y=370, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "company.email", bindings))\
        .place(x=150, y=370, width=350, height=20)

    Label(text='№ ДТ', bg='#bdf0d4').place(x=10, y=400, height=20)
    Entry(textvariable=make_json_str_bind(deal_json, "numberDt", bindings))\
        .place(x=50, y=400, width=200, height=20)

    Radiobutton(text="таможенный представитель", value=1,
                variable=make_json_str_bind(deal_json, "customsRepresentative", bindings), bg='#bdf0d4',
                activebackground='#bdf0d4').place(x=10, y=430, height=20)
    Radiobutton(text="декларант", value=2,
                variable=make_json_str_bind(deal_json, "customsRepresentative", bindings), bg='#bdf0d4',
                activebackground='#bdf0d4').place(x=200, y=430, height=20)

    Button(text="Сохранить", command=show_message).place(relx=.5, rely=.95, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")

    dialog.mainloop()


def create_dialog():
    dialog = Tk()
    dialog.title("Добавить/Изменить ДАП")
    w = dialog.winfo_screenwidth()
    h = dialog.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 255
    h = h - 300
    dialog.geometry('510x510+{}+{}'.format(w, h))
    dialog.configure(bg='#bdf0d4')
    return dialog


def update_deals_storage(resources_provider: ResourcesProvider, deal_number: str, deal_json):
    file_pointer = open(resources_provider.get_deals_path(), 'r', encoding='utf-8')
    existing_deals = json.load(file_pointer)
    file_pointer.close()
    existing_deals[deal_number] = deal_json
    file_pointer = open(resources_provider.get_deals_path(), 'w', encoding='utf-8')
    file_pointer.write(str(json.dumps(existing_deals, ensure_ascii=False, sort_keys=True, indent=4)))
    file_pointer.close()


def make_json_str_bind(json_obj, dict_path, container: list):
    bind = JsonToStrVarBind(json_obj, dict_path)
    container.append(bind)
    return bind.get_str_var()
