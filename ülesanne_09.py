# Ülesanne 09
# Matis Russi
# IT-21
# 17.02.2022

# Kuupäev

import datetime

# Inglise keeles

aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

print('─────────────────')
# Eesti keeles

import locale
locale.setlocale(locale.LC_TIME, 'et_ET.UTF-8')

aeg1 = datetime.datetime.now()
print(aeg1.strftime('%d. %B %Y'))

# Isikukood

pic = int(input('Sisesta oma isikukood: '))
pic[1]

