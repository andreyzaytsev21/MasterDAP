from tkinter import *
from tkinter import ttk
import json

winChooseDocs = Tk()
#winChooseDocs.title("Выбор документов для ДАП 10418000-" + chosenDeal + "/2020")
w = winChooseDocs.winfo_screenwidth()
h = winChooseDocs.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 285
h = h - 470
winChooseDocs.geometry('570x850+{}+{}'.format(w, h))

box_01, box_02, box_03, box_04, box_05, box_06, box_07, box_08, box_09, box_10, box_11, box_12, box_13, box_14,\
box_15, box_16, box_17, box_18, box_19, box_20 = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(),\
BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

zntToARName, zntZaprosName, zntToRassmName, zntPostName, dateToAR, monthToAR, dateIstreb, monthIstreb, dateZapros, \
monthZapros, dateProtokol, monthProtokol, dateToRassm, monthToRassm, datePost, monthPost = StringVar(), StringVar(),\
StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),\
StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

with open("../data/dap.json", 'r', encoding='utf-8') as f:
    dapJson = json.load(f)
listOfPer = []
for l in dapJson['signers'].keys():
    listOfPer.append(l)
listOfMonths = []
for l in dapJson['months'].keys():
    listOfMonths.append(l)


labelframeToAR = LabelFrame(winChooseDocs, text="Передача дела об АП для проведения административного расследования", fg = "blue", bg = "#37faac", labelanchor = "n", padx = 5, pady = 5)
labelframeToAR.pack(fill="x", expand="yes")
Checkbutton(labelframeToAR, text="Решение о передаче дела об АП", variable=box_01, bg = "#37faac", activebackground = "#37faac").pack(anchor="w")
Checkbutton(labelframeToAR, text="Определение о принятии дела к своему производству", variable=box_02, bg = "#37faac", activebackground = "#37faac").pack(anchor="w")
frame1 = Frame(labelframeToAR, bg = "#37faac")
Label(frame1, text="дата передачи", bg = "#37faac").pack(side=LEFT)
Entry(frame1, textvariable=dateToAR, width = 5).pack(side=LEFT, padx = 3)
monthper_ = ttk.Combobox(frame1, textvariable=monthToAR, values = listOfMonths, height = 12, width = 10)
monthper_['state']='readonly'
monthper_.pack(side=LEFT, padx = 3)
Label(frame1, text="2020 года", bg = "#37faac").pack(side=LEFT, padx = 3)
frame1.pack(side=LEFT)
frame2 = Frame(labelframeToAR, bg = "#37faac")
Label(frame2, text="лицо, передающее", bg = "#37faac").pack(side=LEFT)
znt1_ = ttk.Combobox(frame2, textvariable=zntToARName, values = listOfPer, height = 2, width = 15)
znt1_['state']='readonly'
znt1_.pack(side=LEFT)
frame2.pack(side=RIGHT)
#+++++++++++++++++++++++++ready+++++++++++++++++++++++++++

labelframeZapros1 = LabelFrame(winChooseDocs, text = "Запросы в ходе административного расследования", fg = "blue", bg = "#7affca", labelanchor = "n", padx = 5, pady = 5)
labelframeZapros1.pack(fill="x", expand = "yes")
Checkbutton(labelframeZapros1, text="Определение об истребовании документов и сведений", variable=box_03, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
Checkbutton(labelframeZapros1, text="Повестка о явке", variable=box_04, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
frame3 = Frame(labelframeZapros1, bg = "#7affca")
Label(frame3, text="дата направления", bg = "#7affca").pack(side=LEFT)
Entry(frame3, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame3, width = 10).pack(side=LEFT, padx = 3)
Label(frame3, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
frame3.pack(side=LEFT)

labelframeZapros2 = LabelFrame(winChooseDocs, bg = "#7affca", padx = 5, pady = 5)
labelframeZapros2.pack(fill="x", expand = "yes")
Checkbutton(labelframeZapros2, text="Запрос в ГИБДД", variable=box_05, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
Checkbutton(labelframeZapros2, text="Запрос в Росреестр", variable=box_06, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
frame4 = Frame(labelframeZapros2, bg = "#7affca")
Label(frame4, text="дата запроса", bg = "#7affca").pack(side=LEFT)
Entry(frame4, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame4, width = 10).pack(side=LEFT, padx = 3)
Label(frame4, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
frame4.pack(side=LEFT)
frame5 = Frame(labelframeZapros2, bg = "#7affca")
Label(frame5, text="лицо, направляющее", bg = "#7affca").pack(side=LEFT)
ttk.Combobox(frame5,height = 2).pack(side=LEFT)
frame5.pack(side=RIGHT)

labelframeZapros3 = LabelFrame(winChooseDocs, bg = "#7affca", padx = 5, pady = 5)
labelframeZapros3.pack(fill="x", expand = "yes")
Checkbutton(labelframeZapros3, text="Телеграмма - вызов на протокол", variable=box_07, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
Checkbutton(labelframeZapros3, text="Уведомление - вызов на протокол", variable=box_08, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
Checkbutton(labelframeZapros3, text="Шаблон протокола об АП", variable=box_09, bg = "#7affca", activebackground = "#7affca").pack(anchor="w")
frame6 = Frame(labelframeZapros3, bg = "#7affca")
Label(frame6, text="дата протокола", bg = "#7affca").pack(side=LEFT)
Entry(frame6, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame6, width = 10).pack(side=LEFT, padx = 3)
Label(frame6, text="2020 года", bg = "#7affca").pack(side=LEFT, padx = 3)
frame6.pack(side=LEFT)

labelframeToRassm = LabelFrame(winChooseDocs, text = "Передача дела об АП на рассмотрение", fg = "blue", bg = "#C1F1B1", labelanchor = "n", padx = 5, pady = 5)
labelframeToRassm.pack(fill="x", expand="yes")
Checkbutton(labelframeToRassm, text="Рапорт об окончании адм.расследования", variable=box_10, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
Checkbutton(labelframeToRassm, text="Справка об отсутствии издержек", variable=box_11, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
Checkbutton(labelframeToRassm, text="Определение о назначении времени и места рассмотрения дела об АП", variable=box_12, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
Checkbutton(labelframeToRassm, text="Письмо - вызов на рассмотрерние", variable=box_13, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
Checkbutton(labelframeToRassm, text="Телеграмма - вызов на рассмотрение", variable=box_14, bg = "#C1F1B1", activebackground = "#C1F1B1").pack(anchor="w")
frame7 = Frame(labelframeToRassm, bg = "#C1F1B1")
Label(frame7, text="дата передачи", bg = "#C1F1B1").pack(side=LEFT)
Entry(frame7, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame7, width = 10).pack(side=LEFT, padx = 3)
Label(frame7, text="2020 года", bg = "#C1F1B1").pack(side=LEFT, padx = 3)
frame7.pack(side=LEFT)
frame8 = Frame(labelframeToRassm, bg = "#C1F1B1")
Label(frame8, text="лицо, принимающее", bg = "#C1F1B1").pack(side=LEFT)
ttk.Combobox(frame8,height = 2).pack(side=LEFT)
frame8.pack(side=RIGHT)

labelframeOtlozh = LabelFrame(winChooseDocs, text = "Отложение рассмотрения дела об АП", fg = "blue", bg = "#D7FFD7", labelanchor = "n", padx = 5, pady = 5)
labelframeOtlozh.pack(fill="x", expand="yes")
Checkbutton(labelframeOtlozh, text="Определение об отложении времени и места рассмотрения дела об АП", variable=box_15, bg = "#D7FFD7", activebackground = "#D7FFD7").pack(anchor="w")
Checkbutton(labelframeOtlozh, text="Определение о продлении срока рассмотрения дела об АП", variable=box_16, bg = "#D7FFD7", activebackground = "#D7FFD7").pack(anchor="w")
frame9 = Frame(labelframeOtlozh, bg = "#D7FFD7")
Label(frame9, text="дата отложения", bg = "#D7FFD7").pack(side=LEFT)
Entry(frame9, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame9, width = 10).pack(side=LEFT, padx = 3)
Label(frame9, text="2020 года", bg = "#D7FFD7").pack(side=LEFT, padx = 3)
frame9.pack(side=LEFT)
frame10 = Frame(labelframeOtlozh, bg = "#D7FFD7")
Label(frame10, text="лицо, откладывающее", bg = "#D7FFD7").pack(side=LEFT)
ttk.Combobox(frame10,height = 2).pack(side=LEFT)
frame10.pack(side=RIGHT)

labelframePost = LabelFrame(winChooseDocs, text = "Рассмотрение дела об АП на рассмотрение", fg = "blue", bg = "#ebfff7", labelanchor = "n", padx = 5, pady = 5)
labelframePost.pack(fill="x", expand="yes")
Checkbutton(labelframePost, text="Шаблон постановления по делу об АП", variable=box_17, bg = "#ebfff7", activebackground = "#ebfff7").pack(anchor="w")
Checkbutton(labelframePost, text="Представление об устранении причин и условий", variable=box_18, bg = "#ebfff7", activebackground = "#ebfff7").pack(anchor="w")
frame11 = Frame(labelframePost, bg = "#ebfff7")
Label(frame11, text="дата рассмотрения", bg = "#ebfff7").pack(side=LEFT)
Entry(frame11, width = 5).pack(side=LEFT, padx = 3)
ttk.Combobox(frame11, width = 10).pack(side=LEFT, padx = 3)
Label(frame11, text="2020 года", bg = "#ebfff7").pack(side=LEFT, padx = 3)
frame11.pack(side=LEFT)
frame12 = Frame(labelframePost, bg = "#ebfff7")
Label(frame12, text="лицо, рассматривающее", bg = "#ebfff7").pack(side=LEFT)
ttk.Combobox(frame12,height = 2).pack(side=LEFT)
frame12.pack(side=RIGHT)

Checkbutton(text="Бирка дела об АП", variable=box_19).pack(padx = 7, anchor="w")
Checkbutton(text="Бирка дела об АП (мини)", variable=box_20).pack(padx = 7, anchor="w")
Label("").pack()

Button(text="Сформировать").place(relx=.5, rely=.97, anchor="c")
Button(text="Отмена").place(relx=.97, rely=.97, anchor="e")

winChooseDocs.mainloop()