#function pavadinimas()

def pavadinimas():
    print("Labas")

def pavadinimas2():
    return "Labas"

res = pavadinimas2()
print(res)

#function pavadinimas(vardas = "Jonas", pavarde = "Jonaitis") => JS

def pavadinimas3(vardas = "Jonas", pavarde = "Jonaitis"):
    print(f"{vardas} {pavarde}")
    def pavadinimas4():
        return "Jonas"
    pavadinimas4()

pavadinimas3("Lukas", "M")
pavadinimas3()

def suma(a: int, b: int) -> float:
    return a + b / 1 + 3 + 5 + 8

# res = suma("r", 5)  Blogas formatas
print(suma(1, 2))
# print(r) Klaida

