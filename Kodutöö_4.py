# Kodutöö 4
# Matis Russi
# IT-21
# 08.03.2022

# Moodulid

# Bänner

kord = int(input('Mitu korda soovite reklaami esitada: '))
ad = input('Sisestage reklaamlause: ')

print('────────────────────────────────────────────')

# Õunamahla tegemine

def mahlapakkide_arv(kogus):
    mahlapakkidearv = round(kogus*0.4/3,0)
    return mahlapakkidearv
kg = int(input('Sisesta õunade kogus: '))
print(mahlapakkide_arv(kg))

print('────────────────────────────────────────────')

# Peo eelarve

def eelarve(a):
    summa = (a*10+55)
    return summa
kutsutud = int(input('Mitu inimest on kutsutud? '))
tuleb = int(input('Mitu inimest tuleb? '))
print(f'Maksimaalne eelarve: {eelarve(kutsutud)} eurot')
print(f'Minimaalne eelarve: {eelarve(tuleb)} eurot')

print('────────────────────────────────────────────')

# Tervitused mõtisklustega

kulalised = int(input('Mitu külalist tuleb? '))
def tervitus(a):
    for j in range(a):
        print('Võõrustaja: "Tere!"')
        print(f'Täna on {j+1}. kord tervitada, mõtiskleb võõrustaja')
        print('Külaline: Tere, suur tänu kutse eest!')
tervitus(kulalised)

print('────────────────────────────────────────────')

# Mündid

def pkarv(a):
    konto = 0
    fail = open(a, encoding='UTF-8')
    for k in fail:
        if int(k) < 6:
            konto += int(k)
    return konto
print(f'Hoiupõrsasse läheb {pkarv("mundid.txt")}.')

print('────────────────────────────────────────────')

# Kuupäev

def kuu_nimi(a):
    kuud = ['','jaan','veeb','mär','apr']
    return kuud[a]
print(kuu_nimi(1))

def kuupaev_sonena(b):
    dd,mm,yyyy = b.split('.')
    print(dd,kuu_nimi(int(mm)),yyyy)
kuupaev_sonena('24.02.2022')