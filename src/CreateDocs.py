from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from docxtpl import DocxTemplate

from utils.storage.ResourcesManager import ResourcesProvider


def create_docs(resources_provider: ResourcesProvider, chosen_deal: str, chosen_employee: str):
    def form_docs():
        if box_01.get() == False and box_02.get() == False and box_03.get() == False and box_04.get() == False and \
                        box_05.get() == False and box_06.get() == False and box_07.get() == False and box_08.get() == False and \
                        box_09.get() == False and box_10.get() == False and box_11.get() == False and box_12.get() == False and \
                        box_13.get() == False and box_14.get() == False and box_15.get() == False and box_16.get() == False and \
                        box_17.get() == False and box_18.get() == False and box_19.get() == False and box_20.get() == False and \
                        box_21.get() == False:
            messagebox.showerror("Ошибка", "Выберите документы")
        else:
            context = {"number_case": number_case, "day_init": day_init, "month_init": month_init,
                       "code_part": code_part,
                       "code_art": code_art,
                       "code_full_ip": code_full_ip, "code_full_rp": code_full_rp, "code_full_dp": code_full_dp,
                       "code_full_vp": code_full_vp, "code_full_tp": code_full_tp, "code_full_sh": code_full_sh,
                       "fact_init": fact_init, "fact_resp": fact_resp,
                       "company_name": company_name, "ogrn": ogrn, "inn": inn, "kpp": kpp,
                       "date_reg": date_reg, "index": index, "state": state, "city": city, "street": street,

                       "zp_position": zp_position, "zp_position_ip": zp_position_ip, "zp_position_rp": zp_position_rp,
                       "zp_position_dp": zp_position_dp, "zp_position_vp": zp_position_vp,
                       "zp_position_tp": zp_position_tp,
                       "zp_position_ip_low": zp_position_ip_low, "zp_position_rp_low": zp_position_rp_low,
                       "zp_position_dp_low": zp_position_dp_low, "zp_position_vp_low": zp_position_vp_low,
                       "zp_position_tp_low": zp_position_tp_low,

                       "zp_name_ip": zp_name_ip, "zp_name_rp": zp_name_rp, "zp_name_dp": zp_name_dp,
                       "zp_name_vp": zp_name_vp, "zp_name_tp": zp_name_tp,

                       "company_email": company_email, "number_dt": number_dt,

                       "fiooar_ip": fiooar_ip, "fiooar_rp": fiooar_rp, "fiooar_dp": fiooar_dp, "fiooar_vp": fiooar_vp,
                       "fiooar_tp": fiooar_tp, "doloar_ip": doloar_ip,
                       "doloar_rp": doloar_rp, "doloar_dp": doloar_dp, "doloar_vp": doloar_vp, "doloar_tp": doloar_tp,
                       "doloar_ip_low": doloar_ip_low, "doloar_rp_low": doloar_rp_low, "doloar_dp_low": doloar_dp_low,
                       "doloar_vp_low": doloar_vp_low, "doloar_tp_low": doloar_tp_low, "doloar_ip_sh": doloar_ip_sh,
                       "doloar_rp_sh": doloar_rp_sh, "doloar_dp_sh": doloar_dp_sh, "doloar_vp_sh": doloar_vp_sh,
                       "doloar_tp_sh": doloar_tp_sh, "doloar_ip_sh_low": doloar_ip_sh_low,
                       "doloar_rp_sh_low": doloar_rp_sh_low,
                       "doloar_dp_sh_low": doloar_dp_sh_low, "doloar_vp_sh_low": doloar_vp_sh_low,
                       "doloar_tp_sh_low": doloar_tp_sh_low, "emailOar": emailOar, "gortel": gortel
                       }
            list_of_docs = []

            # готов
            if box_01.get():
                if znt_to_ar_name.get() == '' or day_to_ar.get() == '' or month_to_ar.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_ar_ip = dap_json['signers'][znt_to_ar_name.get()]['znt_ip']
                    doc = DocxTemplate("../templates/01.docx")
                    context.update({"znt_to_ar_ip": znt_to_ar_ip, "znt_to_ar_name_ip": znt_to_ar_name.get(),
                                    "day_to_ar": day_to_ar.get(), "month_to_ar": month_to_ar.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 2.1 РЕШЕНИЕ о передаче дела для проведения АР.docx")
                    list_of_docs.append("Решение о передаче дела для проведения АР")
                    # готов
            if box_02.get():
                if znt_to_ar_name.get() == '' or day_to_ar.get() == '' or month_to_ar.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_ar_rp_low = dap_json['signers'][znt_to_ar_name.get()]['znt_rp_low']
                    znt_to_ar_name_rp = dap_json['signers'][znt_to_ar_name.get()]['rp']
                    doc = DocxTemplate("../templates/02.docx")
                    context.update({"znt_to_ar_rp_low": znt_to_ar_rp_low, "znt_to_ar_name_rp": znt_to_ar_name_rp,
                                    "day_to_ar": day_to_ar.get(), "month_to_ar": month_to_ar.get()})
                    doc.render(context)
                    doc.save(
                        "../buffer/" + number_case + "__ 2.2 ОПРЕДЕЛЕНИЕ о принятии дела к своему проиводству.docx")
                    list_of_docs.append("ОПРЕДЕЛЕНИЕ о принятии дела к своему проиводству")
                    # готов
            if box_03.get():
                if day_istreb.get() == '' or month_istreb.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    month_init_numeral = dap_json['months'][month_init]
                    doc = DocxTemplate("../templates/03.docx")
                    context.update({"day_istreb": day_istreb.get(), "month_istreb": month_istreb.get(),
                                    "month_init_numeral": month_init_numeral})
                    doc.render(context)
                    doc.save(
                        "../buffer/" + number_case + "__ 2.3 ОПРЕДЕЛЕНИЕ об истребовании документов и сведений.docx")
                    list_of_docs.append("ОПРЕДЕЛЕНИЕ об истребовании документов и сведений")
                    # готов
            if box_04.get():
                if day_istreb.get() == '' or month_istreb.get() == '' or day_opros.get() == '' or month_opros.get() == '' \
                        or hour_opros.get() == '' or min_opros.get() == '' or day_protokol1.get() == '' or month_protokol1.get() == '' \
                        or hour_protokol1.get() == '' or min_protokol1.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    doc = DocxTemplate("../templates/04.docx")
                    context.update({"day_istreb": day_istreb.get(), "month_istreb": month_istreb.get(),
                                    "day_opros": day_opros.get(),
                                    "month_opros": month_opros.get(), "hour_opros": hour_opros.get(),
                                    "min_opros": min_opros.get(),
                                    "day_protokol1": day_protokol1.get(), "month_protokol1": month_protokol1.get(),
                                    "hour_protokol1": hour_protokol1.get(), "min_protokol1": min_protokol1.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 2.4 ПОВЕСТКА о явке.docx")
                    list_of_docs.append("ПОВЕСТКА о явке")
                    # готов
            if box_05.get():
                if znt_zapros_name.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_zapros_ip = dap_json['signers'][znt_zapros_name.get()]['znt_ip']
                    rank = dap_json['signers'][znt_zapros_name.get()]['rank']
                    doc = DocxTemplate("../templates/05.docx")
                    context.update(
                        {"znt_zapros_ip": znt_zapros_ip, "znt_zapros_name_ip": znt_zapros_name.get(), "rank": rank})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 2.5 ЗАПРОС в ГИБДД.docx")
                    list_of_docs.append("ЗАПРОС в ГИБДД")
                    # готов
            if box_06.get():
                if znt_zapros_name.get() == '' or day_zapros.get() == '' or month_zapros.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_zapros_ip = dap_json['signers'][znt_zapros_name.get()]['znt_ip']
                    znt_zapros_name_ip_full = dap_json['signers'][znt_zapros_name.get()]['ip_full']
                    rank = dap_json['signers'][znt_zapros_name.get()]['rank']
                    cert_ser = dap_json['signers'][znt_zapros_name.get()]['cert_ser']
                    cert_num = dap_json['signers'][znt_zapros_name.get()]['cert_num']
                    cert_day = dap_json['signers'][znt_zapros_name.get()]['cert_day']
                    cert_month = dap_json['signers'][znt_zapros_name.get()]['cert_month']
                    cert_year = dap_json['signers'][znt_zapros_name.get()]['cert_year']
                    doc1 = DocxTemplate("../templates/06.docx")
                    doc2 = DocxTemplate("../templates/06_1.docx")
                    context.update({"znt_zapros_ip": znt_zapros_ip, "znt_zapros_name_ip": znt_zapros_name.get(),
                                    "znt_zapros_name_ip_full": znt_zapros_name_ip_full, "day_zapros": day_zapros.get(),
                                    "month_zapros": month_zapros.get(), "rank": rank, "cert_ser": cert_ser,
                                    "cert_num": cert_num, "cert_day": cert_day, "cert_month": cert_month,
                                    "cert_year": cert_year})
                    doc1.render(context)
                    doc2.render(context)
                    doc1.save("../buffer/" + number_case + "__ 2.6 ЗАПРОС в РОСРЕЕСТР.docx")
                    doc2.save("../buffer/" + number_case + "__ 2.6 Приложение - ЗАПРОС в РОСРЕЕСТР.docx")
                    list_of_docs.append("ЗАПРОС в Росреестр (+ приложение)")

            if box_07.get():
                if day_protokol2.get() == '' or month_protokol2.get() == '' or hour_protokol2.get() == '' or min_protokol2.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    doc = DocxTemplate("../templates/07.docx")
                    context.update({"day_protokol2": day_protokol2.get(), "month_protokol2": month_protokol2.get(),
                                    "hour_protokol2": hour_protokol2.get(), "min_protokol2": min_protokol2.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 2.7 ТЕЛЕГРАММА - вызов на протокол.docx")
                    list_of_docs.append("ТЕЛЕГРАММА - вызов на протокол")
                    # готов
            if box_08.get():
                if day_protokol2.get() == '' or month_protokol2.get() == '' or hour_protokol2.get() == '' or min_protokol2.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    doc = DocxTemplate("../templates/08.docx")
                    context.update({"day_protokol2": day_protokol2.get(), "month_protokol2": month_protokol2.get(),
                                    "hour_protokol2": hour_protokol2.get(), "min_protokol2": min_protokol2.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 2.8 УВЕДОМЛЕНИЕ - вызов на протокол.docx")
                    list_of_docs.append("УВЕДОМЛЕНИЕ - вызов на протокол")

                    # if box_09.get():
                    # готов
            if box_10.get():
                if day_protokol3.get() == '' or month_protokol3.get() == '' or day_to_rassm.get() == '' or month_to_rassm.get() == '' \
                        or znt_to_rassm_name.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_rassm_ip = dap_json['signers'][znt_to_rassm_name.get()]['znt_ip']
                    znt_to_rassm_dp = dap_json['signers'][znt_to_rassm_name.get()]['znt_dp']
                    znt_to_rassm_name_dp = dap_json['signers'][znt_to_rassm_name.get()]['dp']
                    rank = dap_json['signers'][znt_to_rassm_name.get()]['rank']
                    rank_dp = dap_json['signers'][znt_to_rassm_name.get()]['rank_dp']
                    doc = DocxTemplate("../templates/10.docx")
                    context.update({"day_protokol3": day_protokol3.get(), "month_protokol3": month_protokol3.get(),
                                    "day_to_rassm": day_to_rassm.get(), "month_to_rassm": month_to_rassm.get(),
                                    "znt_to_rassm_ip": znt_to_rassm_ip, "znt_to_rassm_dp": znt_to_rassm_dp,
                                    "znt_to_rassm_name_ip": znt_to_rassm_name.get(),
                                    "znt_to_rassm_name_dp": znt_to_rassm_name_dp,
                                    "rank": rank, "rank_dp": rank_dp})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 3.1 РАПОРТ об окончании адм.расследования.docx")
                    list_of_docs.append("РАПОРТ об окончании адм.расследования")
                    # готов
            if box_11.get():
                if znt_to_rassm_name.get() == '' or day_to_rassm.get() == '' or month_to_rassm.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_rassm_ip = dap_json['signers'][znt_to_rassm_name.get()]['znt_ip']
                    rank = dap_json['signers'][znt_to_rassm_name.get()]['rank']
                    doc = DocxTemplate("../templates/11.docx")
                    context.update({"znt_to_rassm_ip": znt_to_rassm_ip, "znt_to_rassm_name_ip": znt_to_rassm_name.get(),
                                    "rank": rank,
                                    "day_to_rassm": day_to_rassm.get(), "month_to_rassm": month_to_rassm.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 3.2 СПРАВКА об отсутствии издержек.docx")
                    list_of_docs.append("СПРАВКА об отсутствии издержек")

                    # if box_12.get():
                    # готов
            if box_13.get():
                if znt_to_rassm_name.get() == '' or day_rassm1.get() == '' or month_rassm1.get() == '' or hour_rassm1.get() == '' \
                        or min_rassm1.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_rassm_ip = dap_json['signers'][znt_to_rassm_name.get()]['znt_ip']
                    doc = DocxTemplate("../templates/13.docx")
                    context.update({"znt_to_rassm_ip": znt_to_rassm_ip, "znt_to_rassm_name_ip": znt_to_rassm_name.get(),
                                    "day_rassm1": day_rassm1.get(), "month_rassm1": month_rassm1.get(),
                                    "hour_rassm1": hour_rassm1.get(),
                                    "min_rassm1": min_rassm1.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 3.4 ПИСЬМО - вызов на рассмотрение.docx")
                    list_of_docs.append("ПИСЬМО - вызов на рассмотрение")
                    # готов
            if box_14.get():
                if znt_to_rassm_name.get() == '' or day_rassm1.get() == '' or month_rassm1.get() == '' or hour_rassm1.get() == '' \
                        or min_rassm1.get() == '':
                    messagebox.showerror("Ошибка", "Заполните все поля")
                else:
                    znt_to_rassm_ip = dap_json['signers'][znt_to_rassm_name.get()]['znt_ip']
                    doc = DocxTemplate("../templates/14.docx")
                    context.update({"znt_to_rassm_ip": znt_to_rassm_ip, "znt_to_rassm_name_ip": znt_to_rassm_name.get(),
                                    "day_rassm1": day_rassm1.get(), "month_rassm1": month_rassm1.get(),
                                    "hour_rassm1": hour_rassm1.get(),
                                    "min_rassm1": min_rassm1.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 3.5 ТЕЛЕГРАММА - вызов на рассмотрение.docx")
                    list_of_docs.append("ТЕЛЕГРАММА - вызов на рассмотрение")

            if box_15.get():
                znt_otlozh_ip = dap_json['signers'][znt_otlozh_name.get()]['znt_ip']
                doc = DocxTemplate("../templates/15.docx")
                context.update({"znt_otlozh_ip": znt_otlozh_ip, "zntOtlozhName_ip": znt_otlozh_name.get(),
                                "day_otlozh": day_otlozh.get(), "month_otlozh": month_otlozh.get()})
                doc.render(context)
                doc.save("../buffer/" + number_case + "__ 3.6 ОПРЕДЕЛЕНИЕ об отложении.docx")

            '''if box_16.get():
            if box_17.get():
            if box_18.get():
            if box_19.get():'''
            # готов
            if box_20.get():
                if day_rassm3.get() == '' or month_rassm3.get() == '':
                    messagebox.showerror("Ошибка", "Заполните поля о дате рассмотрения")
                else:
                    doc = DocxTemplate("../templates/20.docx")
                    context.update({"day_rassm3": day_rassm3.get(), "month_rassm3": month_rassm3.get()})
                    doc.render(context)
                    doc.save("../buffer/" + number_case + "__ 3.11 БИРКА дела об АП (мини).docx")
                    list_of_docs.append("БИРКА дела об АП (мини)")
                    # готов
            if box_21.get():
                doc = DocxTemplate("../templates/21.docx")
                doc.render(context)
                doc.save("../buffer/" + number_case + "__ 3.12 ОПИСЬ по делу об АП.docx")
                list_of_docs.append("ОПИСЬ")

            list_of_docs_splitted = ('\n'.join(list_of_docs))

            if list_of_docs == []:
                messagebox.showerror("Ошибка", "Документы не сформированы")
            else:
                messagebox.showinfo("Сформировано",
                                    "Сформировано по делу об АП\n10418000-" + number_case + "/2020:\n\n" + list_of_docs_splitted)

    class Scrollable(Frame):

        def __init__(self, frame):
            scrollbar = Scrollbar(frame)
            scrollbar.pack(side=RIGHT, fill=Y, expand=False)
            self.canvas = Canvas(frame, yscrollcommand=scrollbar.set)
            self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
            scrollbar.config(command=self.canvas.yview)
            self.canvas.bind('<Configure>', self.__fill_canvas)
            Frame.__init__(self, frame)
            self.windows_item = self.canvas.create_window(0, 0, window=self, anchor=NW)
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        def _on_mousewheel(self, event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def __fill_canvas(self, event):
            canvas_width = event.width
            self.canvas.itemconfig(self.windows_item, width=canvas_width)

        def update(self):
            self.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))

    winChooseDocs = Tk()
    winChooseDocs.title("Выбор документов для ДАП 10418000-" + chosen_deal + "/2020")
    w = winChooseDocs.winfo_screenwidth()
    h = winChooseDocs.winfo_screenheight()
    w = w // 2
    w = w // 2
    h = h // 2
    w = w - 0
    h = h - 470
    winChooseDocs.geometry('500x850+{}+{}'.format(w, h))

    body = Frame(winChooseDocs)
    body.pack(fill='both', expand=True)

    scrollable_body = Scrollable(body)

    box_01, box_02, box_03, box_04, box_05, box_06, box_07, box_08, box_09, box_10, box_11, box_12, box_13, box_14, \
    box_15, box_16, box_17, box_18, box_19, box_20, box_21 = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), \
                                                             BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), \
                                                             BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

    znt_to_ar_name, znt_zapros_name, znt_to_rassm_name, znt_otlozh_name, znt_rassm_name, day_to_ar, month_to_ar, day_istreb, month_istreb, \
    day_zapros, month_zapros, day_opros, month_opros, hour_opros, min_opros, day_protokol1, month_protokol1, hour_protokol1, min_protokol1, \
    day_protokol2, month_protokol2, hour_protokol2, min_protokol2, day_protokol3, month_protokol3, day_rassm1, month_rassm1, \
    hour_rassm1, min_rassm1, day_rassm2, month_rassm2, hour_rassm2, min_rassm2, day_rassm3, month_rassm3, hour_rassm3, min_rassm3, \
    day_to_rassm, month_to_rassm, day_otlozh, month_otlozh, fact_init, fact_resp = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
                                                                                   StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
                                                                                   StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
                                                                                   StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
                                                                                   StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), \
                                                                                   StringVar(), StringVar()

    dap_json = resources_provider.load_config()
    listOfPer = []
    for l in dap_json['signers'].keys():
        listOfPer.append(l)
    listOfMonths = []
    for l in dap_json['months'].keys():
        listOfMonths.append(l)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeToAR = LabelFrame(scrollable_body,
                                text="Передача дела об АП для проведения административного расследования", fg="blue",
                                bg="#37faac", labelanchor="n", padx=5, pady=5)
    labelframeToAR.pack(fill="x", expand="yes")
    Checkbutton(labelframeToAR, text="Решение о передаче дела об АП", variable=box_01, bg="#37faac",
                activebackground="#37faac").pack(anchor="w")
    Checkbutton(labelframeToAR, text="Определение о принятии дела к своему производству", variable=box_02, bg="#37faac",
                activebackground="#37faac").pack(anchor="w")
    frame1 = Frame(labelframeToAR, bg="#37faac")
    Label(frame1, text="дата передачи", bg="#37faac").pack(side=LEFT)
    Entry(frame1, textvariable=day_to_ar, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame1, textvariable=month_to_ar, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame1, text="2020 года", bg="#37faac").pack(side=LEFT, padx=3, pady=1)
    frame1.pack(anchor='w')
    frame2 = Frame(labelframeToAR, bg="#37faac")
    Label(frame2, text="лицо, передающее", bg="#37faac").pack(side=LEFT)
    ttk.Combobox(frame2, textvariable=znt_to_ar_name, values=listOfPer, height=2, width=15, state='readonly') \
        .pack(side=LEFT, pady=1)
    frame2.pack(anchor='w')
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros1 = LabelFrame(scrollable_body, text="Запросы в ходе административного расследования", fg="blue",
                                   bg="#7affca", labelanchor="n", padx=5, pady=5)
    labelframeZapros1.pack(fill="x", expand="yes")
    Checkbutton(labelframeZapros1, text="Определение об истребовании документов и сведений", variable=box_03,
                bg="#7affca", activebackground="#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros1, text="Повестка о явке", variable=box_04, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    frame3 = Frame(labelframeZapros1, bg="#7affca")
    Label(frame3, text="дата направления", bg="#7affca").pack(side=LEFT)
    Entry(frame3, textvariable=day_istreb, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame3, textvariable=month_istreb, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame3, text="2020 года", bg="#7affca").pack(side=LEFT, padx=3, pady=1)
    frame3.pack(anchor='w')

    frame21 = Frame(labelframeZapros1, bg="#7affca")
    Label(frame21, text="дата опроса законного представителя", bg="#7affca").pack(side=LEFT)
    Entry(frame21, textvariable=day_opros, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame21, textvariable=month_opros, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame21, text="2020 года", bg="#7affca").pack(side=LEFT, padx=3, pady=1)
    Entry(frame21, textvariable=hour_opros, width=3).pack(side=LEFT, padx=1, pady=1)
    Label(frame21, text=":", bg="#7affca").pack(side=LEFT)
    Entry(frame21, textvariable=min_opros, width=3).pack(side=LEFT, padx=1, pady=1)
    frame21.pack(anchor='w')

    frame22 = Frame(labelframeZapros1, bg="#7affca")
    Label(frame22, text="дата протокола", bg="#7affca").pack(side=LEFT)
    Entry(frame22, textvariable=day_protokol1, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame22, textvariable=month_protokol1, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame22, text="2020 года", bg="#7affca").pack(side=LEFT, padx=3, pady=1)
    Entry(frame22, textvariable=hour_protokol1, width=3).pack(side=LEFT, padx=1)
    Label(frame22, text=":", bg="#7affca").pack(side=LEFT)
    Entry(frame22, textvariable=min_protokol1, width=3).pack(side=LEFT, padx=1)
    frame22.pack(anchor='w')
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros2 = LabelFrame(scrollable_body, bg="#7affca", padx=5, pady=5)
    labelframeZapros2.pack(fill="x", expand="yes")
    Checkbutton(labelframeZapros2, text="Запрос в ГИБДД", variable=box_05, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros2, text="Запрос в Росреестр", variable=box_06, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    frame4 = Frame(labelframeZapros2, bg="#7affca")
    Label(frame4, text="дата запроса", bg="#7affca").pack(side=LEFT)
    Entry(frame4, textvariable=day_zapros, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame4, textvariable=month_zapros, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame4, text="2020 года", bg="#7affca").pack(side=LEFT, padx=3, pady=1)
    frame4.pack(anchor='w')
    frame5 = Frame(labelframeZapros2, bg="#7affca")
    Label(frame5, text="лицо, направляющее", bg="#7affca").pack(side=LEFT)
    ttk.Combobox(frame5, textvariable=znt_zapros_name, values=listOfPer, height=2, state='readonly') \
        .pack(side=LEFT, pady=1)
    frame5.pack(anchor='w')
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeZapros3 = LabelFrame(scrollable_body, bg="#7affca", padx=5, pady=5)
    labelframeZapros3.pack(fill="x", expand="yes")
    Checkbutton(labelframeZapros3, text="Телеграмма - вызов на протокол", variable=box_07, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros3, text="Уведомление - вызов на протокол", variable=box_08, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    Checkbutton(labelframeZapros3, text="Шаблон протокола об АП", variable=box_09, bg="#7affca",
                activebackground="#7affca").pack(anchor="w")
    frame6 = Frame(labelframeZapros3, bg="#7affca")
    Label(frame6, text="дата протокола", bg="#7affca").pack(side=LEFT)
    Entry(frame6, textvariable=day_protokol2, width=5).pack(side=LEFT, padx=3)
    ttk.Combobox(frame6, textvariable=month_protokol2, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3)
    Label(frame6, text="2020 года", bg="#7affca").pack(side=LEFT, padx=3)
    Entry(frame6, textvariable=hour_protokol2, width=3).pack(side=LEFT, padx=1)
    Label(frame6, text=":", bg="#7affca").pack(side=LEFT)
    Entry(frame6, textvariable=min_protokol2, width=3).pack(side=LEFT, padx=1)
    frame6.pack(side=LEFT)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeToRassm = LabelFrame(scrollable_body, text="Передача дела об АП на рассмотрение", fg="blue", bg="#C1F1B1",
                                   labelanchor="n", padx=5, pady=5)
    labelframeToRassm.pack(fill="x", expand="yes")
    Checkbutton(labelframeToRassm, text="Рапорт об окончании адм.расследования", variable=box_10, bg="#C1F1B1",
                activebackground="#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Справка об отсутствии издержек", variable=box_11, bg="#C1F1B1",
                activebackground="#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Определение о назначении времени и места рассмотрения дела об АП",
                variable=box_12, bg="#C1F1B1", activebackground="#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Письмо - вызов на рассмотрерние", variable=box_13, bg="#C1F1B1",
                activebackground="#C1F1B1").pack(anchor="w")
    Checkbutton(labelframeToRassm, text="Телеграмма - вызов на рассмотрение", variable=box_14, bg="#C1F1B1",
                activebackground="#C1F1B1").pack(anchor="w")

    frame23 = Frame(labelframeToRassm, bg="#C1F1B1")
    Label(frame23, text="дата протокола", bg="#C1F1B1").pack(side=LEFT)
    Entry(frame23, textvariable=day_protokol3, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame23, textvariable=month_protokol3, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame23, text="2020 года", bg="#C1F1B1").pack(side=LEFT, padx=3, pady=1)
    frame23.pack(anchor='w')

    frame7 = Frame(labelframeToRassm, bg="#C1F1B1")
    Label(frame7, text="дата передачи", bg="#C1F1B1").pack(side=LEFT)
    Entry(frame7, textvariable=day_to_rassm, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame7, textvariable=month_to_rassm, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame7, text="2020 года", bg="#C1F1B1").pack(side=LEFT, padx=3, pady=1)
    frame7.pack(anchor='w')

    frame24 = Frame(labelframeToRassm, bg="#C1F1B1")
    Label(frame24, text="дата рассмотрения", bg="#C1F1B1").pack(side=LEFT)
    Entry(frame24, textvariable=day_rassm1, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame24, textvariable=month_rassm1, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame24, text="2020 года", bg="#C1F1B1").pack(side=LEFT, padx=3, pady=1)
    Entry(frame24, textvariable=hour_rassm1, width=3).pack(side=LEFT, padx=1, pady=1)
    Label(frame24, text=":", bg="#C1F1B1").pack(side=LEFT)
    Entry(frame24, textvariable=min_rassm1, width=3).pack(side=LEFT, padx=1, pady=1)
    frame24.pack(anchor='w')

    frame8 = Frame(labelframeToRassm, bg="#C1F1B1")
    Label(frame8, text="лицо, принимающее", bg="#C1F1B1").pack(side=LEFT)
    ttk.Combobox(frame8, textvariable=znt_to_rassm_name, values=listOfPer, height=2, state='readonly') \
        .pack(side=LEFT, pady=1)
    frame8.pack(anchor='w')
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframeOtlozh = LabelFrame(scrollable_body, text="Отложение рассмотрения дела об АП", fg="blue", bg="#D7FFD7",
                                  labelanchor="n", padx=5, pady=5)
    labelframeOtlozh.pack(fill="x", expand="yes")
    Checkbutton(labelframeOtlozh, text="Определение об отложении времени и места рассмотрения дела об АП",
                variable=box_15, bg="#D7FFD7", activebackground="#D7FFD7").pack(anchor="w")
    Checkbutton(labelframeOtlozh, text="Определение о продлении срока рассмотрения дела об АП", variable=box_16,
                bg="#D7FFD7", activebackground="#D7FFD7").pack(anchor="w")
    frame9 = Frame(labelframeOtlozh, bg="#D7FFD7")
    Label(frame9, text="дата отложения", bg="#D7FFD7").pack(side=LEFT)
    Entry(frame9, textvariable=day_otlozh, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame9, textvariable=month_otlozh, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame9, text="2020 года", bg="#D7FFD7").pack(side=LEFT, padx=3, pady=1)
    frame9.pack(anchor='w')

    frame25 = Frame(labelframeOtlozh, bg="#D7FFD7")
    Label(frame25, text="новая дата рассмотрения", bg="#D7FFD7").pack(side=LEFT)
    Entry(frame25, textvariable=day_rassm2, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame25, textvariable=month_rassm2, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame25, text="2020 года", bg="#D7FFD7").pack(side=LEFT, padx=3, pady=1)
    Entry(frame25, textvariable=hour_rassm2, width=3).pack(side=LEFT, padx=1, pady=1)
    Label(frame25, text=":", bg="#D7FFD7").pack(side=LEFT)
    Entry(frame25, textvariable=min_rassm2, width=3).pack(side=LEFT, padx=1, pady=1)
    frame25.pack(anchor='w')

    frame10 = Frame(labelframeOtlozh, bg="#D7FFD7")
    Label(frame10, text="лицо, откладывающее", bg="#D7FFD7").pack(side=LEFT)
    ttk.Combobox(frame10, textvariable=znt_otlozh_name, values=listOfPer, height=2, state='readonly') \
        .pack(side=LEFT, pady=1)
    frame10.pack(anchor='w')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    labelframePost = LabelFrame(scrollable_body, text="Рассмотрение дела об АП", fg="blue", bg="#ebfff7",
                                labelanchor="n", padx=5, pady=5)
    labelframePost.pack(fill="x", expand="yes")
    Checkbutton(labelframePost, text="Шаблон постановления по делу об АП", variable=box_17, bg="#ebfff7",
                activebackground="#ebfff7").pack(anchor="w")
    Checkbutton(labelframePost, text="Представление об устранении причин и условий", variable=box_18, bg="#ebfff7",
                activebackground="#ebfff7").pack(anchor="w")
    frame11 = Frame(labelframePost, bg="#ebfff7")
    Label(frame11, text="дата рассмотрения", bg="#ebfff7").pack(side=LEFT)
    Entry(frame11, textvariable=day_rassm3, width=5).pack(side=LEFT, padx=3, pady=1)
    ttk.Combobox(frame11, textvariable=month_rassm3, values=listOfMonths, height=12, width=10, state='readonly') \
        .pack(side=LEFT, padx=3, pady=1)
    Label(frame11, text="2020 года", bg="#ebfff7").pack(side=LEFT, padx=3, pady=1)
    Entry(frame11, textvariable=hour_rassm3, width=3).pack(side=LEFT, padx=1, pady=1)
    Label(frame11, text=":", bg="#ebfff7").pack(side=LEFT)
    Entry(frame11, textvariable=min_rassm3, width=3).pack(side=LEFT, padx=1, pady=1)

    frame11.pack(anchor='w')
    frame12 = Frame(labelframePost, bg="#ebfff7")
    Label(frame12, text="лицо, рассматривающее", bg="#ebfff7").pack(side=LEFT, pady=1)
    ttk.Combobox(frame12, textvariable=znt_rassm_name, values=listOfPer, height=2, state='readonly') \
        .pack(side=LEFT, pady=1)
    frame12.pack(anchor='w')
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    frame13 = Frame(scrollable_body)
    Checkbutton(frame13, text="Бирка дела об АП", variable=box_19).pack(padx=7, anchor="w")
    Checkbutton(frame13, text="Бирка дела об АП (мини)", variable=box_20).pack(padx=7, anchor="w")
    Checkbutton(frame13, text="Опись", variable=box_21).pack(padx=7, anchor="w")
    frame13.pack(side=LEFT)

    Button(text="Сформировать", command=form_docs).pack(pady=10)

    deals_json = resources_provider.load_deals()

    number_case = chosen_deal
    code_art = deals_json[number_case]['code_art']
    code_part = deals_json[number_case]['code_part']

    if code_part == '-':
        code_full_ip = "статья " + code_art
        code_full_rp = "статьи " + code_art
        code_full_dp = "статье " + code_art
        code_full_vp = "статью " + code_art
        code_full_tp = "статьей " + code_art
        code_full_sh = "ст. " + code_art
    else:
        code_full_ip = "часть " + code_part + " статьи " + code_art
        code_full_rp = "части " + code_part + " статьи " + code_art
        code_full_dp = "части " + code_part + " статьи " + code_art
        code_full_vp = "часть " + code_part + " статьи " + code_art
        code_full_tp = "частью " + code_part + " статьи " + code_art
        code_full_sh = "ч. " + code_part + " ст. " + code_art
    if code_full_sh == "ч. 1 ст. 16.2":
        fact_init = "недекларирования по установленной форме товаров, подлежащих таможенному декларированию, " \
                    "выявленного в ходе таможенного таможенного контроля"
        fact_resp = "заявление сведений о товарах"
    elif code_full_sh == "ч. 2 ст. 16.2":
        fact_init = "заявления при таможенном декларировании товаров недостоверных сведений о товарах (о классификационном коде " \
                    "по единой Товарной номенклатуре внешнеэкономической деятельности Евразийского экономического союза, сопряженное " \
                    "с заявлением при описании товаров неполных и(или) недостоверных сведений об их свойствах, характирестиках, " \
                    "влияющих на их классификацию, о стране происхождения, о таможенной стоимости), если такие сведения послужили " \
                    "или могли послужить основанием для освобождения от уплаты таможенных пошлин, налогов или для занижения их размера"
        fact_resp = "заявление сведений о товарах"
    elif code_full_sh == "ч. 3 ст. 16.2":
        fact_init = "представления при таможенном декларировании товаров недействительных документов, если такие документы " \
                    "послужили или могли послужить основанием для несоблюдения установленных международными договорами " \
                    "государств - членов Евразийского экономического союза, решениями Евразийской экономической комиссии, " \
                    "нормативными правовыми актами Российской Федерации запретов и ограничений"
        fact_resp = "заявление сведений о товарах"
    elif code_full_sh == "ст. 16.3":
        fact_init = "несоблюдения установленных международными договорами государств-членов Евразийского экономического союза, " \
                    "решениями Евразийской экономической комиссии, нормативными правовыми актами Российской Федерации запретов и " \
                    "ограничений на ввоз товаров на таможенную территорию Евразийского экономического союза"
        fact_resp = "соблюдение запретов и ограничений"
    else:
        fact_init = "XXXXX"
        fact_resp = "XXXXX"

    day_init = deals_json[number_case]['day_init']
    date_reg = deals_json[number_case]['company']['date_reg']
    company_email = deals_json[number_case]['company']['email']
    inn = deals_json[number_case]['company']['inn']
    kpp = deals_json[number_case]['company']['kpp']
    month_init = deals_json[number_case]['month_init']
    number_dt = deals_json[number_case]['number_dt']
    ogrn = deals_json[number_case]['company']['ogrn']

    company_name = deals_json[number_case]['company']['name']
    city = deals_json[number_case]['company']['address']['city']
    index = deals_json[number_case]['company']['address']['index']
    street = deals_json[number_case]['company']['address']['street']
    state = deals_json[number_case]['company']['address']['state']

    zp_name_ip = deals_json[number_case]['company']['representative']['name']
    letters2 = zp_name_ip[len(zp_name_ip) - 2:]
    letters3 = zp_name_ip[len(zp_name_ip) - 3:]
    if letters3 == "ева" or letters3 == "ёва" or letters3 == "ина" or letters3 == "ына" or letters3 == "ова":
        zp_name_rp = zp_name_ip[:len(zp_name_ip) - 1] + "ой"
        zp_name_dp = zp_name_ip[:len(zp_name_ip) - 1] + "ой"
        zp_name_vp = zp_name_ip[:len(zp_name_ip) - 1] + "у"
        zp_name_tp = zp_name_ip[:len(zp_name_ip) - 1] + "ой"
    else:
        if letters2 == "ев" or letters2 == "ёв" or letters2 == "ин" or letters2 == "ын" or letters2 == "ов":
            zp_name_rp = zp_name_ip + "а"
            zp_name_dp = zp_name_ip + "у"
            zp_name_vp = zp_name_ip + "а"
            zp_name_tp = zp_name_ip + "ым"
        elif letters2 == "ий":
            zp_name_rp = zp_name_ip[:len(zp_name_ip) - 2] + "ого"
            zp_name_dp = zp_name_ip[:len(zp_name_ip) - 2] + "ому"
            zp_name_vp = zp_name_ip[:len(zp_name_ip) - 2] + "ого"
            zp_name_tp = zp_name_ip[:len(zp_name_ip) - 2] + "им"
        elif letters2 == "ый":
            zp_name_rp = zp_name_ip[:len(zp_name_ip) - 2] + "ого"
            zp_name_dp = zp_name_ip[:len(zp_name_ip) - 2] + "ому"
            zp_name_vp = zp_name_ip[:len(zp_name_ip) - 2] + "ого"
            zp_name_tp = zp_name_ip[:len(zp_name_ip) - 2] + "ым"
        elif letters2 == "ая":
            zp_name_rp = zp_name_ip[:len(zp_name_ip) - 2] + "ой"
            zp_name_dp = zp_name_ip[:len(zp_name_ip) - 2] + "ой"
            zp_name_vp = zp_name_ip[:len(zp_name_ip) - 2] + "ую"
            zp_name_tp = zp_name_ip[:len(zp_name_ip) - 2] + "ой"
        else:
            zp_name_rp = zp_name_ip
            zp_name_dp = zp_name_ip
            zp_name_vp = zp_name_ip
            zp_name_tp = zp_name_ip

    zp_position = deals_json[number_case]['company']['representative']['position']
    zp_position_ip = dap_json['actionerPositions'][zp_position]['ip']
    zp_position_rp = dap_json['actionerPositions'][zp_position]['rp']
    zp_position_dp = dap_json['actionerPositions'][zp_position]['dp']
    zp_position_vp = dap_json['actionerPositions'][zp_position]['vp']
    zp_position_tp = dap_json['actionerPositions'][zp_position]['tp']
    zp_position_ip_low = dap_json['actionerPositions'][zp_position]['ip_low']
    zp_position_rp_low = dap_json['actionerPositions'][zp_position]['rp_low']
    zp_position_dp_low = dap_json['actionerPositions'][zp_position]['dp_low']
    zp_position_vp_low = dap_json['actionerPositions'][zp_position]['vp_low']
    zp_position_tp_low = dap_json['actionerPositions'][zp_position]['tp_low']

    employeeOar = chosen_employee

    fiooar_ip = dap_json['employeesOar'][employeeOar]['fiooar_ip']
    fiooar_rp = dap_json['employeesOar'][employeeOar]['fiooar_rp']
    fiooar_dp = dap_json['employeesOar'][employeeOar]['fiooar_dp']
    fiooar_vp = dap_json['employeesOar'][employeeOar]['fiooar_vp']
    fiooar_tp = dap_json['employeesOar'][employeeOar]['fiooar_tp']
    doloar_ip = dap_json['employeesOar'][employeeOar]['doloar_ip']
    doloar_rp = dap_json['employeesOar'][employeeOar]['doloar_rp']
    doloar_dp = dap_json['employeesOar'][employeeOar]['doloar_dp']
    doloar_vp = dap_json['employeesOar'][employeeOar]['doloar_vp']
    doloar_tp = dap_json['employeesOar'][employeeOar]['doloar_tp']
    doloar_ip_low = dap_json['employeesOar'][employeeOar]['doloar_ip_low']
    doloar_rp_low = dap_json['employeesOar'][employeeOar]['doloar_rp_low']
    doloar_dp_low = dap_json['employeesOar'][employeeOar]['doloar_dp_low']
    doloar_vp_low = dap_json['employeesOar'][employeeOar]['doloar_vp_low']
    doloar_tp_low = dap_json['employeesOar'][employeeOar]['doloar_tp_low']
    doloar_ip_sh = dap_json['employeesOar'][employeeOar]['doloar_ip_sh']
    doloar_rp_sh = dap_json['employeesOar'][employeeOar]['doloar_rp_sh']
    doloar_dp_sh = dap_json['employeesOar'][employeeOar]['doloar_dp_sh']
    doloar_vp_sh = dap_json['employeesOar'][employeeOar]['doloar_vp_sh']
    doloar_tp_sh = dap_json['employeesOar'][employeeOar]['doloar_tp_sh']
    doloar_ip_sh_low = dap_json['employeesOar'][employeeOar]['doloar_ip_sh_low']
    doloar_rp_sh_low = dap_json['employeesOar'][employeeOar]['doloar_rp_sh_low']
    doloar_dp_sh_low = dap_json['employeesOar'][employeeOar]['doloar_dp_sh_low']
    doloar_vp_sh_low = dap_json['employeesOar'][employeeOar]['doloar_vp_sh_low']
    doloar_tp_sh_low = dap_json['employeesOar'][employeeOar]['doloar_tp_sh_low']
    emailOar = dap_json['employeesOar'][employeeOar]['emailOar']
    gortel = dap_json['employeesOar'][employeeOar]['gortel']

    scrollable_body.update()
    winChooseDocs.focus_force()
    winChooseDocs.attributes('-topmost', True)
    winChooseDocs.mainloop()
