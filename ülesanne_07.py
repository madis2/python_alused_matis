# Ülesanne 07
# Matis Russi
# IT-21
# 16.02.2022

def nimi(nimi,keel='GER'):
    if keel == 'EST':
        print("Tere",nimi)
    elif keel == 'ENG':
        print("Hello", nimi)
    else:
        print("Hallo", nimi)
    print()

nimi('Matis','EST')

# Ruumala leidmine
# Kõigepealt teen funktsioonid kujundi valemitega

import math

def cube(a):
    v = round(a**3,3)
    return v
def sphere(r):
    v = round(4.0/3.0*math.pi*r**3,3)
    return v
def cone(r,h):
    v = round((1.0/3)*math.pi*r*r*h,3)
    return v
def cylinder(r,h):
    v = round(math.pi*r*r*h,3)
    return v

print('******* LEIAME RUUMALAD *******')
print()
print('Vali kujund')
print()
print('1 Kuup')
print('2 Kera')
print('3 Koonus')
print('4 Silinder')

# Kasutaja peab sisestama soovitud kujundi numbri

kjnd = int(input("Sisesta soovitud kujundi nr: "))
print("Kujundi muutujad sisesta täisarvudena")
print()

# Olenedes kasutaja vastusest, küsitakse talt kujundi muutujad
# Pärast seda väljastatakse vastus

if kjnd == 1:
    a = int(input("Valisid kuubi. Sisesta külg: "))
    v = cube(a)
    print("Kuubi ruumala on", v)
elif kjnd == 2:
    r = int(input("Valisid kera. Sisesta raadius: "))
    v = sphere(r)
    print("Kera ruumala on", v)
elif kjnd == 3:
    r = int(input("Valisid koonuse. Sisesta raadius: "))
    h = int(input("Sisesta kõrgus: "))
    v = cone(r,h)
    print("Koonuse ruumala on", v)
else:
    r = int(input("Valisid silindri. Sisesta raadius: "))
    h = int(input("Sisesta kõrgus: "))
    v = cylinder(r,h)
    print("Silindri ruumala on", v)