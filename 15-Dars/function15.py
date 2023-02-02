def func(car):
    print("Mening mashinamning modeli",car)
func("BMW")


print("                                                                                            ")


def mars(ism,xabar):
    print("salom",ism,",","men",xabar)

mars("Abdurahmon","o'qishga yetib keldim")


print(" ")


def cars(*cars):
    print("Eng zo'r mashina bu",cars[2])

cars("Mercedes-Benz","Audi","BMW")


print("                                                                                            ")

def myfunc(**bolalar):
    print("Uning familiyasi",bolalar["Familiya"])

myfunc(ism = "Asilbek", Familiya = "Hamidov")


print("  ")

def start(country = "Norway"):
    print("I am from",country)

start("Sweden")
start("Italy")
start()
start("Uzbekistan")

print("   ")

def star(food):
    for x in food:
        print(x)

fruits = ["Apple","Banana","kiwi"]

star(fruits)