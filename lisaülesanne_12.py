# Lisaülesanne 12
# Matis Russi
# IT-21
# 02.03.2022
# Kalkulaator EUR-EEK ja vastupidi.

# Teen funktsioonid

print('Eurost - Krooni kalkulaator (töötab ka vastupidi)')
print('──────────────────────────────────────────────────')

def eur_eek(a):
    'funktsioon eurost krooni'
    EEK = 15.6466
    v = round(a*EEK,3)
    return v

def eek_eur(a):
    'funktsioon kroonist eurosse'
    EUR = 0.0639
    v = round(a*EUR,2)
    return v

# Küsin kasutajalt kumba valuutat soovib vahetada.
# Kui kasutaja sisestab valesti, siis tuleb teade.

val = input('Mida soovid vahetada (EUR/EEK): ')
print('──────────────────────────────────────────────────')

if val == 'EUR':
    a = int(input('Sisesta euro kogus: '))
    v = eur_eek(a)
    print(f'Kroonides: {v} krooni')
elif val == 'eur':
    a = int(input('Sisesta euro kogus: '))
    v = eur_eek(a)
    print(f'Kroonides: {v} krooni')
elif val == 'EEK':
    a = int(input('Sisesta krooni kogus: '))
    v = eek_eur(a)
    print(f'Eurodes: {v}€')
elif val == 'eek':
    a = int(input('Sisesta krooni kogus: '))
    v = eek_eur(a)
    print(f'Eurodes: {v}€')
else:
    print('Sisestasite valesti. Palun sisestage "EUR" või "EEK"')
