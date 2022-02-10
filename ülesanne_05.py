#Ülesanne 05
#Matis Russi
#IT-21 HKHK
#10.02.2022

#Tärnid

import random

suv = []
for n in range(5):
    suv.append(random.randint(1,10))
for n in range(len(suv)):
    print("*"*suv[n])


#Vanused

import random
age = []
for m in range(5):
    age.append(random.randint(1,99))
print(f"Ages: {age}")
print("Max:",max(age))
print("Min:",min(age))
print("Sum:",sum(age))
print("Avg:",sum(age)/len(age))


#Duplikaadid

nimed = ['Juhan','Kati','Mario','Mario','Mati','Mati']
for l in nimed:
    if nimed.count(l) > 1:
        nimed.remove(l)
print(nimed)



#Õpilased


opilane = ['mati','kalle','pille','sille','tille']
for j in range(len(opilane)):
    print(j+1,opilane[j])

nr = int(input("Vali number (1-5): "))
del opilane[nr-1]
add = input("Sisesta muudatused: ")
opilane.insert(nr-1, add)

for k in range(len(opilane)):
    print(opilane[k])


#Nimede lisamine loendisse

loend = []
for i in range(5):
    nimi = input("Sisesta nimi: ")
    loend.append(nimi)
    loend.sort

for i in range(len(loend)):
    print(loend[i])
