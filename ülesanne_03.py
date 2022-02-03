###############
# Matis Russi #
#   IT-21     #
# 03.02.2022  #
###############


#Korralik nimi

nimi = input("Sisesta oma nimi: ")
nimi = nimi.strip().capitalize()

print("Tere",nimi+"!")



#Vandumine

tekst = input("Sisesta tekst: ")
tekst = vanne.lower().replace("kurat","*****")
print(tekst)



#Email

email = input("Sisesta oma email: ")
print('@' in email)


#Tundide ajad

algus = input("Sisesta oma tundide algus: ")
lopp = input("Sisesta oma tundide lõpp: ")
hh1, min1 = algus.split(":")
hh2, min2 = lopp.split(":")
minutid1 = int(hh1)*60+int(min1)
minutid2 = int(hh2)*60+int(min2)
aeg = abs(minutid1-minutid2)
aegH = aeg // 60
aegM = aeg % 60
print(f"Kool kestab {aegH}:{aegM}")


#Palindroom

pal = input("Sisesta palindroom: ")
pal = pal.lower()
rev_pal = reversed(pal)
if list(pal) == list(rev_pal):
    print("Tekst on palindroom.")
else:
    print("Tekst ei ole palindroom.")

