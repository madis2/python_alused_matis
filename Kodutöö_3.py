# Kodutöö 3
# Matis Russi
# IT-21
# 08.03.2022

# Ülikooli vastuvõetud

fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []

for rida in fail:
    vastuvoetud.append(int(rida))
fail.close()

yr = int(input('Mis aastat soovid teada (2011-2019): '))
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
ase = aastad.index(yr)
dat = vastuvoetud[ase]
print(f'Aastal {yr} võeti vastu {dat} sisseastujat.')

# Jänesevanemate mure

ring = int(input('Sisesta ringide arv: '))
b = 0

for i in range(ring-1):
    if ring % 2 == 0:
        b += ring
    ring += -1
print(f'Porgandite koguarv: {b}')

# Sissetulekud

fail1 = open("konto.txt", encoding="UTF-8")

for j in fail1:
    arv = float(j)
    if arv > 0.0:
        print(arv)
        
# Jukebox

file = input('Sisestage failinimi ja laiend (edm.txt): ')
fail2 = open(file, encoding="UTF-8")
laul = []
jk = -1
for k in fail2:
    laul.append(k)
    jk += 1
    print(f'{jk:3}. {k}',end = "")
print('')
vali = int(input('Vali laul: '))
song = laul[vali]
print(f'Valitud laul: {song}')