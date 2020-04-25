from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from docxtpl import DocxTemplate
import json
from ResourcesProvider import ResourcesProvider

def runCreateDocs(resourcesProvider: ResourcesProvider, chosenDeal: str, chosenEmployeeOar: str):
    print(chosenEmployeeOar)



    def formDocs():
        if box_01.get() == False and box_02.get() == False and box_03.get() == False and box_04.get() == False and \
                        box_05.get() == False and box_06.get() == False and box_07.get() == False and box_08.get() == False and \
                        box_09.get() == False and box_10.get() == False and box_11.get() == False and box_12.get() == False and \
                        box_13.get() == False and box_14.get() == False and box_15.get() == False and box_16.get() == False and \
                        box_17.get() == False and box_18.get() == False and box_19.get() == False:
            messagebox.showerror("Ошибка", "Выберите документы")
        else:
            #zntToAR = dapJson['signers'][zntToARName.get()]['znt_ip']
            #zntZapros = dapJson['signers'][zntZaprosName.get()]['znt_ip']
            #zntToRassm = dapJson['signers'][zntToRassmName.get()]['znt_ip']
            context = {"artCode" : artCode, "dateInit" : dateInit, "dateRegUl" : dateRegUl, "emailUl" : emailUl,
                       "inn" : inn, "kpp" : kpp, "monthInit" : monthInit, "numberCase": numberCase, "numberDt" : numberDt,
                       "ogrn" : ogrn, "partCode" : partCode, "tpdecl" : tpdecl, "ul" : ul, "ulCity": ulCity,
                       "ulIndex" : ulIndex, "ulStreetOffice": ulStreetOffice, "ulSubrf": ulSubrf, "zpName_dp" : zpName_dp,
                       "zpName_ip" : zpName_ip, "zpName_rp" : zpName_rp, "zpName_tp" : zpName_tp, "zpName_vp" : zpName_vp,
                       "zpPosition" : zpPosition, "zpPosition_ip" : zpPosition_ip, "zpPosition_rp" : zpPosition_rp,
                       "zpPosition_dp" : zpPosition_dp, "zpPosition_vp" : zpPosition_vp, "zpPosition_tp" : zpPosition_tp,
                       "zpPosition_ip_low" : zpPosition_ip_low, "zpPosition_rp_low" : zpPosition_rp_low,
                       "zpPosition_dp_low" : zpPosition_dp_low, "zpPosition_vp_low" : zpPosition_vp_low,
                       "zpPosition_tp_low" : zpPosition_tp_low, "fiooar_ip" : fiooar_ip, "fiooar_rp" : fiooar_rp,
                       "fiooar_dp" : fiooar_dp, "fiooar_vp" : fiooar_vp, "fiooar_tp" : fiooar_tp, "doloar_ip" : doloar_ip,
                       "doloar_rp" : doloar_rp, "doloar_dp" : doloar_dp, "doloar_vp" : doloar_vp, "doloar_tp" : doloar_tp,
                       "doloar_ip_low" : doloar_ip_low, "doloar_rp_low" : doloar_rp_low, "doloar_dp_low" : doloar_dp_low,
                       "doloar_vp_low" : doloar_vp_low, "doloar_tp_low" : doloar_tp_low, "doloar_ip_sh" : doloar_ip_sh,
                       "doloar_rp_sh" : doloar_rp_sh, "doloar_dp_sh" : doloar_dp_sh, "doloar_vp_sh" : doloar_vp_sh,
                       "doloar_tp_sh" : doloar_tp_sh, "doloar_ip_sh_low" : doloar_ip_sh_low, "doloar_rp_sh_low" : doloar_rp_sh_low,
                       "doloar_dp_sh_low" : doloar_dp_sh_low, "doloar_vp_sh_low" : doloar_vp_sh_low,
                       "doloar_tp_sh_low" : doloar_tp_sh_low, "emailOar" : emailOar, "gortel" : gortel
                       }
                       #"zntToAR" : zntToAR, "zntToARName" : zntToARName.get(), "dateToAR" : dateToAR.get(), "monthToAR" : monthToAR.get(),
                       #"zntZapros" : zntZapros, "zntZaprosName" : zntZaprosName.get(), "dateZapros" : dateZapros.get(),
                       #"monthZapros" : monthZapros.get(), "dateProtokol" : dateProtokol.get(), "monthProtokol" : monthProtokol.get(),
                       #"zntToRassm" : zntToRassm, "zntToRassmName" : zntToRassmName.get(), "dateToRassm" : dateToRassm.get(),
                       #"monthToRassm" : monthToRassm.get(), "zntPost" : zntPostName, "zntPostName" : zntPostName.get(),
                       #"datePost" : datePost.get(), "monthPost" : monthPost.get()
                       #}
            # ГОТОВ
            if box_01.get():
                zntToAR_ip = dapJson['signers'][zntToARName.get()]['znt_ip']
                doc = DocxTemplate("../templates/01.docx")
                context.update({"zntToAR_ip" : zntToAR_ip, "zntToARName_ip" : zntToARName.get(), "dateToAR" : dateToAR.get(),
                                "monthToAR" : monthToAR.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 2.1 РЕШЕНИЕ о передаче дела для проведения АР.docx")
            # ГОТОВ
            if box_02.get():
                zntToAR_rp_low = dapJson['signers'][zntToARName.get()]['znt_rp_low']
                zntToARName_rp = dapJson['signers'][zntToARName.get()]['rp']
                doc = DocxTemplate("../templates/02.docx")
                context.update({"zntToAR_rp_low" : zntToAR_rp_low, "zntToARName_rp" : zntToARName_rp, "dateToAR" : dateToAR.get(),
                                "monthToAR" : monthToAR.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 2.2 ОПРЕДЕЛЕНИЕ о принятии дела к своему проиводству.docx")
            # ГОТОВ
            if box_11.get():
                zntToRassm = dapJson['signers'][zntToRassmName.get()]['znt_ip']
                doc = DocxTemplate("../templates/11.docx")
                context.update({"zntToRassm" : zntToRassm, "zntToRassmName" : zntToRassmName.get(), "dateToRassm" : dateToRassm.get(),
                                "monthToRassm" : monthToRassm.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 3.2 Cправка об издержках.docx")

            messagebox.showinfo("Сформировано", "Сформировано по делу об АП\n10418000-" + numberCase + "/2020")

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

    box_01, box_02, box_03, box_04, box_05, box_06, box_07, box_08, box_09, box_10, box_11, box_12, box_13, box_14,\
    box_15, box_16, box_17, box_18, box_19 = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
    BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
    BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

    zntToARName, zntZaprosName, zntToRassmName, zntPostName, dateToAR, monthToAR, dateIstreb, monthIstreb, dateZapros, monthZapros, dateProtokol,\
    monthProtokol, dateToRassm, monthToRassm, datePost, monthPost = StringVar(), StringVar(), StringVar(), StringVar(),\
    StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),\
    StringVar(), StringVar(), StringVar()

    with open(resourcesProvider.getConfigPath(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    listOfPer = []
    for l in dapJson['signers'].keys():
        listOfPer.append(l)
    listOfMonths = []
    for l in dapJson['months'].keys():
        listOfMonths.append(l)

    Checkbutton(text="Решение о передаче ДАП", variable=box_01).place(x=10, y=10, height = 20)
    Checkbutton(text="Определение о принятии дела к своему производству", variable=box_02).place(x=200, y=10, height = 20)
    znt1_ = ttk.Combobox(winChooseDocs, textvariable=zntToARName, values = listOfPer, height = 2)
    znt1_['state']='readonly'
    znt1_.place(x = 30, y = 35, width=110, height = 20)
    Label(text='дата передачи ДАП').place(x=220, y=35, height = 20)
    Entry(textvariable=dateToAR).place(x=340, y=35, width=30, height = 20)
    monthper_ = ttk.Combobox(winChooseDocs, textvariable=monthToAR, values = listOfMonths, height = 12)
    monthper_['state']='readonly'
    monthper_.place(x = 380, y = 35, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=35, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=55, height = 20)
    Checkbutton(text="Определение об истребовании документов и сведений", variable=box_03).place(x=10, y=80, height = 20)
    Checkbutton(text="Повестка о явке", variable=box_04).place(x=410, y=80, height = 20)
    Label(text='дата направления').place(x=220, y=105, height = 20)
    Entry(textvariable=dateIstreb).place(x=340, y=105, width=30, height = 20)
    monthpovestka_ = ttk.Combobox(winChooseDocs, textvariable=monthIstreb, values = listOfMonths, height = 12)
    monthpovestka_['state']='readonly'
    monthpovestka_.place(x = 380, y = 105, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=105, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=125, height = 20)
    Checkbutton(text="Запрос в ГИБДД", variable=box_05).place(x=10, y=150, height = 20)
    Checkbutton(text="Запрос в Росреестр с приложением", variable=box_06).place(x=300, y=150, height = 20)
    znt2_ = ttk.Combobox(winChooseDocs, textvariable=zntZaprosName, values = listOfPer, height = 2)
    znt2_['state']='readonly'
    znt2_.place(x = 30, y = 175, width=110, height = 20)
    Label(text='дата направления').place(x=220, y=175, height = 20)
    Entry(textvariable=dateZapros).place(x=340, y=175, width=30, height = 20)
    monthzapros_ = ttk.Combobox(winChooseDocs, textvariable=monthZapros, values = listOfMonths, height = 12)
    monthzapros_['state']='readonly'
    monthzapros_.place(x = 380, y = 175, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=175, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=195, height = 20)
    Checkbutton(text="Шаблон ТЛГ вызов на протокол", variable=box_07).place(x=10, y=220, height = 20)
    Checkbutton(text="Шаблон ответа ЮЛ на вызов на протокол", variable=box_08).place(x=270, y=220, height = 20)
    Checkbutton(text="Шаблон протокола об АП", variable=box_09).place(x=10, y=240, height = 20)
    Label(text='дата протокола об АП').place(x=200, y=265, height = 20)
    Entry(textvariable=dateProtokol).place(x=340, y=265, width=30, height = 20)
    monthprotokol_ = ttk.Combobox(winChooseDocs, textvariable=monthProtokol, values = listOfMonths, height = 12)
    monthprotokol_['state']='readonly'
    monthprotokol_.place(x = 380, y = 265, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=265, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=285, height = 20)
    Checkbutton(text="Рапорт об окончании адм.расследования", variable=box_10).place(x=10, y=310, height = 20)
    Checkbutton(text="Справка об отсутствии издержек", variable=box_11).place(x=320, y=310, height = 20)
    Checkbutton(text="Определение о назначении времени и места рассмотрения ДАП", variable=box_12).place(x=10, y=330, height = 20)
    Checkbutton(text="Шаблон ТЛГ вызов на рассмотрение", variable=box_13).place(x=10, y=350, height = 20)
    Checkbutton(text="Шаблон ответа ЮЛ на вызов на рассмотрение", variable=box_14).place(x=245, y=350, height = 20)
    znt3_ = ttk.Combobox(winChooseDocs, textvariable=zntToRassmName, values = listOfPer, height = 2)
    znt3_['state']='readonly'
    znt3_.place(x = 30, y = 375, width=110, height = 20)
    Label(text='дата передачи ДАП').place(x=220, y=375, height = 20)
    Entry(textvariable=dateToRassm).place(x=340, y=375, width=30, height = 20)
    monthrassm_ = ttk.Combobox(winChooseDocs, textvariable=monthToRassm, values = listOfMonths, height = 12)
    monthrassm_['state']='readonly'
    monthrassm_.place(x = 380, y = 375, width=80, height = 20)
    Label(text='2020 года').place(x=465, y=375, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=395, height = 20)
    Checkbutton(text="Определение об отложении времени и места рассмотрения ДАП", variable=box_15).place(x=30, y=420, height = 20)
    Checkbutton(text="Определение о продлении срока рассмотрения ДАП", variable=box_16).place(x=30, y=440, height = 20)
    Checkbutton(text="Шаблон постановления по ДАП", variable=box_17).place(x=10, y=460, height = 20)
    Checkbutton(text="Представление об устранении причин и условий", variable=box_18).place(x=10, y=480, height = 20)
    znt4_ = ttk.Combobox(winChooseDocs, textvariable=zntPostName, values = listOfPer, height = 2)
    znt4_['state']='readonly'
    znt4_.place(x = 30, y = 505, width=110, height = 20)
    Label(text='дата рассмотрения').place(x=220, y=505, height = 20)
    Entry(textvariable=datePost).place(x=340, y=505, width=30, height = 20)
    monthrassm2_ = ttk.Combobox(winChooseDocs, textvariable=monthPost, values = listOfMonths, height = 12)
    monthrassm2_['state']='readonly'
    monthrassm2_.place(x = 380, y = 505, width=80, height = 20)
    Label(text='2020 года').place(x=465, y= 505, height = 20)
    Label(text='______________________________________________________________________________________________________').place(x=10, y=525, height = 20)
    Checkbutton(text="Бирка ДАП", variable=box_19).place(x=10, y=550, height = 20)
    Button(text="Сформировать", command=formDocs).place(relx=.5, rely=.95, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")

    with open(resourcesProvider.getDealsPath(), 'r', encoding='utf-8') as readNumbers:
        numbersJson = json.load(readNumbers)

    numberCase = chosenDeal

    artCode = numbersJson[numberCase]['artCode']
    dateInit = numbersJson[numberCase]['dateInit']
    dateRegUl = numbersJson[numberCase]['company']['dateRegUl']
    emailUl = numbersJson[numberCase]['company']['emailUl']
    inn = numbersJson[numberCase]['company']['inn']
    kpp = numbersJson[numberCase]['company']['kpp']
    monthInit = numbersJson[numberCase]['monthInit']
    numberDt = numbersJson[numberCase]['numberDt']
    ogrn = numbersJson[numberCase]['company']['ogrn']
    partCode = numbersJson[numberCase]['partCode']
    tpdecl = numbersJson[numberCase]['tpdecl']
    ul = numbersJson[numberCase]['company']['ul']
    ulCity = numbersJson[numberCase]['company']['address']['ulCity']
    ulIndex = numbersJson[numberCase]['company']['address']['ulIndex']
    ulStreetOffice = numbersJson[numberCase]['company']['address']['ulStreetOffice']
    ulSubrf = numbersJson[numberCase]['company']['address']['ulSubrf']
    zpName_dp = numbersJson[numberCase]['company']['actioner']['zpName_dp']
    zpName_ip = numbersJson[numberCase]['company']['actioner']['zpName_ip']
    zpName_rp = numbersJson[numberCase]['company']['actioner']['zpName_rp']
    zpName_tp = numbersJson[numberCase]['company']['actioner']['zpName_tp']
    zpName_vp = numbersJson[numberCase]['company']['actioner']['zpName_vp']
    zpPosition = numbersJson[numberCase]['company']['actioner']['zpPosition']
    zpPosition_ip = dapJson['actionerPositions'][zpPosition]['ip']
    zpPosition_rp = dapJson['actionerPositions'][zpPosition]['rp']
    zpPosition_dp = dapJson['actionerPositions'][zpPosition]['dp']
    zpPosition_vp = dapJson['actionerPositions'][zpPosition]['vp']
    zpPosition_tp = dapJson['actionerPositions'][zpPosition]['tp']
    zpPosition_ip_low = dapJson['actionerPositions'][zpPosition]['ip_low']
    zpPosition_rp_low = dapJson['actionerPositions'][zpPosition]['rp_low']
    zpPosition_dp_low = dapJson['actionerPositions'][zpPosition]['dp_low']
    zpPosition_vp_low = dapJson['actionerPositions'][zpPosition]['vp_low']
    zpPosition_tp_low = dapJson['actionerPositions'][zpPosition]['tp_low']

    employeeOar = chosenEmployeeOar

    fiooar_ip = dapJson['employeesOar'][employeeOar]['fiooar_ip']
    fiooar_rp = dapJson['employeesOar'][employeeOar]['fiooar_rp']
    fiooar_dp = dapJson['employeesOar'][employeeOar]['fiooar_dp']
    fiooar_vp = dapJson['employeesOar'][employeeOar]['fiooar_vp']
    fiooar_tp = dapJson['employeesOar'][employeeOar]['fiooar_tp']
    doloar_ip = dapJson['employeesOar'][employeeOar]['doloar_ip']
    doloar_rp = dapJson['employeesOar'][employeeOar]['doloar_rp']
    doloar_dp = dapJson['employeesOar'][employeeOar]['doloar_dp']
    doloar_vp = dapJson['employeesOar'][employeeOar]['doloar_vp']
    doloar_tp = dapJson['employeesOar'][employeeOar]['doloar_tp']
    doloar_ip_low = dapJson['employeesOar'][employeeOar]['doloar_ip_low']
    doloar_rp_low = dapJson['employeesOar'][employeeOar]['doloar_rp_low']
    doloar_dp_low = dapJson['employeesOar'][employeeOar]['doloar_dp_low']
    doloar_vp_low = dapJson['employeesOar'][employeeOar]['doloar_vp_low']
    doloar_tp_low = dapJson['employeesOar'][employeeOar]['doloar_tp_low']
    doloar_ip_sh = dapJson['employeesOar'][employeeOar]['doloar_ip_sh']
    doloar_rp_sh = dapJson['employeesOar'][employeeOar]['doloar_rp_sh']
    doloar_dp_sh = dapJson['employeesOar'][employeeOar]['doloar_dp_sh']
    doloar_vp_sh = dapJson['employeesOar'][employeeOar]['doloar_vp_sh']
    doloar_tp_sh = dapJson['employeesOar'][employeeOar]['doloar_tp_sh']
    doloar_ip_sh_low = dapJson['employeesOar'][employeeOar]['doloar_ip_sh_low']
    doloar_rp_sh_low = dapJson['employeesOar'][employeeOar]['doloar_rp_sh_low']
    doloar_dp_sh_low = dapJson['employeesOar'][employeeOar]['doloar_dp_sh_low']
    doloar_vp_sh_low = dapJson['employeesOar'][employeeOar]['doloar_vp_sh_low']
    doloar_tp_sh_low = dapJson['employeesOar'][employeeOar]['doloar_tp_sh_low']
    emailOar = dapJson['employeesOar'][employeeOar]['emailOar']
    gortel = dapJson['employeesOar'][employeeOar]['gortel']



    winChooseDocs.mainloop()