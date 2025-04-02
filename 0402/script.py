i = input("skaicius: ")

# s = int(i)
# res = s / 10
# Standartinis
# try:
#     s = int(i)
#     res = 10 / s
# # except Exception as e:
# except ValueError:
#     print("Klaida")
# finally:
#     print("Finally blokas")
#
# print("Veikia kodas")

try:
    s = int(i)
    res = 10 / s
except ValueError:
    print("Klaida")

print(res)

if type(res) == float:
    raise RuntimeError

print("Vykdomas kodas")