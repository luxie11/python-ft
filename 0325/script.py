#for (let i = 0; i< 10 ; i++)
for item in range(10):
    print(item)


print("1", "2", "3", "4", "5", "6", "7", "8", "9", sep=" | ")

# print("1", "2", "3", "4", "5", "6", "7", "8", "9", end=";")

if type("A") is str:
    print("string")
else:
    print("not string")

l = ["abc", 45, True, ("a", "b", "c"),  45.555]
for item in l:
    if type(item) is str:
        print("string")
    if type(item) is list:
        print("list")
    if type(item) is tuple:
        print("tuple")
    if type(item) is float:
        print("float")
    if type(item) is int:
        print("int")
    if type(item) is bool:
        print("bool")

k = 123.31231245243564763521
print(round(k, 8))

s = [6, 11, True, 0, 55, 44, 34, 3, 1]
print(sorted(s))
print(sorted(s, reverse=True))

import locale
locale.setlocale(locale.LC_ALL, "lt_LT")
print(locale.windows_locale)
lt = ["žemė", "Kaunas", "Ąžuolas", "Ąsotis"]
r = sorted(lt, key=locale.strxfrm)
print(r)