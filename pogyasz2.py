from Csomag2 import Csomag

def beolvasas2():
    fajl = open("csomag.txt", "r", encoding='UTF-8')
    fajl.readline()
    sorok=fajl.readlines() #ez egy strig lista lesz
    print(sorok)
    fajl.close()

    #1. megnyitom a filet olvasásra
    #beolvasom a fejléc sort, ha van
    #beolvasom az összes sort egy listába - string lista
    #bezárom a fájlt
    #5. a sorokat átalakítom objktumokká, azaz szétszedem a benne lévő adatokat
        #/1 létrehozom az osztályt, amibe beolvasom az adatokat
        #/2 végigmegyek a listánés minden sorát feldolgozom
            #//1 eltöntetem a végéről az entert
            #//2 szétvágom a szeparátorok mentén
    
    csomag_lista:list =[] #itt tároljuk ez elkészült csomah objektumainkat
    for i in range(0,len(sorok),1):
        sor= sorok[i]
        sor_lista = sor.strip().split("#") #az elválasztójel mentén szétválasztaja a sorokat
        a=int(sor_lista[0])
        b=int(sor_lista[1])
        c=int(sor_lista[2])
        m=int(sor_lista[3])
        csomag=Csomag(a,b,c,m)
        csomag_lista.append(csomag)

    return csomag_lista

def pogyasz_atlagsuly(lista): #sima összegzés tétele
    ossz:int=0
    db:int=0
    for i in range(0,len(lista),1):
       if (lista[i].a==51):
            ossz+=lista[i].m
            db+=1
        
    return 1000*ossz/db

def legmagasabb_pogyasz(lista):
    max_ertek=0
    max_index=0
    for i in range(0,len(lista),1):
        if (max_ertek<lista[i].b):
            max_ertek=lista[i].b
            max_index=i
            
    return max_index