# Harjutus 02
# Matis Russi
# 01.02.2022

#Kütusekulu arvutamine

tank = int(input("Sisesta tangitud kütus liitrites: "))
km = int(input("Sisesta läbitud kilomeetrid: "))
valem = round((tank/km)*100)
print("Sinu auto kasutab",valem,"liitrit 100'le km'le")


#Arvusüsteemid

tais = int(input("Sisesta täisarv: "))
kahend = bin(tais)
kuuend = hex(tais)
print("Kahendsüsteemis on arv:", kahend)
print("Kuusteistkümnendsüsteemis on arv:", kuuend)


#Ajateisendus

sis = int(input("Sisesta minutid: "))
tund = 60
tunnid = sis // tund
min = sis % tund
print(tunnid,"h",":",min,"min")


#Kolmnurga hüpotenuus

a = 16
b = 9
teoreem = pow(a,2)+pow(b,2)
import math
hypotenuus = round(math.sqrt(teoreem))
print("Kolnurga hüpotenuus on",hypotenuus)


#Rulluisutajad

avg = 29.9
aeg = 0.4
vahemaa = round((avg*aeg))
print("24 minutiga jõuab",vahemaa,"kilomeetri kaugusele")


#pitsa

sobrad = 3
hind = 12.90
tip = 0.1
proge = ((hind*tip)+hind)/sobrad
print("Iga sõber maksab", proge,"€")


#kolmnurga ümbermõõt

a,b,c = 15,16,18
p = a+b+c
print("Kolmnurga ümbermõõt: ",p)


#3 toote hind

hind = 36.75
ale = 0.4
kogus =3
summa = (hind-(hind*ale))*kogus
print(kogus, "toote hind on" ,summa,"€")
