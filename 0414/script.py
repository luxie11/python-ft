# def program():
#     print("") - BLOGAI

def suma(a, b):
    return a + b
def subs(a, b):
    return a - b

def main():
    print(subs(4, 5))
    print(suma(4,5 ))
print(suma2(4,5))
#  def init():
#     print("print")

def suma2(a, b):
    return a + b


try:
    print(suma2(4, 5))
except ValueError:
    print(suma2(4, 5))
    print("ValueError")


# main()

# ================================

# Pusiau teisingas pavyzdys
# import random
#
# try:
#     skaiciai_inp = input("Įveskite 6 skaičius, nuo 1 iki 30 (pvz: 1 2 3 4 5 6):")
#     skaiciai = skaiciai_inp.split(" ")
#     lucky = random.sample(range(1, 30), 6)
#     correct = 0
#     for skai in skaiciai:
#         skai = int(skai)
#         for luck in lucky:
#             if luck == skai:
#                correct += 1
#     print(f"Jūs atspėjote {correct} iš {len(skaiciai)} skaičių.")
# except ValueError:
#     print("Neteisingi skaičiai.")

#TEisingas pavyzdys
# import random
# def action_fnc():
#     skaiciai_inp = input("Įveskite 6 skaičius, nuo 1 iki 30 (pvz: 1 2 3 4 5 6):")
#     skaiciai = skaiciai_inp.split(" ")
#     lucky = random.sample(range(1, 30), 6)
#     correct = 0
#     for skai in skaiciai:
#         skai = int(skai)
#         for luck in lucky:
#             if luck == skai:
#                 correct += 1
# try:
#     action_fnc()
#     print(f"Jūs atspėjote {correct} iš {len(skaiciai)} skaičių.")
# except ValueError:
#     print("Neteisingi skaičiai.")


# camel case = smallTest
# snake case = small_test

#BLOGAS smalltest
#SmallTest Blogas



import string

vartotojo_slaptazodis = str(input("Slaptazodis: "))

def slaptazodzio_tikrinimas(slaptazodis):
    salygu_atitikimas = 0
    # visų sąlygų tikrinimas
    ilgas_slaptazodis = len(slaptazodis) > 8
    turi_didziaja_raide = any(simbolis.isupper() for simbolis in slaptazodis)
    turi_skaiciu = any(simbolis.isdigit() for simbolis in slaptazodis)
    turi_specialu_simboli = any(simbolis in string.punctuation for simbolis in slaptazodis)

    if ilgas_slaptazodis:
        salygu_atitikimas += 1
    if turi_didziaja_raide:
        salygu_atitikimas += 1
    if turi_skaiciu:
        salygu_atitikimas += 1
    if turi_specialu_simboli:
        salygu_atitikimas += 1
    return salygu_atitikimas
    # print(salygu_atitikimas)


pass_result = slaptazodzio_tikrinimas(vartotojo_slaptazodis)
if pass_result <= 1:
    print('Jūsų slaptažodis silpnas')
elif pass_result == 2:
    print('Jūsų slaptažodis vyra vidutinis')
else:
    print('Jūsų slaptažodis yra stiprus')

# import string
#
# def slaptazodzio_tikrinimas(slaptazodis):
#     salygos = [
#         len(slaptazodis) > 8,
#         any(c.isupper() for c in slaptazodis),
#         any(c.isdigit() for c in slaptazodis),
#         any(c in string.punctuation for c in slaptazodis)
#     ]
#
#     salygu_atitikimas = sum(salygos)
#
#     if salygu_atitikimas <= 1:
#         print('Jūsų slaptažodis silpnas')
#     elif salygu_atitikimas == 2:
#         print('Jūsų slaptažodis yra vidutinis')
#     else:
#         print('Jūsų slaptažodis yra stiprus')
#
# # Vartotojo įvestis
# slaptazodis = input("Slaptažodis: ")
# slaptazodzio_tikrinimas(slaptazodis)

klausimai = [
    {"klausimas": "Kokia yra Lietuvos sostinė?", "atsakymas": "Vilnius"},
    {"klausimas": "Kiek yra 5 + 7?", "atsakymas": "12"},
    {"klausimas": "Kokia didžiausia planeta Saulės sistemoje?", "atsakymas": "Jupiteris"}
]

def viktorina(klausimai_array):
    taskai = 0
    for klausimas in klausimai_array:
        ats = input(klausimas["klausimas"] + ".")
        if ats.strip().lower() == klausimas["atsakymas"].lower():
            print("Teisingai!")
            taskai += 1
        else:
            print(f"Neteisingai! Teisingas atsakymas: {klausimas['atsakymas']}")

    print(f"\nTeisingi atsakymai: {taskai} iš {len(klausimai_array)}")

viktorina()