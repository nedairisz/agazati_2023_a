import ertekel
import sorozat
import pogyasz1
import pogyasz2


#ertekel.ertekel()

""""""
lista=sorozat.sorozatok()
paratlanok_szama=sorozat.paratlanok_szama(lista)
print(f"A páratlanok száma: {paratlanok_szama}.")

#paratlanok_szama = sorozat.sorozatok()
#print(paratlanok_szama)

#lista=sorozat.sorozatok()



"""
pogyasz1.beolvasas()

pogyasz1.atlag_suly()

pogyasz1.legmagasabb_pogyasz()"""

"""
csomag_lista=pogyasz2.beolvasas2()
print("III/A, B:")
# ki akarom írni az első csomag szélességét
print(f"\t A pogyászok száma:  {len(csomag_lista)}")
pogyasz2.pogyasz_atlagsuly(csomag_lista)

print("III/C:")
atlag= pogyasz2.pogyasz_atlagsuly(csomag_lista)
print(f"\t Az 51 cm-es pogyászok átlag súlyértéke: {round(atlag)} g")

print("III/D:")
max_index= pogyasz2.legmagasabb_pogyasz(csomag_lista)
print(f"\t A legmagasabb pogyász méretei: {csomag_lista[max_index].a}x{csomag_lista[max_index].b}x{csomag_lista[max_index].c}, súlya: {csomag_lista[max_index].m} kg.")

#print(f"Az első csomag szélessége: {csomag_lista[0].a}")"""