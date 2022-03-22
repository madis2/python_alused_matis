# Graafiline 06
# Matis Russi
# IT-21
# 22.03.2022

# Moodulid

from tkinter import *

# Akna seaded

aken = Tk()
aken.title('Taani')

# Lõuend

louend = Canvas(aken, width = 500, height = 500)
louend.pack()

# Lipu loomine

louend.create_rectangle(0, 0, 600, 600, fill='#BB2020', outline='#BB2020')
louend.create_rectangle(0,270,600,220, fill='#FFFFFF', outline='#FFFFFF')
louend.create_rectangle(110,0,150,600, fill='#FFFFFF', outline='#FFFFFF')

# Tekst

louend.create_text(300,50, text="Hello Tkinter!", fill="Black", font=("Tahoma", 24))

# Pilt

minu_pilt = PhotoImage(file='kopenhaagen.png')
louend.create_image(300, 300, anchor=NW, image=minu_pilt)



aken.mainloop()