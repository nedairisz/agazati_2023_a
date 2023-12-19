
"""
A csomag.txt állomány szerkezete:
·         a (szélesség cm): pl: 51
·         b (magasság cm): pl.: 33
·         c (mélység cm): pl.: 24
·         m (súly kg-ban megadva): pl.: 10
Az állomány első sora a mezőneveket tartalmazza kettőskereszttel elválasztva.

III/A, B:
            	A pogyászok száma: 101
III/C:
            	Az 51 cm-es pogyászok átlag súlyértéke: 7375 g
III/D:
            	A legmagasabb pogyász méretei: 47x46x16, súlya: 4 kg.     

⦁	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a csomag.txt fájlból a játékosok adatait, 
    és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány 
    első sora az adatok fejlécét tartalmazza! (7p)
⦁	Írassa ki a pogyászok számát a mintának megfelelően a konzolra! (2p)
⦁	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok átlag súlya gramban. (1kg = 1000g) (4p)
⦁	Írassa ki konzolra a mintának megfelelően a legmagasabb pogyász  méreteit és súlyát (ha több is van, akkor az első legmagasabb adatait).(4p)

"""
from csomag import Csomag

csomagok_listaja:list = []

def beolvasas():

    text = open("csomag.txt", "r")
    text.readline()
    sorok=text.readlines() #ez egy strig lista lesz
    #print(sorok)

    for sor in sorok:
        tisztitottsor = sor.strip()
        daraboltsor = tisztitottsor.split("#")

        szelesseg = int(daraboltsor[0])
        magassag = int(daraboltsor[1])
        melyseg = int(daraboltsor[2])
        suly = int(daraboltsor[3])

        # példányosítás
        csomag = Csomag(szelesseg, magassag, melyseg, suly)
        # belefűzzük az objektumot
        csomagok_listaja.append(csomag)

    text.close()

    print(f"A pogyászok száma: {len(csomagok_listaja)}")

def atlag_suly():

    suly_gyujto = 0
    db_gyujto = 0

    for csomag in csomagok_listaja:
        if csomag.szelesseg == 51:
            suly_gyujto += csomag.suly
            db_gyujto += 1

    if db_gyujto == 0:
        print("Nincs 51 cm széles pogyász a listában.")
    else:
        atlag_suly = suly_gyujto / db_gyujto
        print(f"Az 51 cm széles pogyászok átlag súlya: {atlag_suly * 1000} g")

def legmagasabb_pogyasz():

    legmagasabb = csomagok_listaja[0]

    for csomag in csomagok_listaja[1:]:
        if csomag.magassag > legmagasabb.magassag:
            legmagasabb = csomag

    print(f"A legmagasabb pogyász méretei: {legmagasabb.szelesseg}x{legmagasabb.magassag}x{legmagasabb.melyseg}, súlya: {legmagasabb.suly} kg.")