# Kodutöö 1
# Matis Russi
# IT-21
# 03.03.2022

# Tervitus

print('Tere, maailm!')
print('────────────────────────────────────────────')

# Aasta liblikas

aasta = 2020
liblikas = 'teelehe-mosaiikliblikas'
lause_keskosa = 'Aasta liblikas on '
lause = lause_keskosa+liblikas
print(lause)
print('────────────────────────────────────────────')

# Pilved

pilv = int(float(input("Sisesta pilvede kõrgus kilomeetrites: ")))
if pilv >= 6.0:
    print("Need on ülemised pilved.")
else:
    print("Need ei ole ülemised pilved.")
print('────────────────────────────────────────────')

# Bussid

koht = int(input('Inimeste arv: '))
buss = int(input('Bussikohtade arv: '))

last = koht%buss

if last == 0:
    buss = koht//buss
    last = buss
else:
    buss = koht//buss+1

print(f"Busse vaja: {buss} \nViimases bussis inimesi: {last}")
