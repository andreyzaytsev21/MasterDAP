from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from ResourcesProvider import ResourcesProvider

def runSaveDeal(resourcesProvider: ResourcesProvider):

    def close_window():
        winEnterWindow.destroy()

    def show_message():
        if numberCase.get() == '' or ul.get() == '':
            messagebox.showerror("Ошибка", "Заполните все поля")
        else:
            if partCode.get() == '' or partCode.get() == '-':
                codeRF_ip = "статья " + artCode.get()
                codeRF_rp = "статьи " + artCode.get()
                codeRF_dp = "статье " + artCode.get()
                codeRF_vp = "статью " + artCode.get()
                codeRF_tp = "статьей " + artCode.get()
                codeRF_sh = "ст. " + artCode.get()
            else:
                codeRF_ip = "часть " + partCode.get() + "статьи " + artCode.get()
                codeRF_rp = "части " + partCode.get() + "статьи " + artCode.get()
                codeRF_dp = "части " + partCode.get() + "статьи " + artCode.get()
                codeRF_vp = "часть " + partCode.get() + "статьи " + artCode.get()
                codeRF_tp = "частью " + partCode.get() + "статьи " + artCode.get()
                codeRF_sh = "ч. " + partCode.get() + "ст. " + artCode.get()
            letters2 = zpName_ip.get()[len(zpName_ip.get())-2:]
            letters3 = zpName_ip.get()[len(zpName_ip.get())-3:]
            if letters3 == "ева" or letters3 == "ёва" or letters3 == "ина" or letters3 == "ына" or letters3 == "ова":
                zpName_rp = zpName_ip.get()[:len(zpName_ip.get())-1] + "ой"
                zpName_dp = zpName_ip.get()[:len(zpName_ip.get())-1] + "ой"
                zpName_vp = zpName_ip.get()[:len(zpName_ip.get())-1] + "у"
                zpName_tp = zpName_ip.get()[:len(zpName_ip.get())-1] + "ой"
            else:
                if letters2 == "ев" or letters2 == "ёв" or letters2 == "ин" or letters2 == "ын" or letters2 == "ов":
                    zpName_rp = zpName_ip.get() + "а"
                    zpName_dp = zpName_ip.get() + "у"
                    zpName_vp = zpName_ip.get() + "а"
                    zpName_tp = zpName_ip.get() + "ым"
                elif letters2 == "ий":
                    zpName_rp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ого"
                    zpName_dp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ому"
                    zpName_vp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ого"
                    zpName_tp = zpName_ip.get()[:len(zpName_ip.get())-2] + "им"
                elif letters2 == "ый":
                    zpName_rp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ого"
                    zpName_dp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ому"
                    zpName_vp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ого"
                    zpName_tp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ым"
                elif letters2 == "ая":
                    zpName_rp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ой"
                    zpName_dp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ой"
                    zpName_vp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ую"
                    zpName_tp = zpName_ip.get()[:len(zpName_ip.get())-2] + "ой"
                else:
                    zpName_rp = zpName_ip.get()
                    zpName_dp = zpName_ip.get()
                    zpName_vp = zpName_ip.get()
                    zpName_tp = zpName_ip.get()

            newDeal = {
                "partCode" : partCode.get(),
                "artCode" : artCode.get(),
                "codeRF_ip" : codeRF_ip,
                "codeRF_rp" : codeRF_rp,
                "codeRF_dp" : codeRF_dp,
                "codeRF_vp" : codeRF_vp,
                "codeRF_tp" : codeRF_tp,
                "codeRF_sh" : codeRF_sh,
                "dateInit" : dateInit.get(),
                "monthInit" : monthInit.get(),
                "numberDt" : numberDt.get(),
                "tpdecl" : tpdecl.get(),
                "company" : {
                        "ul" : ul.get(),
                        "ogrn" : ogrn.get(),
                        "inn" : inn.get(),
                        "kpp" : kpp.get(),
                        "dateRegUl" : dateRegUl.get(),
                        "emailUl" : emailUl.get(),
                        "address" : {
                            "ulIndex" : ulIndex.get(),
                            "ulSubrf": ulSubrf.get(),
                            "ulCity": ulCity.get(),
                            "ulStreetOffice": ulStreetOffice.get()
                        },
                        "actioner" : {
                            "zpPosition" : zpPosition.get(),
                            "zpName_ip" : zpName_ip.get(),
                            "zpName_rp" : zpName_rp,
                            "zpName_dp" : zpName_dp,
                            "zpName_vp" : zpName_vp,
                            "zpName_tp" : zpName_tp
                        }
                    }
                }

            filePointer = open(resourcesProvider.getDealsPath(), 'r', encoding='utf-8')
            existingDeals = json.load(filePointer)
            filePointer.close()
            existingDeals[numberCase.get()] = newDeal
            filePointer = open(resourcesProvider.getDealsPath(), 'w', encoding='utf-8')
            filePointer.write(str(json.dumps(existingDeals, ensure_ascii=False, sort_keys=True, indent=4)))
            filePointer.close()

            messagebox.showinfo("Сохранено", "Добавлено новое дело об АП\n\n10418000-" + numberCase.get() + "/2020\n" + ul.get())
            winEnterWindow.destroy()


    winEnterWindow = Tk()
    winEnterWindow.title("Добавить/Изменить ДАП")
    w = winEnterWindow.winfo_screenwidth()
    h = winEnterWindow.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 255
    h = h - 300
    winEnterWindow.geometry('510x510+{}+{}'.format(w, h))
    winEnterWindow.configure(bg ='#bdf0d4')

    numberCase = StringVar()
    dateInit = StringVar()
    monthInit = StringVar()
    partCode = StringVar()
    artCode = StringVar()
    ul = StringVar()
    ogrn = StringVar()
    inn = StringVar()
    kpp = StringVar()
    dateRegUl = StringVar()
    ulIndex = StringVar()
    ulSubrf = StringVar()
    ulCity = StringVar()
    ulStreetOffice = StringVar()
    zpPosition = StringVar()
    zpName_ip = StringVar()
    emailUl = StringVar()
    numberDt = StringVar()
    tpdecl = IntVar()


    Label(text='10418000-', bg ='#bdf0d4').place(x=10, y=10, height = 20)
    Entry(textvariable=numberCase).place(x=70, y=10, width=50, height = 20)
    Label(text='/2020', bg ='#bdf0d4').place(x=120, y=10, height = 20)

    Label(text='дата возбуждения', bg ='#bdf0d4').place(x=10, y=40, height = 20)
    Entry(textvariable=dateInit).place(x=120, y=40, width=30, height = 20)
    with open(resourcesProvider.getConfigPath(), 'r', encoding='utf-8') as f:
        dapJson = json.load(f)

    listOfMonths = []
    for l in dapJson['months'].keys():
        listOfMonths.append(l)
    monthvozb_ = ttk.Combobox(winEnterWindow, textvariable=monthInit, values = listOfMonths, height = 12)
    monthvozb_['state']='readonly'
    monthvozb_.place(x = 160, y = 40, width=80, height = 20)

    Label(text='2020 года', bg ='#bdf0d4').place(x=240, y=40, height = 20)

    Label(text='часть', bg ='#bdf0d4').place(x=10, y=70, height = 20)
    Entry(textvariable=partCode).place(x=50, y=70, width=30, height = 20)
    Label(text='статьи', bg ='#bdf0d4').place(x=85, y=70, height = 20)
    Entry(textvariable=artCode).place(x=130, y=70, width=60, height = 20)
    Label(text='КоАП РФ', bg ='#bdf0d4').place(x=195, y=70, height = 20)

    Label(text='юридическое лицо', bg ='#bdf0d4').place(x=10, y=100, height = 20)
    Entry(textvariable=ul).place(x=130, y=100, width=370, height = 20)

    Label(text='ОГРН', bg ='#bdf0d4').place(x=10, y=130, height = 20)
    Entry(textvariable=ogrn).place(x=60, y=130, width=150, height = 20)

    Label(text='ИНН', bg ='#bdf0d4').place(x=10, y=160, height = 20)
    Entry(textvariable=inn).place(x=60, y=160, width=150, height = 20)

    Label(text='КПП', bg ='#bdf0d4').place(x=10, y=190, height = 20)
    Entry(textvariable=kpp).place(x=60, y=190, width=150, height = 20)

    Label(text='дата государственной регистрации ЮЛ', bg ='#bdf0d4').place(x=10, y=220, height = 20)
    Entry(textvariable=dateRegUl).place(x=240, y=220, width=90, height = 20)

    Label(text='юридический адрес', bg ='#bdf0d4').place(x=10, y=250, height = 20)
    Entry(textvariable=ulIndex).place(x=130, y=250, width=80, height = 20)
    Entry(textvariable=ulSubrf).place(x=220, y=250, width=280, height = 20)
    Entry(textvariable=ulCity).place(x=10, y=280, width=235, height = 20)
    Entry(textvariable=ulStreetOffice).place(x=255, y=280, width=245, height = 20)

    Label(text='законный представитель', bg ='#bdf0d4').place(x=10, y=310, height = 20)

    listOfPositions = []
    for k in dapJson['actionerPositions'].keys():
        listOfPositions.append(k)
    zpPosition_ = ttk.Combobox(winEnterWindow, textvariable=zpPosition, values = listOfPositions, height = 2)
    zpPosition_['state']='readonly'
    zpPosition_.place(x = 160, y = 310, width=150, height = 20)

    Label(text='инициалы, фамилия', bg ='#bdf0d4').place(x=10, y=340, height = 20)
    Entry(textvariable=zpName_ip).place(x=140, y=340, width=160, height = 20)

    Label(text='электронная почта ЮЛ', bg ='#bdf0d4').place(x=10, y=370, height = 20)
    Entry(textvariable=emailUl).place(x=150, y=370, width=350, height = 20)

    Label(text='№ ДТ', bg ='#bdf0d4').place(x=10, y=400, height = 20)
    Entry(textvariable=numberDt).place(x=50, y=400, width=200, height = 20)

    Radiobutton(text="таможенный представитель", value=1, variable=tpdecl, bg ='#bdf0d4', activebackground = '#bdf0d4').place(x = 10, y = 430, height = 20)
    Radiobutton(text="декларант", value=2, variable=tpdecl, bg ='#bdf0d4', activebackground = '#bdf0d4').place(x = 200, y = 430, height = 20)

    Button(text="Сохранить", command=show_message).place(relx=.5, rely=.95, anchor="c")
    Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")



    winEnterWindow.mainloop()
