# Ülesanne 06
# Matis Russi
# IT-21
# 15.02.2022

#Teen muutujad

ke = 0
re = 0
era = []

with open('s6pru_l6ustaraamatus.txt', 'r') as fail:
    for i in fail:
        
        #Väljastan failist info
        
        rida = i.split(" ")
        print(f"{rida[0]:10} {rida[1]:11}{rida[2]:5}{rida[3]:4}", end=" ")
        
        #Loendan kokku reformikad ja kesikud
        
        if rida[2] == 'RE':
            re += 1
        elif rida[2] == 'KE':
            ke += 1
        
        #Kui erakonda pole listis lisan selle
        
        if rida[2] not in era:
            era.append(rida[2])
            
        #Salvestan faili poliitikute nimed
        
        nimi = rida[0]+" "+rida[1]
        nimed = []
        nimed.append(nimi)
        f = open('poliitikud.txt', 'a')
        for i in range(len(nimed)):
            f.write("%s\n" % nimed[i])
        f.close()
        
        
print("")    
print("─────────────────────────────────")
#Loen erinevaid erakondi kokku

erand = set(era)
kokku = len(erand)

#Väljastan info erakondade kohta

print("Kesikuid kokku:",ke)
print("Reformikaid kokku:",re)
print("Erinevaid kokku:",kokku)