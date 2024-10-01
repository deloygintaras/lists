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

studentai = ["Jonas:", [1, 2, 8, 6, 7],
"Valdemaras:", [5, 8, 1, 3, 4],
"Oskaras:", [2, 3, 4, 8],
"Diana:", [4, 5, 6, 7]
]
if studentai <= 4:
    print(f"Studentai {studentai} turi neigiamu pazymiu: ")


