# Kodutöö 1
# Matis Russi
# IT-21
# 08.03.2022

import random

# Äratus

a = int(input('Sisestage mitu korda äratada: '))
print('Tõuse ja sära!\n'*a)

print('───────────────────────────────────────')

# Murelikud lapsevanemad

ring = int(input('Sisesta ringide arv: '))

b = 0
while ring >= 1:
    if ring % 2 == 0:
        b += ring
    ring += -1
print(f'Porgandite koguarv: {b}')

print('───────────────────────────────────────')

# Täringud

c = int(input('Täringute arv: '))

for i in range(c):
    print(random.randint(1,6), end="\n")
    
print('───────────────────────────────────────')

# Male

ruuduke = int(input('Sisestage täisarv: '))

j = 1
nisu = 1

while j <= ruuduke-1:
    nisu *= 2
    j += 1

print(f"Nisu teri {ruuduke}. Ruudu eest: {nisu}")
print('───────────────────────────────────────')
# Õunad

poidlad = int(input('Mitu pöialpoissi tahab õunu? '))
ounad = 14

while poidlad > 0:
    oun = random.randint(1,2)
    print(oun)
    ounad -= oun
    poidlad -= 1

print(f'Lumivalgekesele jäi {ounad}')