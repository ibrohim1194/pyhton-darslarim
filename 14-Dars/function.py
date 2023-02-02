def mars():
    """Bu funksiya "salom bolalar" so'zini chiqarib beradi"""
    for i in range(1,10):
        print("salom bolalar")

mars()
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# ==============================================================================================================================================================
# ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()())()()()()()()()()()()()()()()
# _____________________________________________________________________________________________________________________________________________________________
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


print(mars.__doc__)

print("                                                                                                                                             ")



def mars2(talaba):
    print("Assalomu alaykum. Mening ismim",talaba)



mars2("Sarvar")
mars2("Ibrohim")



print("                                                                                                                                             ")


son1 = int(input("1-sonni kiriting:"))
son2 = int(input("2-Sonni kiriting:"))

def qoshish():
    print("Natija:",son1+son2)

qoshish()


print("                                                                                                                                             ")


def asosiy_qiymat(raqam):
    """Bu funksiya returnni tushunib olish uchun"""

    if raqam >= 0:
        return raqam*5
    else:
        return -raqam

print(asosiy_qiymat(2))
print(asosiy_qiymat(-4))


print("                                                                                                                                             ")


def myfunc():
    print("Hi world!")
    return 3+3
    print("Hello world!")

print(myfunc())



print("                                                                                                                                             ")


def salom():
    x=10
    print(x)# bu X boshqa o'zgaruvchilarga teng emas


"""print(x)"""

salom()
x=20
print("X ni qiymati",x)


print("                                                                                                                                             ")


def add_numbers(x,y):
    sum = x+y
    return sum

num1 = 5
num2 = 6


print("The sum is", add_numbers(num1, num2))