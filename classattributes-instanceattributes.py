class Dog:
    species = 'abacus'
    def __init__(self,name,age):

        self.naam = name       
        self.vayassu = age
k = Dog("Dattu",3)
l = Dog("Bow Bow",4)
print(k.naam)
print(k.vayassu)
print(l.naam)
print(l.vayassu)
k.vayassu = 5
print(k.vayassu)
print(k.species)
k.species = "abrakadabra"
print(k.species)
#naam is self i.e instance attribute also vayassu and name ,age are parametres passed they don't refer anything
#species is a class attribute.
#this is code 2 of the tutorial
