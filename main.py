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

miestai = ["Vilnius", "Moscow", "Ryga", "Amsterdam", "Paris"]
print(miestai)




# 5. Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.