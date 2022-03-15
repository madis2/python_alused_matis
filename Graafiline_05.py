# Graafiline 05
# Matis Russi
# IT-21
# 15.03.2022

# Moodulid

from tkinter import *

# Akna seaded

aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.geometry("400x200")

# Funktsioonid

 
def ok_kalk():
    if var.get() == 1:
        pros = round((float(hind.get()))*0.09,2)
        summ = round((float(hind.get()))*1.09,2)
    if var.get() == 2:
        pros = round((float(hind.get()))*0.2,2)
        summ = round((float(hind.get()))*1.2,2)
    kaibe.config(text=f'{pros}€')
    kokku.config(text=f'{summ}€')

# Sildid

silt = Label(text='Hind käibemaksuta: ', font='Tahoma 12')
silt.grid(row=0, column=0)
silt1 = Label(text='Käibemaksumäär: ', font='Tahoma 12')
silt1.grid(row=1, column=0)
kriips = Label(text='─────────────────────────────────')
kriips.grid(row=3, columnspan=3)
silt2 = Label(text='Käibemaks: ', font='Tahoma 12')
silt2.grid(row=4, column=0)
silt3 = Label(text='Hind käibemaksuga: ', font='Tahoma 12')
silt3.grid(row=5, column=0)

kaibe = Label(text='')
kaibe.grid(row=4, column=1)
kokku = Label(text='')
kokku.grid(row=5, column=1)

# Sisestusväljad

hind = Entry(aken)
hind.grid(row=0,column=1)

# Valikukast

var = IntVar()
maar = Radiobutton(aken, text='9%', variable=var, value=1)
maar.grid(row=1,column=1)
maar = Radiobutton(aken, text='20%', variable=var, value=2)
maar.grid(row=2,column=1)

# Nupud

nupp = Button(aken, text="OK", width=4, command=ok_kalk)
nupp.grid(row=6, column=2)

aken.mainloop()