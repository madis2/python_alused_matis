# Ülesanne 09
# Matis Russi
# IT-21
# 28.02.2022

# Moodulid

import locale
from dateutil.relativedelta import relativedelta
import datetime

# Inglise keeles

aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

print('─────────────────')

# Eesti keeles

locale.setlocale(locale.LC_TIME, 'et_ET.UTF-8')

aeg1 = datetime.datetime.now()
print(aeg1.strftime('%d. %B %Y'))

print('─────────────────')

# Isikukood

ik = "50503310866"
aasta = int(ik[1]+ik[2])+2000
kuu = int(ik[4])
paev = int(ik[5]+ik[6])

alg = datetime.datetime(aasta,kuu,paev)
lopp = datetime.datetime(int(aeg1.strftime('%Y')),int(aeg1.strftime('%m')),int(aeg1.strftime('%d')))

diff = relativedelta(lopp, alg).years
print(diff)
