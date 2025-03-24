num1 = 100
num2 = 30
num3 = 50
print("=========")
print(num1 < num2)
print(num1 > num2)
print(num1 == num2)
print(num1 != num2)
print("=========")
print(type(num1) is int)
print("H" in "ABCDEFG")
print("=========")
list = ["Labas", "Vakaras", "Diena", "Pietus", "Pavakariai"]
print("Pietus" in list)

# if (a > b) {
# }
a = 5
b = 6
if a < b:
    print("a < b")
else:
    print("a > b")

print("Salyga isoreje")


#if () {
# } else if() {
#} else {
# }

if a < b:
    print("a < b")
    # if a == b:
    #     print("a == b")
    #     if a ==b:
    #         print("a == b")
    #         if a == b:
    #             print()
elif a > b:
    print("a > b")
# elif a > b:
#     print("a > b")
else:
    print("a == b")

# && / and
if a < b and a == 5:
    print("a == 5")

# || / or
if a > b or a == 5:
    print("a == 5 (OR)")

# ! / not
# !false = true
if not a > b:
    print("a < b (inverted)")

autos_ger = ["BMW", "Audi", "Mercedes"]
autos_it = ["Ferrari", "Lamborghini"]
autos_sport = ["BMW", "Ferrari"]
auto = "Renault"


if (auto in autos_ger) or (auto in autos_it) or (auto in autos_sport):
    print("yra vokiskas arba sportinis arba italiskas")
else:
    print(auto, " nera")

if auto in autos_ger:
    print("yra vokiskas")
elif auto in autos_it:
    print("yra italistas")
elif auto in autos_sport:
    print("yra sportinis")
else:
    print("nera")

c = 9
# var res = c % 2 === 0 ? "lygu" : "nelygu"
res = "lygu" if c % 2 == 0 else "nelygu"
print(res)

str = "Kaunas"

print(str.istitle())
print(str.isupper()) #KAUNAS
print(str.startswith("K"))
if str.startswith("K"):
    print("Prasideda is didziosios raides")