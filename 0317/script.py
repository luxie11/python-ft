num1 = 10
num2 = 20
num3 = 30
num4 = 30.55
text = "Hello world"
char = 'c'
res1 = num1 + num2
print(res1)

res2 = num1 - num2
print(res2)

print(num2 % num1)

print(text)

print(type(text))
print(type(num4))
print(type(char))


resT = "100" + "1"
#adssdadsaads
print(resT)
try:
    input1 = input("Iveskite teksta: ")
    input2 = input("Iveskite teksta2: ") #aseqwewqewqeqw
    # print(type(input))
    # print("Ivestas tekstas: " + input)
    converted_input = int(input1)
    converted_input2 = int(input2)
    # print(type(converted_input))
except ValueError:
    print("Neteisingai ivesta reiksme")
