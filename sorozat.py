
"""
II/A, B, C:
           	20$28$124$166$15$188$174$243$221$22$945$841
II/D, E:
           	A páratlanok száma: 5.  	
kimutatas.txt tartalma:
II/F:
A páratlanok száma: 5. 
 
⦁	Írasson ki a konzolra dollár jelel ($) elválasztva 12 számból álló véletlen számsorozatot [-10,1000] zárt intervallumon 
    a mintának megfelelően! (4p)
⦁	A generált értékeket tárolja lista adatszerkezetben! (1p)
#⦁	A $ jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)

#⦁	Írjon függvényt paratlanok_szama néven, amiben számolja meg, hogy hány olyan elem van, ami páratlan. 
    A visszatérési érték legyen egy egész szám! (3p)
#⦁	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban 
    fogalmazzon meg! (2p)

#⦁	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a eredmeny.txt nevű fájlba, amit fajlba_kiir 
    nevű metódusban fogalmazzon meg! (2p)
"""

import random
import math

def sorozatok():
    lista= []
    for i in range(0,12,1):
        szam=math.floor(random.random() * 1011 - 10)
        lista.append(szam)
        print(szam, end="$")
    print()
    return lista



def paratlanok_szama(lista):
    i:int=0
    paratlanok_szama:int= 0
    while i<len(lista):
        if int(lista[i])%2!=0:
            paratlanok_szama+=1
        i+=1
    return paratlanok_szama
    




    