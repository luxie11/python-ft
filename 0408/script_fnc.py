def printas(a, b):
    print(a, b)

printas(3, 4)

def printas2(*args):
    print(*args)
    print(type(args))
    print(args[4])

printas2(1, 2, 3, "5", "Stringas", True)

def print_names(*args):
    res = ""
    for name in args:
        res += f"Hello {name} / "
    return res

print(print_names("Petras", "Petraitis", "Petrauskas"))


def multiply(a, *args):
    for index, arg in enumerate(args):
        if not type(arg) is int:
            print(f"Blogas Ivestas parametras {index}: {arg}")
            return
        else:
            print(arg * a)

multiply(10, 1, 2, 3, 4, "treqwdsa")


def multiply2(a, *args, txt="** Daugyba"):
    for index, arg in enumerate(args):
        if not type(arg) is int:
            print(f"Blogas Ivestas parametras {index}: {arg}")
            return
        else:
            res = arg * a
            print(f"{txt}: {res}")

multiply2(1, 2, 3, 4)
multiply2(1, 2, 3, 4, 5, 6, 7, "dasdas", txt="** Daugybu Daugyba:")


def print_kwargs(**kwargs):
    print(kwargs["pirmas"])  # NEGALIMA, NES nezinom kada bus ivestas pirmas, jeigu bus ivestas pirmas kaip objektas
    print(type(kwargs))

print_kwargs(pirmas=1, antras=2, trecias=2)

def print_kwargs2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs2(pirmas=1, antras=2, trecias=2)

def print_kwargs3(sk, **kwargs):
    for key, value in kwargs.items():
        res = value * sk
        print(f"{key}: {res}")


print_kwargs3(10, pirmas=1, antras=2, trecias=2)


class Student:
    # country = "Lukas"
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def getAgeAfter10Years(self):
        return self.age + 10

    def __str__(self):
        return f"Student {self.name} with age {self.age} years old."


# JS: const student1 = new Student("", "")
student1 = Student("John", 18)
student2 = Student("Petras", 40)
print(student1.name, student1.age)

print(student2.name, student2.age)

print(student1.getAgeAfter10Years())
print(student2.getAgeAfter10Years())

print(student1.__str__())

studentsList = [student1, student2]

for student in studentsList:
    student.age = student.age + 1

print(student1)
print(student2)