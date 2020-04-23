from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from docxtpl import DocxTemplate
import json
from ResourcesProvider import ResourcesProvider

def runCreateDocs(resourcesProvider: ResourcesProvider, chosenDeal: str):

    def formDocs():
        if box_01.get():
            doc = DocxTemplate("../templates/01.docx")
            context = {'number': number}
            doc.render(context)
            doc.save("../buffer/" + number + "__ 2.1 РЕШЕНИЕ о передаче дела для проведения АР.docx")

        if box_11.get():
            print('1')
            doc = DocxTemplate("../templates/11.docx")
            context = {'number': number}
            doc.render(context)
            doc.save("../buffer/" + number + "__ 3.2 Cправка об издержках.docx")

        messagebox.showinfo("Сформировано по делу об АП\n\n10418000-" + number + "/2020")

    def close_window():
        winChooseDocs.destroy()

    winChooseDocs = Tk()
    winChooseDocs.title("Выбор документов для ДАП 10418000-" + chosenDeal + "/2020")
    w = winChooseDocs.winfo_screenwidth()
    h = winChooseDocs.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 270
    h = h - 345
    winChooseDocs.geometry('540x620+{}+{}'.format(w, h))

    box_01 = BooleanVar()
    box_02 = BooleanVar()
    box_03 = BooleanVar()
    box_04 = BooleanVar()
    box_05 = BooleanVar()
    box_06 = BooleanVar()
    box_07 = BooleanVar()
    box_08 = BooleanVar()
    box_09 = BooleanVar()
    box_10 = BooleanVar()
    box_11 = BooleanVar()
    box_12 = BooleanVar()
    box_13 = BooleanVar()
    box_14 = BooleanVar()
    box_15 = BooleanVar()
    box_16 = BooleanVar()
    box_17 = BooleanVar()
    box_18 = BooleanVar()
    box_19 = BooleanVar()

    znt1 = StringVar()
    znt2 = StringVar()
    znt3 = StringVar()
    znt4 = StringVar()
    dateper = StringVar()
    monthper = StringVar()
    datepovestka = StringVar()
    monthpovestka = StringVar()
    datezapros = StringVar()
    monthzapros = StringVar()
    dateprotokol = StringVar()
    monthprotokol = StringVar()
    daterassm = StringVar()
    monthrassm = StringVar()
    daterassm2 = StringVar()
    monthrassm2 = StringVar()

    Checkbutton(text="Решение о передаче ДАП", variable=box_01).place(x=10, y=10, height = 20)
    Checkbutton(text="Определение о принятии дела к своему производству", variable=box_02).place(x=200, y=10, height = 20)

    with open(resourcesProvider.getConfigPath(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    listOfPer = []
    for l in dapJson['signers'].keys():
        listOfPer.append(l)
    znt1_ = ttk.Combobox(winChooseDocs, textvariable=znt1, values = listOfPer, height = 2)
    znt1_['state']='readonly'
    znt1_.place(x = 30, y = 35, width=110, height = 20)

    Label(text='дата передачи ДАП').place(x=220, y=35, height = 20)
    Entry(textvariable=dateper).place(x=340, y=35, width=30, height = 20)

    listOfMonths = []
    for l in dapJson['months'].keys():
        listOfMonths.append(l)
    monthper_ = ttk.Combobox(winChooseDocs, textvariable=monthper, values = listOfMonths, height = 12)
    monthper_['state']='readonly'
    monthper_.place(x = 380, y = 35, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=35, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=55, height = 20)

    Checkbutton(text="Определение об истребовании документов и сведений", variable=box_03).place(x=10, y=80, height = 20)
    Checkbutton(text="Повестка о явке", variable=box_04).place(x=410, y=80, height = 20)

    Label(text='дата направления').place(x=220, y=105, height = 20)
    Entry(textvariable=datepovestka).place(x=340, y=105, width=30, height = 20)

    monthpovestka_ = ttk.Combobox(winChooseDocs, textvariable=monthpovestka, values = listOfMonths, height = 12)
    monthpovestka_['state']='readonly'
    monthpovestka_.place(x = 380, y = 105, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=105, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=125, height = 20)

    Checkbutton(text="Запрос в ГИБДД", variable=box_05).place(x=10, y=150, height = 20)
    Checkbutton(text="Запрос в Росреестр с приложением", variable=box_06).place(x=300, y=150, height = 20)

    znt2_ = ttk.Combobox(winChooseDocs, textvariable=znt2, values = listOfPer, height = 2)
    znt2_['state']='readonly'
    znt2_.place(x = 30, y = 175, width=110, height = 20)

    Label(text='дата направления').place(x=220, y=175, height = 20)
    Entry(textvariable=datezapros).place(x=340, y=175, width=30, height = 20)

    monthzapros_ = ttk.Combobox(winChooseDocs, textvariable=monthzapros, values = listOfMonths, height = 12)
    monthzapros_['state']='readonly'
    monthzapros_.place(x = 380, y = 175, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=175, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=195, height = 20)

    Checkbutton(text="Шаблон ТЛГ вызов на протокол", variable=box_07).place(x=10, y=220, height = 20)
    Checkbutton(text="Шаблон ответа ЮЛ на вызов на протокол", variable=box_08).place(x=270, y=220, height = 20)
    Checkbutton(text="Шаблон протокола об АП", variable=box_09).place(x=10, y=240, height = 20)

    Label(text='дата протокола об АП').place(x=200, y=265, height = 20)
    Entry(textvariable=dateprotokol).place(x=340, y=265, width=30, height = 20)

    monthprotokol_ = ttk.Combobox(winChooseDocs, textvariable=monthprotokol, values = listOfMonths, height = 12)
    monthprotokol_['state']='readonly'
    monthprotokol_.place(x = 380, y = 265, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=265, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=285, height = 20)

    Checkbutton(text="Рапорт об окончании адм.расследования", variable=box_10).place(x=10, y=310, height = 20)
    Checkbutton(text="Справка об отсутствии издержек", variable=box_11).place(x=320, y=310, height = 20)
    Checkbutton(text="Определение о назначении времени и места рассмотрения ДАП", variable=box_12).place(x=10, y=330, height = 20)
    Checkbutton(text="Шаблон ТЛГ вызов на рассмотрение", variable=box_13).place(x=10, y=350, height = 20)
    Checkbutton(text="Шаблон ответа ЮЛ на вызов на рассмотрение", variable=box_14).place(x=245, y=350, height = 20)

    znt3_ = ttk.Combobox(winChooseDocs, textvariable=znt3, values = listOfPer, height = 2)
    znt3_['state']='readonly'
    znt3_.place(x = 30, y = 375, width=110, height = 20)

    Label(text='дата передачи ДАП').place(x=220, y=375, height = 20)
    Entry(textvariable=daterassm).place(x=340, y=375, width=30, height = 20)

    monthrassm_ = ttk.Combobox(winChooseDocs, textvariable=monthrassm, values = listOfMonths, height = 12)
    monthrassm_['state']='readonly'
    monthrassm_.place(x = 380, y = 375, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=375, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=395, height = 20)

    Checkbutton(text="Определение об отложении времени и места рассмотрения ДАП", variable=box_15).place(x=30, y=420, height = 20)
    Checkbutton(text="Определение о продлении срока рассмотрения ДАП", variable=box_16).place(x=30, y=440, height = 20)
    Checkbutton(text="Шаблон постановления по ДАП", variable=box_17).place(x=10, y=460, height = 20)
    Checkbutton(text="Представление об устранении причин и условий", variable=box_18).place(x=10, y=480, height = 20)

    znt4_ = ttk.Combobox(winChooseDocs, textvariable=znt4, values = listOfPer, height = 2)
    znt4_['state']='readonly'
    znt4_.place(x = 30, y = 505, width=110, height = 20)

    Label(text='дата рассмотрения').place(x=220, y=505, height = 20)
    Entry(textvariable=daterassm2).place(x=340, y=505, width=30, height = 20)

    monthrassm2_ = ttk.Combobox(winChooseDocs, textvariable=monthrassm2, values = listOfMonths, height = 12)
    monthrassm2_['state']='readonly'
    monthrassm2_.place(x = 380, y = 505, width=80, height = 20)
    Label(text='2020 года').place(x=465, y= 505, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=525, height = 20)

    Checkbutton(text="Бирка ДАП", variable=box_19).place(x=10, y=550, height = 20)

    Button(text="Сформировать", command=formDocs).place(relx=.5, rely=.95, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")

    number = chosenDeal
    '''[number]['company']['address']['ad_index']
    [number]['chkoap']
    [number]['datevozb']
    [number]['monthvozb']
    [number]['company']['dateul']
    [number]['company']['emailul']
    ['company']['actioner']['position']
    ['company']['actioner']['name']
    ['dd1']
    ['dd2']
    ['dd4']
    ['dd5']
    ['fio1_1']
    ['fio1']
    ['fio2']
    ['fio2']
    ['fio3_1']
    ['fio3']
    ['fio3']
    ['fio3']
    [number]['company']['inn']
    [number]['company']['kpp']
    ['month1']
    ['month2']
    ['month4']
    ['month5']
    [number]['company']['address']['naspunkt']
    ['number']
    [number]['company']['ogrn']
    [number]['stkoap']
    [number]['company']['address']['subrf']
    [number]['company']['ul']
    [number]['company']['address']['ulitsadom']
    ['znt1']
    ['znt2']
    ['znt3_1']
    ['znt3']
    ['doloar']
    ['doloar_vp']
    ['fiooar']
    ['fiooar_vp']'''


    winChooseDocs.mainloop()