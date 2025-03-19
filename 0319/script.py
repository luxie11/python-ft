sum0 = 0
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list:
    sum0 += i

print(sum0)

sum2 = 0
for index, item in enumerate(list):
    sum2 += index
    print(f"{index}: {sum2}")
    # print(index + ":" + sum2)

print(sum2)

sum3 = 0
for index, item in enumerate(list[::2]):
    sum3 += index
    print(f"{index}: {sum3}")
    # print(index + ":" + sum2)

print(sum3)

print(f"Ilgis: {len(list)}")

sum4 = sum(list)
print(f"Suma: {sum4}")
print(f"Max: {max(list)}")
print(f"Min: {min(list)}")
# [].map(() => {

# })

print(list[8])
print(list[3:-3])

tupleList = (1 , 2, 3, 4)
print(tupleList)

tupleList = tupleList + (5, 7)
print(tupleList)

darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

for item in darbuotojai:
    print(item)
    for data in item:
        print(data)

# for item in darbuotojai:
#     print(item[3])

print(darbuotojai[1])
print(darbuotojai[1][2])

for vardas, pozicija, atlyginimas in darbuotojai:
    print(f"Vardas: {vardas}")
    print(f"Pozicija: {pozicija}")
    print(f"Atlyginimas: {atlyginimas}")
    print("--------------")

months = "January;February;March"
monthsList = months.split(";")
print(monthsList)

monthsList.append("April")
print(monthsList)

joinedMonths = ",".join(monthsList)
print(joinedMonths)