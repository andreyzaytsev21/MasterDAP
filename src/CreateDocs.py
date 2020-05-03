from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from docxtpl import DocxTemplate
import json
from ResourcesProvider import ResourcesProvider

def runCreateDocs(resourcesProvider: ResourcesProvider, chosenDeal: str, chosenEmployeeOar: str):

    def formDocs():
        if box_01.get() == False and box_02.get() == False and box_03.get() == False and box_04.get() == False and \
                        box_05.get() == False and box_06.get() == False and box_07.get() == False and box_08.get() == False and \
                        box_09.get() == False and box_10.get() == False and box_11.get() == False and box_12.get() == False and \
                        box_13.get() == False and box_14.get() == False and box_15.get() == False and box_16.get() == False and \
                        box_17.get() == False and box_18.get() == False and box_19.get() == False:
            messagebox.showerror("Ошибка", "Выберите документы")
        else:
            #zntZapros = dapJson['signers'][zntZaprosName.get()]['znt_ip']
            #zntToRassm = dapJson['signers'][zntToRassmName.get()]['znt_ip']
            context = {"artCode" : artCode, "codeRF_sh" : codeRF_sh,
                       "dateInit" : dateInit, "dateRegUl" : dateRegUl, "emailUl" : emailUl,
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

            if box_03.get():
                doc = DocxTemplate("../templates/03.docx")
                context.update({"dateIstreb" : dateIstreb.get(), "monthIstreb" : monthIstreb.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 2.3 ОПРЕДЕЛЕНИЕ об истребовании документов и сведений.docx")

            if box_04.get():
                doc = DocxTemplate("../templates/04.docx")
                context.update({"dateIstreb" : dateIstreb.get(), "monthIstreb" : monthIstreb.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 2.4 ПОВЕСТКА о явке.docx")

            # ГОТОВ
            if box_05.get():
                zntZapros_ip = dapJson['signers'][zntZaprosName.get()]['znt_ip']
                doc = DocxTemplate("../templates/05.docx")
                context.update({"zntZapros_ip" : zntZapros_ip, "zntZaprosName_ip" : zntZaprosName.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 2.5 Запрос в ГИБДД.docx")

            if box_06.get():
                zntZapros_ip = dapJson['signers'][zntZaprosName.get()]['znt_ip']
                doc1 = DocxTemplate("../templates/06.docx")
                doc2 = DocxTemplate("../templates/06_1.docx")
                context.update({"zntZapros_ip" : zntZapros_ip, "zntZaprosName_ip" : zntZaprosName.get(),
                               "dateZapros" : dateZapros.get(), "monthZapros" : monthZapros.get()})
                doc1.render(context)
                doc2.render(context)
                doc1.save("../buffer/" + numberCase + "__ 2.6 Запрос в РОСРЕЕСТР.docx")
                doc2.save("../buffer/" + numberCase + "__ 2.6 Приложение - Запрос в РОСРЕЕСТР.docx")

            # ГОТОВ
            if box_11.get():
                zntToRassm_ip = dapJson['signers'][zntToRassmName.get()]['znt_ip']
                doc = DocxTemplate("../templates/11.docx")
                context.update({"zntToRassm_ip" : zntToRassm_ip, "zntToRassmName_ip" : zntToRassmName.get(),
                                "dateToRassm" : dateToRassm.get(), "monthToRassm" : monthToRassm.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "__ 3.2 Cправка об отсутствии издержек.docx")

            if box_15.get():
                zntOtlozh_ip = dapJson['signers'][zntOtlozhName.get()]['znt_ip']
                doc = DocxTemplate("../templates/15.docx")
                context.update({"zntOtlozh_ip" : zntOtlozh_ip, "zntOtlozhName_ip" : zntOtlozhName.get(),
                               "dateOtlozh" : dateOtlozh.get(), "monthOtlozh" : monthOtlozh.get()})
                doc.render(context)
                doc.save("../buffer/" + numberCase + "Определение об отложении.docx")

            messagebox.showinfo("Сформировано", "Сформировано по делу об АП\n10418000-" + numberCase + "/2020")

    def close_window():
        winChooseDocs.destroy()

    winChooseDocs = Tk()
    winChooseDocs.title("Выбор документов для ДАП 10418000-" + chosenDeal + "/2020")
    w = winChooseDocs.winfo_screenwidth()
    h = winChooseDocs.winfo_screenheight()
    w = w // 2
    w = w // 2
    h = h // 2
    w = w - 285
    h = h - 470
    winChooseDocs.geometry('570x850+{}+{}'.format(w, h))

    box_01, box_02, box_03, box_04, box_05, box_06, box_07, box_08, box_09, box_10, box_11, box_12, box_13, box_14,\
    box_15, box_16, box_17, box_18, box_19, box_20 = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
    BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
    BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

    zntToARName, zntZaprosName, zntToRassmName, zntOtlozhName, zntPostName, dateToAR, monthToAR, dateIstreb, monthIstreb,\
    dateZapros, monthZapros, dateProtokol, monthProtokol, dateToRassm, monthToRassm, dateOtlozh, monthOtlozh, datePost,\
    monthPost = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),\
    StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),\
    StringVar(), StringVar()

    with open(resourcesProvider.get_config_path(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)
    listOfPer = []
    for l in dapJson['signers'].keys():
        listOfPer.append(l)
    listOfMonths = []
    for l in dapJson['months'].keys():
        listOfMonths.append(l)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeToAR = LabelFrame(winChooseDocs, text="Передача дела об АП для проведения административного расследования", fg = "blue", bg = "#37faac", labelanchor = "n", padx = 5, pady = 5)
    labelframeToAR.pack(fill="x", expand="yes")
    Checkbutton(labelframeToAR, text="Решение о передаче дела об АП", variable=box_01, bg = "#37faac", activebackground = "#37faac").pack(anchor="w")
    Checkbutton(labelframeToAR, text="Определение о принятии дела к своему производству", variable=box_02, bg = "#37faac", activebackground = "#37faac").pack(anchor="w")
    frame1 = Frame(labelframeToAR, bg = "#37faac")
    Label(frame1, text="дата передачи", bg = "#37faac").pack(side=LEFT)
    Entry(frame1, textvariable=dateToAR, width = 5).pack(side=LEFT, padx = 3)
    month1 = ttk.Combobox(frame1, textvariable=monthToAR, values = listOfMonths, height = 12, width = 10)
    month1['state']='readonly'
    month1.pack(side=LEFT, padx = 3)
    Label(frame1, text="2020 года", bg = "#37faac").pack(side=LEFT, padx = 3)
    frame1.pack(side=LEFT)
    frame2 = Frame(labelframeToAR, bg = "#37faac")
    Label(frame2, text="лицо, передающее", bg = "#37faac").pack(side=LEFT)
    znt1 = ttk.Combobox(frame2, textvariable=zntToARName, values = listOfPer, height = 2, width = 15)
    znt1['state']='readonly'
    znt1.pack(side=LEFT)
    frame2.pack(side=RIGHT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros1 = LabelFrame(winChooseDocs, text = "Запросы в ходе административного расследования", fg = "blue", bg = "#7affca", labelanchor = "n", padx = 5, pady = 5)
    labelframeZapros1.pack(fill="x", expand = "yes")
    Checkbutton(labelframeZapros1, text="Определение об истребовании документов и сведений", variable=box_03, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros1, text="Повестка о явке", variable=box_04, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    frame3 = Frame(labelframeZapros1, bg = "#7affca")
    Label(frame3, text="дата направления", bg = "#7affca").pack(side=LEFT)
    Entry(frame3, textvariable=dateIstreb, width = 5).pack(side=LEFT, padx = 3)
    month2 = ttk.Combobox(frame3, textvariable=monthIstreb, values = listOfMonths, height = 12, width = 10)
    month2['state']='readonly'
    month2.pack(side=LEFT, padx = 3)
    Label(frame3, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
    frame3.pack(side=LEFT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros2 = LabelFrame(winChooseDocs, bg = "#7affca", padx = 5, pady = 5)
    labelframeZapros2.pack(fill="x", expand = "yes")
    Checkbutton(labelframeZapros2, text="Запрос в ГИБДД", variable=box_05, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros2, text="Запрос в Росреестр", variable=box_06, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    frame4 = Frame(labelframeZapros2, bg = "#7affca")
    Label(frame4, text="дата запроса", bg = "#7affca").pack(side=LEFT)
    Entry(frame4, textvariable=dateZapros, width = 5).pack(side=LEFT, padx = 3)
    month3 = ttk.Combobox(frame4, textvariable=monthZapros, values = listOfMonths, height = 12, width = 10)
    month3['state']='readonly'
    month3.pack(side=LEFT, padx = 3)
    Label(frame4, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
    frame4.pack(side=LEFT)
    frame5 = Frame(labelframeZapros2, bg = "#7affca")
    Label(frame5, text="лицо, направляющее", bg = "#7affca").pack(side=LEFT)
    znt2 = ttk.Combobox(frame5, textvariable=zntZaprosName, values = listOfPer, height = 2)
    znt2['state']='readonly'
    znt2.pack(side=LEFT)
    frame5.pack(side=RIGHT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros3 = LabelFrame(winChooseDocs, bg = "#7affca", padx = 5, pady = 5)
    labelframeZapros3.pack(fill="x", expand = "yes")
    Checkbutton(labelframeZapros3, text="Телеграмма - вызов на протокол", variable=box_07, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros3, text="Уведомление - вызов на протокол", variable=box_08, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros3, text="Шаблон протокола об АП", variable=box_09, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
    frame6 = Frame(labelframeZapros3, bg = "#7affca")
    Label(frame6, text="дата протокола", bg = "#7affca").pack(side=LEFT)
    Entry(frame6, textvariable=dateProtokol, width = 5).pack(side=LEFT, padx = 3)
    month4 = ttk.Combobox(frame6, textvariable=monthProtokol, values = listOfMonths, height = 12, width = 10)
    month4['state']='readonly'
    month4.pack(side=LEFT, padx = 3)
    Label(frame6, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
    frame6.pack(side=LEFT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeToRassm = LabelFrame(winChooseDocs, text = "Передача дела об АП на рассмотрение", fg = "blue", bg = "#C1F1B1", labelanchor = "n", padx = 5, pady = 5)
    labelframeToRassm.pack(fill="x", expand="yes")
    Checkbutton(labelframeToRassm, text="Рапорт об окончании адм.расследования", variable=box_10, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Справка об отсутствии издержек", variable=box_11, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Определение о назначении времени и места рассмотрения дела об АП", variable=box_12, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Письмо - вызов на рассмотрерние", variable=box_13, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Телеграмма - вызов на рассмотрение", variable=box_14, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
    frame7 = Frame(labelframeToRassm, bg = "#C1F1B1")
    Label(frame7, text="дата передачи", bg = "#C1F1B1").pack(side=LEFT)
    Entry(frame7, textvariable=dateToRassm, width = 5).pack(side=LEFT, padx = 3)
    month5 = ttk.Combobox(frame7, textvariable=monthToRassm, values = listOfMonths, height = 12, width = 10)
    month5['state']='readonly'
    month5.pack(side=LEFT, padx = 3)
    Label(frame7, text="2020 года", bg = "#C1F1B1").pack(side=LEFT, padx = 3)
    frame7.pack(side=LEFT)
    frame8 = Frame(labelframeToRassm, bg = "#C1F1B1")
    Label(frame8, text="лицо, принимающее", bg = "#C1F1B1").pack(side=LEFT)
    znt3 = ttk.Combobox(frame8, textvariable=zntToRassmName, values = listOfPer, height = 2)
    znt3['state']='readonly'
    znt3.pack(side=LEFT)
    frame8.pack(side=RIGHT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeOtlozh = LabelFrame(winChooseDocs, text = "Отложение рассмотрения дела об АП", fg = "blue", bg = "#D7FFD7", labelanchor = "n", padx = 5, pady = 5)
    labelframeOtlozh.pack(fill="x", expand="yes")
    Checkbutton(labelframeOtlozh, text="Определение об отложении времени и места рассмотрения дела об АП", variable=box_15, bg = "#D7FFD7", activebackground = "#D7FFD7").pack(anchor="w")
    Checkbutton(labelframeOtlozh, text="Определение о продлении срока рассмотрения дела об АП", variable=box_16, bg = "#D7FFD7", activebackground = "#D7FFD7").pack(anchor="w")
    frame9 = Frame(labelframeOtlozh, bg = "#D7FFD7")
    Label(frame9, text="дата отложения", bg = "#D7FFD7").pack(side=LEFT)
    Entry(frame9, textvariable = dateOtlozh, width = 5).pack(side=LEFT, padx = 3)
    month6 = ttk.Combobox(frame9, textvariable = monthOtlozh, values = listOfMonths, height = 12, width = 10)
    month6['state']='readonly'
    month6.pack(side=LEFT, padx = 3)
    Label(frame9, text="2020 года", bg = "#D7FFD7").pack(side=LEFT, padx = 3)
    frame9.pack(side=LEFT)
    frame10 = Frame(labelframeOtlozh, bg = "#D7FFD7")
    Label(frame10, text="лицо, откладывающее", bg = "#D7FFD7").pack(side=LEFT)
    znt4 = ttk.Combobox(frame10, textvariable = zntOtlozhName, values = listOfPer, height = 2)
    znt4['state']='readonly'
    znt4.pack(side=LEFT)
    frame10.pack(side=RIGHT)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframePost = LabelFrame(winChooseDocs, text = "Рассмотрение дела об АП на рассмотрение", fg = "blue", bg = "#ebfff7", labelanchor = "n", padx = 5, pady = 5)
    labelframePost.pack(fill="x", expand="yes")
    Checkbutton(labelframePost, text="Шаблон постановления по делу об АП", variable=box_17, bg = "#ebfff7", activebackground = "#ebfff7").pack(anchor="w")
    Checkbutton(labelframePost, text="Представление об устранении причин и условий", variable=box_18, bg = "#ebfff7", activebackground = "#ebfff7").pack(anchor="w")
    frame11 = Frame(labelframePost, bg = "#ebfff7")
    Label(frame11, text="дата рассмотрения", bg = "#ebfff7").pack(side=LEFT)
    Entry(frame11, textvariable=datePost, width = 5).pack(side=LEFT, padx = 3)
    month7 = ttk.Combobox(frame11, textvariable=monthPost, values = listOfMonths, height = 12, width = 10)
    month7['state']='readonly'
    month7.pack(side=LEFT, padx = 3)
    Label(frame11, text="2020 года", bg = "#ebfff7").pack(side=LEFT, padx = 3)
    frame11.pack(side=LEFT)
    frame12 = Frame(labelframePost, bg = "#ebfff7")
    Label(frame12, text="лицо, рассматривающее", bg = "#ebfff7").pack(side=LEFT)
    znt5 = ttk.Combobox(frame12, textvariable=zntPostName, values = listOfPer, height = 2)
    znt5['state']='readonly'
    znt5.pack(side=LEFT)
    frame12.pack(side=RIGHT)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Checkbutton(text="Бирка дела об АП", variable=box_19).pack(padx = 7, anchor="w")
    Checkbutton(text="Бирка дела об АП (мини)", variable=box_20).pack(padx = 7, anchor="w")
    Label("").pack()
    Button(text="Сформировать", command=formDocs).place(relx=.5, rely=.97, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.97, anchor="e")

    with open(resourcesProvider.get_deals_path(), 'r', encoding='utf-8') as readNumbers:
        numbersJson = json.load(readNumbers)

    numberCase = chosenDeal

    artCode = numbersJson[numberCase]['artCode']
    codeRF_sh = numbersJson[numberCase]['codeRF_sh']
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
    zpName_ip = numbersJson[numberCase]['company']['actioner']['zpName_ip']
    zpName_rp = numbersJson[numberCase]['company']['actioner']['zpName_rp']
    zpName_dp = numbersJson[numberCase]['company']['actioner']['zpName_dp']
    zpName_vp = numbersJson[numberCase]['company']['actioner']['zpName_vp']
    zpName_tp = numbersJson[numberCase]['company']['actioner']['zpName_tp']
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