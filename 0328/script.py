# sk = 0
# while sk < 10:
#     print(sk)
#     sk += 1
#
# sk2 = 0
# for i in range(10):
#     print(i)


# while True:
#     try:
#         number = int(input("Enter a number: "))
#         print(f"Number: {number}")
#         break
#     except ValueError:
#         print("Error! Please enter a number.")

# while True:
#     print("kartojimo pradžia")
#     print("1. šis meniu punktas nedaro nieko\n"
#           "2. išeiti iš kartojimo bloko\n"
#           "3. vėl parodyti meniu")
#     p = input("Iveskite pasirinkima: ")
#     if p == "2":
#         print("Iseinama is bloko")
#         break
#     if p == "3":
#         print("Vel rodomas meniu")
#         continue
#     else:
#         print("Nieko nebuvo pasirinkta")
#     print("Pabaiga")


# while True:
#     print("kartojimo pradžia")
#     print("1. Skaiciavimas\n"
#           "2. išeiti iš kartojimo bloko\n"
#           "3. vėl parodyti meniu\n")
#     p = input("Iveskite pasirinkima: ")
#     if p == "1":
#         while True:
#             print("Iveskite skaiciu daugybai is 100 arba spauskite q - grizti i meniu")
#             i = input("Iveskite skaiciu: ")
#             if i == "q":
#                 break
#             elif not i.isdigit():
#                 print("KLAIDA!! IVESTAS NE SKAICIUS")
#                 continue
#             else:
#                 rez = int(i) * 100
#                 print(f"Rezultatas: {rez}")
#     if p == "2":
#         print("Iseinama is bloko")
#         break
#     if p == "3":
#         print("Vel rodomas meniu")
#         continue
#     else:
#         print("Nieko nebuvo pasirinkta")
#     print("Pabaiga")

# for i in range(20):
#     print(i)

list = [4, 2, 3, 4, 44, 6, 7,77, 9, 999]

print(max(list))

# max = 0
# for i in list:
#     if i > max:
#         max = i
# print(max)

min = list[0]
for num in list:
    if num < min:
        min = num
print(min)

list2 = [4, 2, 3, 4, 44, 6, 7, 77, 9, 999]
list3 = []
# PIRMAS BUDAS
# for num in list2:
#     list3.append(num)
# print(list2)
# print(list3)

#Naujas Budas
list3 = [el for el in list2]
print(list2)
print(list3)

list4 = [el * 10 for el in list2]
print(list2)
print(list4)

list5 = [el % 10 for el in list2]
print(list2)
print(list5)

d = [1, 10, 20]
list7 = []
for el in list2:
    l = []
    for num in d:
        l.append(num * el)
    list7.append(l)

print(list2)
print(list7)

list6 = [[el, el * 10, el * 20] for el in list2]
print(list2)
print(list6)

list8 = [el for el in list2 if el % 2 == 0]
print(list2)
print(list8)

r = ["A", "B", "C", "D", "E", "F"]
s = [1, 2, 3, 4, 5, 6]

list9 = [f"{raid}{sk}" for raid in r for sk in s]
print(list9)