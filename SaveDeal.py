from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json

def show_message():
    if number.get() == '' or ul.get() == '':
        messagebox.showerror("Ошибка", "Заполните все поля")
    else:
        messagebox.showinfo("Сохранено", "Сохранено дело об АП\n\n10418000-" + number.get() + "/2020\n" + ul.get())
        winEnterWindow.destroy()
def close_window():
    winEnterWindow.destroy()

winEnterWindow = Tk()
winEnterWindow.title("Добавить/Изменить ДАП")
w = winEnterWindow.winfo_screenwidth()
h = winEnterWindow.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 255
h = h - 255
winEnterWindow.geometry('510x510+{}+{}'.format(w, h))
winEnterWindow.configure(bg ='#bdf0d4')

number = StringVar()
datevozb = StringVar()
monthvozb = StringVar()
chkoap = StringVar()
stkoap = StringVar()
ul = StringVar()
ogrn = StringVar()
inn = StringVar()
kpp = StringVar()
dateul = StringVar()
ad_index = StringVar()
subrf = StringVar()
naspunkt = StringVar()
ulitsadom = StringVar()
zpPosition = StringVar()
zpName_ip = StringVar()
emailul = StringVar()
dt = StringVar()
tpdecl = IntVar()

Label(text='10418000-', bg ='#bdf0d4').place(x=10, y=10, height = 20)
Entry(textvariable=number).place(x=70, y=10, width=50, height = 20)
Label(text='/2020', bg ='#bdf0d4').place(x=120, y=10, height = 20)

Label(text='дата возбуждения', bg ='#bdf0d4').place(x=10, y=40, height = 20)
Entry(textvariable=datevozb).place(x=120, y=40, width=30, height = 20)
with open('dap.json', 'r', encoding='utf-8') as f:
    dapJson = json.load(f)
listOfMonths = []
for l in dapJson['months'].keys():
    listOfMonths.append(l)
monthvozb_ = ttk.Combobox(winEnterWindow, textvariable=monthvozb, values = listOfMonths, height = 12)
monthvozb_['state']='readonly'
monthvozb_.place(x = 160, y = 40, width=80, height = 20)

Label(text='2020 года', bg ='#bdf0d4').place(x=240, y=40, height = 20)

Label(text='часть', bg ='#bdf0d4').place(x=10, y=70, height = 20)
Entry(textvariable=chkoap).place(x=50, y=70, width=30, height = 20)
Label(text='статьи', bg ='#bdf0d4').place(x=85, y=70, height = 20)
Entry(textvariable=stkoap).place(x=130, y=70, width=60, height = 20)
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
Entry(textvariable=dateul).place(x=240, y=220, width=90, height = 20)

Label(text='юридический адрес', bg ='#bdf0d4').place(x=10, y=250, height = 20)
Entry(textvariable=ad_index).place(x=130, y=250, width=80, height = 20)
Entry(textvariable=subrf).place(x=220, y=250, width=280, height = 20)
Entry(textvariable=naspunkt).place(x=10, y=280, width=235, height = 20)
Entry(textvariable=ulitsadom).place(x=255, y=280, width=245, height = 20)

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
Entry(textvariable=emailul).place(x=150, y=370, width=350, height = 20)

Label(text='№ ДТ', bg ='#bdf0d4').place(x=10, y=400, height = 20)
Entry(textvariable=dt).place(x=50, y=400, width=200, height = 20)

Radiobutton(text="таможенный представитель", value=1, variable=tpdecl, bg ='#bdf0d4', activebackground = '#bdf0d4').place(x = 10, y = 430, height = 20)
Radiobutton(text="декларант", value=2, variable=tpdecl, bg ='#bdf0d4', activebackground = '#bdf0d4').place(x = 200, y = 430, height = 20)

saveButtonEnterWindow = Button(text="Сохранить", command=show_message).place(relx=.5, rely=.95, anchor="c")
cancelButtonEnterWindow = Button(text="Отмена", command=close_window).place(relx=.97, rely=.95, anchor="e")

winEnterWindow.mainloop()