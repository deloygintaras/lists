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
# from audioop import reverse
from idlelib.replace import replace

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

# zodziai = input("Sukurkite zodziu zodyna, iveskite asmeniskai: ")
# zodziai_list = zodziai.split()
# zodziai_list.sort()
# print("Surikiuoti zodziai:", zodziai_list)


# 15.Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai).

# sarasas = [
#     ["plyteles:", 45],
#     ["ausines:", 14],
#     ["kopecios:", 4],
#     ["klijai:", 88],
# ]
# mazai =[]
# for preke, likutis in sarasas:
#     if likutis < 5:
#         mazai.append(preke)
# print(f"Prekes, kuriu likuciai mazesni nei 5: {mazai}")


# 16.Susikurkite norimą sąrašą su duomenimis. Išveskite šį sąrašą šiais
# pavidalais:
# 1. Kiekvieną elementą atskirant kableliu ir tarpu: pirmas, antras, trečias, ...
# 2. Kiekvieną elementą atskiriant vertikaliu brūkšneliu: pirmas|antras|trečias|...
# 3. Kiekvieną elementą atskiriant tarpu: pirmas antras trečias
#
# listas = ["ananasas", "kirminas", "astunkojis", "dvejetas"]
# print(', '.join(listas))
# print('|'.join(listas))
# print(' '.join(listas))


# 17.Pabandykite atlikti list unpacking. Sąraše sudėkite informaciją ir iškart
# padarykite list unpacking. Tai atlikus išsiveskite gautas reikšmes.
# Pavyzdžiui, sąraše galėtų būti taip pateikta informacija:
# 1. pirmoje vietoje - naudojama programavimo kalba
# 2. antroje vietoje - aplinka (desktop, web, ...)
# 3. likusiose vietose nuo trečios - failai, su kuriais būtų dirbama

# info = ["Python", "Desktop", "main.py", "README.md", "python.txt"]
#
# progkalba, aplinka, *failai = info
#
# print("Naudojama programavimo kalba:", progkalba)
# print("Aplinka:", aplinka)
# print("Failai, su kuriais dirbama:", failai)



# 18.Susikurkite sąrašą projekto komandos narių vardams ir pavardėms
# saugoti. Išveskite tekstą "prie projekto dirba šie komandos nariai:" ir iškart
# po to kiekvieną komandos narį atskiroje eilutėje.
# var = 0
# varpav = ["Gintaras Kanskus", "Vardemaras Plato", "Vaizgantas Strazdunas", "Algimantas Bezdnus", "Natalija Volkina"]
# while var < len(varpav):
#     print(f"Prie projekto dirba sie komandos nariai: {var}: {varpav[var]}")
#     var += 1


# 19.Susikurkite sąrašą, kuriame būtų saugomos jau praeitos Python temos.
# Išveskite tekstą "mes jau mokėmės:". Ir iškart po to atskirose eilutėse
# visas temas, tačiau jas sunumeruokite "1-a tema:", "2-a tema:" ir t.t. Tai
# pamėginkite atlikti tiek su for ciklu, tiek su while ciklu.

# sarasas = [
#     "Python",
#     "IF",
#     "WHILE",
#     "Cycle",
#     "FOR"
# ]
# indeksas = 0
# while indeksas < len(sarasas):
#     print(f"Mes jau mokemes:",indeksas + 1, sarasas[indeksas])
#     indeksas += 1



# 20.Susikurkite masyvą studijų programų pavadinimams saugoti. Užpildykite
# šį masyvą duomenimis. Išveskite kiekvieną studijų programą atskiroje
# eilutėje.
# studijos = [
#     "Chemija",
#     "Matematika",
#     "Medicina",
#     "Fizika",
#     "Kosmetine chemija",
#     "Ekonomika",
#     "Ekologija",
#     "Biofizika",
#     "Biochemija"
# ]
# indeksas = 0
# print("Pasirinktinos studiju programos:")
# while indeksas < len(studijos):
#     print(f"Studiju programa:", indeksas + 1, studijos[indeksas])
#     indeksas += 1


# 21.Susikurkite masyvą šalių pavadinimams saugoti ir jį užpildykite
# duomenimis. Išveskite šalių pavadinimus atskirose eilutėse, su prierašu
# "šalis" ir tada nurodant šalį iš masyvo.
#
# salis = [
#     "Anglija",
#     "Svedija",
#     "Amerika",
#     "Vokietija",
#     "Danija",
#     "Estija",
#     "Lenkija",
#     "Australija",
#     "Prancuzija",
#     "Ispanija",
#     "Portugalija"
# ]
# indeksas = 0
# while indeksas < len(salis):
#     print(f"Salis :", indeksas + 1, salis[indeksas])
#     indeksas += 1


# 22.Susikurkite sąrašą prekių krepšeliui saugoti. Išveskite kiek prekių
# krepšelyje yra narių. Tuomet išveskite visą prekių krepšelio informaciją,
# nurodant kelinta prekė, pvz "nr 1 pirkinys:", "nr 2 pirkinys:" ir t.t.

# prekes = ["obuolys", "kriause", "agurkas", "pomidoras", "abrikosas", "mandarinas", "morka", "cesnakas"]
# print("Prekiu krepselyje yra:", len(prekes), "prekiu.")
# indeksas = 0
# while indeksas < len(prekes):
#     print("Nr:", indeksas + 1,"pirkinys -", prekes[indeksas])
#     indeksas += 1


# 23.Susikurkite pažymių sąrašą ir užpildykite jį informacija. Surikiuokite
# pažymius nuo didžiausio iki mažiausio. Išveskite visus turimus pažymius
# atskirose eilutėse. Prie kiekvieno pažymio taip pat prirašykite "puikiai",
# jeigu jis yra 10, "labai gerai", jeigu jis yra 9 ir t.t.

# pazpav = ["labai blogai", "blogai", "dar vis blogai", "puse velnio", "sriednas", "neblogai", "pusiau gerai", "gerai", "labai gerai", "puikiai"]
# pazymiai = [4, 5, 6, 1, 2, 3, 7, 8, 9, 10]
# sortiruote = (sorted(pazymiai, reverse = True))
# print(sortiruote)
# indeksas = 0
# while indeksas < len(sortiruote):
#     print(f"Pazymys", indeksas + 1, '-', pazpav[indeksas])
#     indeksas += 1


# 24.Susikurkite programą, kurioje vartotojas galėtų nusakyti kiek atsitiktinių
# skaičių turėtų būti sugeneruota. Tuomet programa turėtų būtent tokį kiekį
# atsitiktinių skaičių sugeneruoti ir sudėti į sąrašą. Išveskite visus šiuos
# skaičius ekrane. Tuomet tuos pačius skaičius išveskite ekrane dar kartą,
# tačiau viską spausdinkite atskirose eilutėse, eilutėje nurodant patį skaičių
# ir jo kvadratą.





# 25.Susikurkite norimą sąrašą su duomenimis. Išsiveskite viso šio sąrašo
# informaciją. Pakeiskite trijų pasirinktų narių reikšmes į kitas. Išsiveskite
# pakeisto sąrašo informaciją.






# 26.Susikurkite sąrašą ir jį užpildykite skaičiais (savarankiškai arba
# atsitiktiniais). Iš pradžių išveskite tekstą "lyginiai skaičiai" ir visus lyginius
# skaičius. Tuomet išveskite tekstą "visi nelyginiai skaičiai" ir visus nelyginius
# skaičius. Bei ant galo tekstą "visi skaičiai, kurie dalinasi iš 3" ir visus
# skaičius, kurie atitinka tokią sąlygą.




# 27.Susikurkite sąrašą ir jį užpildykite atsitiktiniais skaičiais. Išveskite visus
# skaičius didesnius nei vidurkis.





# 28.Susikurkite programą, kurioje būtų sukurtas sąrašas iš pasirinkto kiekio
# atsitiktinių skaičių. Raskite kiekvieno skaičiaus daliklius, pavyzdžiui:
# skaičius 2 dalinasi iš 2
# skaičius 3 dalinasi iš 3
# skaičius 4 dalinasi iš 2, 4
# skaičius 5 dalinasi iš 5
# skaičius 6 dalinasi iš 2, 3, 6




# 29.Sukurkite programą, kurioje vartotojas galėtų įvesti norimą kiekį žodžių
# (pasirenka iš pradžių ir vykdomas for iki to kiekio skaičiaus, arba
# vykdomas while kol neįveda q ar kokio kito simbolio/žodžio). Išveskite
# visus šiuos žodžius ekrane.



# 30.Susikurkite sąrašą iš pasirinktų žodžių. Atskirose eilutėse išveskite patį
# žodį, jo raidžių kiekį.




# 31.Susikurkite pažymių sąrašą. Šiuos pažymius leiskite įvesti vartotojui.
# Baigus įvedimą, išveskite suvestų pažymių vidurkį. Taip pat, jeigu
# studentas turėjo neigiamų pažymių, tuomet atskirai parodykite tuos
# neigiamus pažymius ir jų kiekį.



# 32.Susikurkite žodžių sąrašą. Raskite ir išveskite trumpiausią ir ilgiausią
# žodžius, bei jų raidžių kiekius.




# 33.Sugeneruokite 100-ą atsitiktinių skaičių ir sukelkite visus tuos skaičius į
# sąrašą. Atlikite šiuos veiksmus:
# a. Raskite mažiausią skaičių, didžiausią skaičių, bei vidurkį.
# b. Tuomet atrinkite į atskirą sąrašą skaičius, kurie žemesni nei vidurkis. Raskite šių skaičių
# vidurkį.
# c. Taip pat, atrinkite į dar vieną sąrašą skaičius, kurie didesni nei vidurkis. Raskite šių skaičių
# vidurkį.
# d. Ekrane išveskite pradinius duomenis, mažiausią ir didžiausią skaičius, rastą vidurkį,
# pirmus atrinktus skaičius ir jų vidurkį, antrus atrinktus skaičius ir jų vidurkį.




# 34.Susikurkite žodžių masyvą. Išveskite per kiek simbolių yra ilgesnis
# ilgiausias žodis už trumpiausią. Tarkime ilgiausias yra “kompiuteris” (11
# simbolių), o trumpiausias “medis” (5), skirtumas tarp jų 11 - 5 = 6
# simboliai.




# 35.Susikurkite dviejų studentų pažymių sąrašus. Šią informaciją leiskite
# suvesti vartotojui. Raskite kurio studento vidurkis yra geresnis. Taip pat,
# ar kuris iš jų (ar abu) turi neigiamų pažymių.


# 36.Susikurkite skaičių masyvą ir užpildykite jį atsitiktiniais skaičiais. Raskite
# visų skaičių, kurie dalinasi iš 4 sumą.



# 37.Susikurkite skaičių masyvą ir užpildykite jį duomenimis. Išveskite visus
# skaičius atskirose eilutėse. Prie kiekvieno lyginio skaičiaus dar išvedant jo
# kvadratą.



# 38.Susikurkite studento pažymių sąrašą ir užpildykite jį duomenimis
# (atsitiktiniais arba kokius įrašysite). Išveskite kiekvieną pažymį atskiroje
# eilutėje. Prie kiekvieno pažymio nurodykite ar tai teigiamas, ar neigiamas
# pažymys. Taip pat, jeigu neigiamas pažymys, tuomet dar nurodykite kiek
# balų trūko iki teigiamo pažymio. Teigiamas pažymys skaitosi 5 balai.




# 39.Susikurkite žodžių sąrašą ir užpildykite duomenimis. Išveskite visus
# žodžius ekrane, nurodant iš kiek raidžių kiekvienas šis žodis yra sudarytas.
# Papildykite programą taip, kad rastumėte visų raidžių kiekį (pvz yra žodžiai
# "medis" ir "alus", 5 ir 4 raidės atitinkamai, o jas sudėjus gaunasi 9 raidės).




# 40.Susikurkite skaičių sąrašą ir užpildykite duomenimis. Raskite visų skaičių,
# kurie dalinasi iš 3 sumą ir vidurkį. Išveskite pradinius duomenis ir gautus
# atsakymus.




# 41.Susikurkite sąrašą failų pavadinimams saugoti, užpildykite jį duomenimis.
# Įsivaizduokite kad jums reikės nuskaityti šiuos failus, todėl pirma norėsite
# patikrinti su kuriais galite dirbti. Atrinkite į atskirą sąrašą tik tuos failus,
# kurių galūnė yra .txt arba .json tipo. Išveskite atrinktus duomenis.




# 42.Susikurkite sąrašą įvykusių klaidų kodams saugoti ir užpildykite šį masyvą
# duomenimis. Tuomet išveskite visas sukauptas klaidas administratoriui,
# taip, kad jis suprastų kas per klaidos įvyko. Pavyzdžiui, jeigu yra kodas
# "ui87", tai kad išvestų "Grafinės sąsajos klaida navigacijoje", arba jeigu
# kodas "sys12", tuomet "Trūksta operatyviosios atminties sistemoje" ir
# pan.





# 43.Susikurkite sąrašą sandėlio likučiams saugoti (kiekvienas atskiras narys
# sąraše yra atskiros prekės likutis). Su kiekvienu likučiu paskaičiuokite per
# kiek dienų bus išpirktas, jei per dieną vidutiniškai yra nuperkami 5 vnt.
# Išveskite atsakymus atskirose eilutėse, nurodant kiek yra dabar ir kiek
# dienų užteks jo. Pavyzdžiui, jeigu yra likučiai 74, 54 ir 32, tai 74 vnt. prekės
# užteks maždaug 15 dienų, 54 vnt. prekės užteks maždaug 11 dienų ir t.t.
# Pabandykite papildyti programą taip, kad į atskirą sąrašą atrinktų tas
# prekes, kurių užteks savaitei ar mažiau, jas išveskite atskirai, pačioje
# pabaigoje.

# 44.Susikurkite sąrašą norimiems žodžiams saugoti. Užpildykite šį sąrašą
# duomenimis. Į kitą sąrašą atrinkite tuos žodžius, kurie yra trumpi (sudaro
# mažiau nei 5 raidės). Išveskite pradinius duomenis ir atrinktus.