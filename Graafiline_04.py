# Graafiline 04
# Matis Russi
# IT-21
# 15.03.2022

# Moodulid

from tkinter import *

# Akna seaded

aken = Tk()
aken.title('Matis Russi')
aken.geometry('200x200+100+100')
aken.resizable(0, 0)

# Tekst ja nupud

tekst = Label(text='Siia kunagi vastus!', font='Tahoma 12')
tekst.grid(row=0,columnspan=4, padx=2)

nupp1 = Button(aken, text='7', font='Tahoma 12', width=4, padx=2)
nupp1.grid(row=1, column=0, padx=2)
nupp2 = Button(aken, text='8', font='Tahoma 12', width=4, padx=2)
nupp2.grid(row=1, column=1, padx=2)
nupp3 = Button(aken, text='9', font='Tahoma 12', width=4, padx=2)
nupp3.grid(row=1, column=2, padx=2)
nupp4 = Button(aken, text='/', font='Tahoma 12', width=4, padx=2)
nupp4.grid(row=1, column=3, padx=2)
nupp5 = Button(aken, text='4', font='Tahoma 12', width=4, padx=2)
nupp5.grid(row=2, column=0, padx=2)
nupp6 = Button(aken, text='5', font='Tahoma 12', width=4, padx=2)
nupp6.grid(row=2, column=1, padx=2)
nupp7 = Button(aken, text='6', font='Tahoma 12', width=4, padx=2)
nupp7.grid(row=2, column=2, padx=2)
nupp8 = Button(aken, text='*', font='Tahoma 12', width=4, padx=2)
nupp8.grid(row=2, column=3, padx=2)
nupp8 = Button(aken, text='1', font='Tahoma 12', width=4, padx=2)
nupp8.grid(row=3, column=0, padx=2)
nupp9 = Button(aken, text='2', font='Tahoma 12', width=4, padx=2)
nupp9.grid(row=3, column=1, padx=2)
nupp10 = Button(aken, text='3', font='Tahoma 12', width=4, padx=2)
nupp10.grid(row=3, column=2, padx=2)
nupp11 = Button(aken, text='-', font='Tahoma 12', width=4, padx=2)
nupp11.grid(row=3, column=3, padx=2)
nupp12 = Button(aken, text='0', font='Tahoma 12', width=4, padx=2)
nupp12.grid(row=4, column=0, padx=2)
nupp13 = Button(aken, text=',', font='Tahoma 12', width=4, padx=2)
nupp13.grid(row=4, column=1, padx=2)
nupp14 = Button(aken, text='=', font='Tahoma 12', width=4, padx=2)
nupp14.grid(row=4, column=2, padx=2)
nupp15 = Button(aken, text='+', font='Tahoma 12', width=4, padx=2)
nupp15.grid(row=4, column=3, padx=2)


aken.mainloop()