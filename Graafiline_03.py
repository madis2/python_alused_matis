# Graafiline 03
# Matis Russi
# IT-21
# 15.03.2022

# Moodulid

from tkinter import *

# Akna seaded

aken = Tk()
tekst = aken.title('Matis Russi')

aken.resizable(0, 0)
aken.configure(background='black')

#tekst
rida = 'Nimi: Matis Russi'
rida1 = 'Rühm: IT-21'
rida2 = '2022'
tekst = Label(aken, text=rida, fg = 'red', bg = 'black', font = 'Tahoma 16 bold italic', pady = 10, padx = 30, justify = CENTER).pack()
tekst1 = Label(aken, text=rida1, fg = 'red', bg = 'black', font = 'Tahoma 16 bold italic', justify = CENTER).pack()
tekst2 = Label(aken, text=rida2, fg = 'red', bg = 'black', font = 'Tahoma 16 bold italic', pady = 10 ,justify = CENTER).pack()

aken.mainloop()