# -5 -4 -3 -2 -1 0 1 2 3 4 => Skaiciu seka

# -5  -4  -3  -2  -1
# 0 1 2 3 4
# L A B A S
txt1 = "Labas"
# 0 1 2 3 4 5 6 7 8 9 10
# H E L L O   W O R L D
txt2 = "Hello World"

print(txt1[1])

print(txt1[-3])

print(txt1[1:4])


print(len(txt1) - 1)
print(txt1[1:-1]) # print(txt1[1:4])

print(txt2[1:-1]) #print(txt2[1:-1:1])
print(txt2[1:-1:2])
print(txt2[1:-1:3])

print(txt2.upper())

print(txt2.count("ll"))

print(txt2.index("l"))
print(txt2.index("World"))

# .index() => Kai neranda nieko tekste grazinamas 0/Klaida
# .find() => kai neranda nieko tekste grazinamas -1
print(txt2.find("BBB"))

print(txt2.replace("l", "WWW"))
print("    Labas vakaras!     ".strip())

print(len(txt2))

# Stringu formatavimas
print("Labas " + txt2)

print(f"Labas {txt2}")

name = "Lukas"
age = 67

print(f"Labas {name} Amzius: {age}") # "Labas" + name + " Amzius: " + age

# =================
# Sarasai
# =================

list = ["Lukas32"]
print(type(list))
print(list) # Nepapildytas

list.append("Lukas")
list.append("Lukas")
list.append("Lukas")
list.append("Lukas10")
list.append("Lukas4")
list.append("Lukas5")
list.append(25)

list.insert(2, "Dovydas2")

list.insert(-4, "Dovydas-4")

print(list) # Papildytas sarasas

print(list.remove("Lukas"))
print(list.pop())
print(list) # Papildytas sarasas

print(list.pop(3))
print(list) # Papildytas sarasas

# print(list[22])
print(list[3:-1])


#
# for(let i = 0; i < list.length; i++) {
#
# }

for item in list:
    print(f"{item}")

for index, item in enumerate(list):
    print(f"{index}: {item}")