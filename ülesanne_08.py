# Ülesanne 08
# Matis Russi
# IT-21
# 16.02.2022

class Auto:
    # Atribuudid
    
    automark = 'teadmata'
    aasta = 0
    hind = 0
    varv = 'teadmata'
    maxkmh = 0
    
    # Meetodid
    
    def lisaMark(self,x):
        self.mark = x
        
    def lisaAasta(self,x):
        self.aasta = x
        
    def lisaHind(self,x):
        self.hind = x
        
    def lisaVarv(self,x):
        self.varv = x
    
    def lisaMaxkmh(self,x):
        self.maxkmh = x
        
    def kuva(self):
        print('Mark: {} \nAasta: {} \nHind: {} \nVärv: {} \nMaksimum kiirus: {} km/h'.format(self.mark, self.aasta, self.hind, self.varv, self.maxkmh))
    
# Objektid
    
uusobjekt = Auto()
uusobjekt.lisaMark('Audi')
uusobjekt.lisaAasta(1984)
uusobjekt.lisaHind(54800)
uusobjekt.lisaVarv('Punane')
uusobjekt.lisaMaxkmh(343)
uusobjekt.kuva()
print("***************************")
sobjekt = Auto()
sobjekt.lisaMark('BMW')
sobjekt.lisaAasta(1992)
sobjekt.lisaHind(1400)
sobjekt.lisaVarv('Must')
sobjekt.lisaMaxkmh(261)
sobjekt.kuva()
