# text = "labas"
# number = 46
# #          0 1 2
# numbers = [1,5,10]
# print(numbers)
# print(numbers[0])
# numbers[0] = 7
# print(numbers[0])
# print(numbers)
# print(len(text)) #labas
# print(len(numbers)) # skaiciu masyvo ilgis
# numbers.append(20)
# print(numbers)
# numbers.insert(0,40)
# print(numbers)
# numbers.extend([5,6,7])
# print(numbers)
#
# names = [
#     "Jonas",
#     "Petras",
#     "Antanas"
# ]
# print(names)
# names.pop()
# print(names)
# # names.clear()
# # print(names)
# print(names.index("Jonas"))
# print("Antanas" in names)
# print("Jonas" in names)
# print(numbers.count(5))
#
# print(sorted(numbers))
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers[:5])
# print(numbers[5:])
# print(numbers[1:5])
# print(numbers[:-1])
# print(numbers[0:8:2])#viskas kas antra elementa
# print(numbers[::2])#viskas kas antra elementa
#
# mixedList = ["miau", 20, True, "bugatti", "70", 4]
# print(mixedList)
#
# Joana = ["Joana", "Marceliute", 29, False, "jm@gmail.com", 1.65]
# Virgis = ["Virgis", "Noreika", 48, True, "vn@yahoo.com", 1.75]
#
# zmones = [
#     Joana,
#     Virgis,
#     ["Virgis1", "Noreika", 48, True, "vn@yahoo.com", 1.75],
#     ["Virgis2", "Noreika", 48, True, "vn@yahoo.com", 1.75],
#     ["Virgis3", "Noreika", 48, True, "vn@yahoo.com", 1.75]
# ]
#
# print(zmones[4][0])
# zmones.pop(4)
# print(zmones)
# print(list(range(0,2)))
# print(list(range(0,100,7)))
# print(len(list(range(0,100,7))))
#
#
# 1. Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.
# vardai = ["Gintaras", "Augis", "Stelmokas", "Vidas", "Kristina", "Aiste"]
# print(vardai)
# print(vardai[0])
# print(vardai[-1])
# print(len(list(vardai)))
# import random
# from audioop import reverse
# from re import search

# 2. Susikurkite list žmonių ūgiams saugoti ir užpildykite jį informacija.
# Išveskite viso šio list duomenis bei kiek ūgių turite.
# ugis = [1.75, 1.45, 1.55, 1.83]
# print(ugis)
# print(len(list(ugis)))


# 3. Susikurkite list pažymiams saugoti. Pamėginkite sukurti programą, kur
# vartotojas galėtų suvesti norimą kiekį naujų duomenų. Galiausiai išveskite
# visus pažymius ir jų kiekį.

# pazymiai = [1,5,7,9,4]
# print("Iveskite 3 naujus pazymius")
# sk1 = int(input("Iveskite pazymi\n"))
# sk2 = int(input("Iveskite pazymi\n"))
# sk3 = int(input("Iveskite pazymi\n"))
# pazymiai.extend([sk1, sk2, sk3])
# print(pazymiai)
# print(len(list(pazymiai)))

# 4. Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list,
# tiek papildytą duomenimis. Pamėginkite papildyti programą, kad
# vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.

# miestai = ["Vilnius", "Moscow", "Ryga", "Amsterdam", "Paris"]
# print(miestai)
# miest1 = input("Iveskite bent koki norima miesta\n")
# pasirinkimas = input("kur noretumete, kad sistema ikeltu jusu ivestus duomenis (prieky - 1, gale - 2)\n")
# if pasirinkimas == 1:
#     miestai.append(miest1)
#     print(miestai)
#     if pasirinkimas == 2:
#         miestai.extend([miest1])
#         print(miestai)


# 5. Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.

# list1 = ['geltoni', 'krantai', 'jūros', 'begalybėj']
# print(list1)
# quant = int(input('Kiek dar narių pašalint: '))
#
# if quant < len(list1):
#     for term in range(quant):
#         list1.pop(random.randint(0, len(list1) - 1))
# else:
#     print('Nebėra ką šalinti, sąrašas tuščias')
#     quant = len(list1)
#     for term in range(quant):
#         list1.pop(random.randint(0, len(list1)) - 1)
# print(list1)

# 6. Sukurkite list su pasirinktais duomenimis. Patikrinkite ar sąraše yra
# daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).
# list1 = [5, 3, 6, 7, 8, 9]
# print(len(list(list1)))
# if len(list(list1)) > 5:
#     list1.clear()
#     print(list1)




# 7. Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. Leiskite vartotojui
# atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa
# pasakytų ar tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.

# list1 = ["vaikas", "bernas", "moliugas", "astronautas"]
# paieska = input("Iveskite zodi, kurio norite ieskoti\n")
# if paieska in list1:
#     index = list1.index(paieska)
#     print(f"Žodis '{paieska}' yra sarase, jo indeksas: {index}")
# else:
#     print(f"Žodis '{paieska}' nera sarase")


# 8. Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. Galite
# padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas.
# Programa turi pasakyti kiek dešimtukų studentas turi.


# list1 = [5, 8, 10, 9, 7, 3]
# print(list1)
# skaiciav = list1.count(10)
# print(f"pazymys 10 pasikartoja - {skaiciav} karta(-us)")

# 9. Susikurkite automobilių markių sąrašą ir užpildykite jį duomenimis
# (kuriantis sąrašą arba su vartotojo įvestimi). Išveskite turimus duomenis
# ekrane. Tuomet surikiuokite automobilių markes didėjimo tvarka ir
# išveskite. Taip pat, surikiuokite mažėjimo tvarka ir išveskite.
# auto = ["BMW", "MERCEDES-BENZ", "VW", "VOLVO"]
# print(auto)
# auto.sort()
# print(f"Sortiruote didejimo tvarka atrodo taip: {auto}")
# auto.sort(reverse = True)
# print(f"Sortiruote mazejimo tvarka atrodo taip: {auto}")



# 10.Susikurkite studento pažymių sąrašą ir užpildykite duomenimis. Išveskite
# tris didžiausius turimus pažymius.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# didz = sorted(list1, reverse=True)[:3]
# print(f"3 didziausi gauti pazymiai: {didz}")


# 11.Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. Jeigu
# studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių
# pažymių jis turi.

# Studentų pazymiu sarasas
# studentai = [
#     ["Jonas", 1, 2, 8, 6, 7],
#     ["Valdemaras", 5, 8, 1, 3, 4],
#     ["Oskaras", 2, 3, 4, 8],
#     ["Diana", 4, 5, 6, 7]
# ]
#
# # Patikriname kiekvieno studento pazymius
# for studentas in studentai:
#     vardas = studentas[0]  # Pirmas elementas - studento vardas
#     pazymiai = studentas[1:]  # Nuo antro elemento - pazymiu pradzia
#     neigiamu_sk = sum(1 for pazymys in pazymiai if pazymys < 5)  # skaiciuojame neigiamus pazymius
#
#     # isvedame rezultata studentui
#     print(f"{vardas} turi neigiamų pažymių: {neigiamu_sk}")

# 12.Susikurkite pasirinktą sąrašą su duomenimis. Pritaikykite list slicing tokiais
# būdais ir gautus atsakymus išveskite:
# 1. Paimkite pirmus tris narius.
# 2. Paimkite du narius, pradedant trečiu.
# 3. Paimkite paskutinius keturis narius.
# 4. Paimkite kas antrą narį, pradedant trečiu nariu.
# 5. Paimkite visus atbuline tvarka.
# pazymiai = [8, 9, 13, 5, 8, 9, 11, 12, 88, 47]
# print(pazymiai[0:3])
# print(pazymiai[2:4])
# print(pazymiai[-4:])
# print(pazymiai[2::2])
# print(pazymiai[::-1])


# 13.Susikurkite list studentų vidurkiams saugoti. Išsitraukite ir pasidėkite į
# atskirą list tris didžiausius pažymius (galite surikiuoti ir išsikirpti ką reikia).

# paz = [3, 5, 8, 6, 4, 7, 9]
# paz1 = paz
# print(sorted(paz1)[-3:])


# 14.Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas,
# įvesdamas visus norimus žodžius. Po kiekvieno įvedimo jam turėtų būti
# parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį
# surikiuokite iš naujo.







# 15.Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai).





# 16.Susikurkite norimą sąrašą su duomenimis. Išveskite šį sąrašą šiais
# pavidalais:
# 1. Kiekvieną elementą atskirant kableliu ir tarpu: pirmas, antras, trečias, ...
# 2. Kiekvieną elementą atskiriant vertikaliu brūkšneliu: pirmas|antras|trečias|...
# 3. Kiekvieną elementą atskiriant tarpu: pirmas antras trečias





# 17.Pabandykite atlikti list unpacking. Sąraše sudėkite informaciją ir iškart
# padarykite list unpacking. Tai atlikus išsiveskite gautas reikšmes.
# Pavyzdžiui, sąraše galėtų būti taip pateikta informacija:
# 1. pirmoje vietoje - naudojama programavimo kalba
# 2. antroje vietoje - aplinka (desktop, web, ...)
# 3. likusiose vietose nuo trečios - failai, su kuriais būtų dirbama


# 18.Susikurkite sąrašą projekto komandos narių vardams ir pavardėms
# saugoti. Išveskite tekstą "prie projekto dirba šie komandos nariai:" ir iškart
# po to kiekvieną komandos narį atskiroje eilutėje.





# 19.Susikurkite sąrašą, kuriame būtų saugomos jau praeitos Python temos.
# Išveskite tekstą "mes jau mokėmės:". Ir iškart po to atskirose eilutėse
# visas temas, tačiau jas sunumeruokite "1-a tema:", "2-a tema:" ir t.t. Tai
# pamėginkite atlikti tiek su for ciklu, tiek su while ciklu.





# 20.Susikurkite masyvą studijų programų pavadinimams saugoti. Užpildykite
# šį masyvą duomenimis. Išveskite kiekvieną studijų programą atskiroje
# eilutėje.



# 21.Susikurkite masyvą šalių pavadinimams saugoti ir jį užpildykite
# duomenimis. Išveskite šalių pavadinimus atskirose eilutėse, su prierašu
# "šalis" ir tada nurodant šalį iš masyvo.

# 22.Susikurkite sąrašą prekių krepšeliui saugoti. Išveskite kiek prekių
# krepšelyje yra narių. Tuomet išveskite visą prekių krepšelio informaciją,
# nurodant kelinta prekė, pvz "nr 1 pirkinys:", "nr 2 pirkinys:" ir t.t.



# 23.Susikurkite pažymių sąrašą ir užpildykite jį informacija. Surikiuokite
# pažymius nuo didžiausio iki mažiausio. Išveskite visus turimus pažymius
# atskirose eilutėse. Prie kiekvieno pažymio taip pat prirašykite "puikiai",
# jeigu jis yra 10, "labai gerai", jeigu jis yra 9 ir t.t.