
"""
I/A, B:
Étel neve: Ananászos pizza
Étel rendelőjének neve: Kiss Előd
Értékelés (1-5): 4

I/C:
Köszönjük az értékelést!
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
étel neve, étel rendelőjének neve és értékelés! (2p)
B.	A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,5], zárt intervallum értendő):
Amennyiben negatív számot adott meg:
“Az értékelés nem lehet negatív!”,
Amennyiben 5 feletti egész számot adott meg:
“5 pont feletti értékelés nem elfogadható!”
Helyes pont-adat esetén:
“Köszönjük az értékelést!” 
Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.	A mintának megfelelően írassa ki az eredményt! (1p)
"""

def ertekel():
    i:int = 0
    etel: str = str(input("Étel neve: "))
    rendelo:str = str(input("Étel rendelőjének neve: "))
    ertekeles:int = int(input("Értékelés (1-5): "))
    while not(ertekeles>1 and ertekeles<5):
        if ertekeles<1:
            print("Az értékelés nem lehet negatív!")
            ertekeles:int = int(input("Értékelés (1-5): "))
        elif ertekeles>5:
            print("5 pont feletti értékelés nem elfogadható!")
            ertekeles:int = int(input("Értékelés (1-5): "))
    i+=1
    print("Köszönjük az értékelést!")