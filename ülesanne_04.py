# Matis Russi
# IT-21
# 03.02.2022


#Ruut

print("Kontrollime kas su kujund on ruut või ei.")
a = int(input("Sisesta kujundi külg: "))
b = int(input("Sisesta kujundi teine külg: "))
if a == b:
    print ("Sinu kujund on ruut.")
else:
    print("Sinu kujund ei ole ruut.")

#Matemaatika

c = int(input("Sisesta 1. täisarv: "))
d = int(input("Sisesta 2. täisarv: "))
tehe = input("Sisesta mis tehte soovid teha (+-*/): ")

if tehe=="+":
    v = c+d
elif tehe=="-":
    v = c-d
elif tehe=="*":
    v = c*d
else:
    v = c/d
print(f"{c}{tehe}{d}={v}")

#Juubel

syn = int(input("Sisesta oma sünniaasta: "))
yr = 2022
age = yr-syn
age = age/5
if age == int(age):
    print("Sul on juubel.")
else:
    print("Sul ei ole juubel.")

#Müük

hind = int(input("Sisesta toote hind täisarvuna: "))
soodus1 = hind-(hind*0.1)
soodus2 = hind-(hind*0.2)
if (hind <= 10):
    print(f"Toote lõpphind on {soodus1}€")
else:
    print(f"Toote lõpphind on {soodus2}€")

#Jalgpalli meeskond

sugu = input("Sisesta oma sugu (m/n): ")
sugu = sugu.lower()
if sugu == "m":
    vanus = int(input("Sisesta oma vanus: "))
    if (vanus >= 16 and vanus <= 18):
        print("Õnnitlen, oled tiimis!")
    else:
        print("Vanus ei sobi!")
else:
    print("Ei sobi kuna sa oled naine.")

#Tärnid

for i in range(1,6):
    for j in range(1,6):    
        print('* ', end='')
    print()
print("----------")
for k in range(0,5):
    for l in range(0,k+1):
        print("*",end="")
    print()
print("----------")
for m in range(5,0,-1):
    for n in range(0,m):
        print("*",end="")
    print()

#Loto

import random
random = random.randint(10000,99999)
print(f"Sinu suvaline number on: {random}")

#Paaris ja Paaritu

arv = int(input("Sisesta täisarv 1-100: "))
jaak = arv%2
 
if jaak==0:
    print('Paaris')
else:
    print('Paaritu')

#Pisike korrutustabel

for p in range(1,11):
    for q in range(5,6):
        print(p, "x", q, "=", p*q)

#Viisikud

for a in range(1,21):
    for b in range(5,6):
        print(a*b)

#Arvamismäng

print("Arva ära number 1-10ni.")

nr = 7
loop = 1
kordade_arv = 0

while loop == 1:
    
    arva= int(input("Sisesta täisarv: "))
    
    if kordade_arv >= 2:
        kordade_arv += 1
        loop = 3
        print(f"GAME OVER!! Sinu kordade arv {kordade_arv}")
    elif arva == nr:
        kordade_arv += 1
        print("Õnnitlen, said õige arvu, pakkumiste arv:",kordade_arv)
        loop = 2
    elif arva > nr:
        kordade_arv += 1
        print("Arv on väiksem.")
    elif arva < nr:
        kordade_arv += 1
        print("Arv on suurem.")

#Pank

moni = float(input("Sisesta raha: "))
konto = 0
intress = 0.05
konto = konto + moni
print("Aasta | Algsumma | Intress | Aasta lõpuks")
for c in range(1,6):
    kasum = konto*intress
    print(f" {c}: {round(konto,2):10},{round(kasum,2):10},{round(konto+kasum,2):10}")
    konto = konto + kasum

#Ruutude ja kuupide tabel

print("Arv |Ruut |Kuup |")
print("----------------")
for c in range(1,11):
    print(f"{c:3} | {c*c:3} | {c*c*c:3}")

