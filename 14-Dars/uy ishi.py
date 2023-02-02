







print("                                                                                                                                             ")

# 2.
sonlar = [8,2,3,0,7]



def yigindi():
    a = 0
    for i in sonlar:
        a += i
    print(a)


yigindi()

print("                                                                                                                                             ")




# 3.
sonlar2=[8,2,3,-1,7]
def kopaytma():
    a = 1
    for i in sonlar2:
        a = a*i
    print(a)

kopaytma()

print("                                                                                                                                             ")


# 4.
example=[1,2,3,4,"a","b","c","d"]                                     
example.reverse()
ex = []
def teskari():
    for i in example:
        ex.append(i)
    print(ex)
            

teskari()


print("                                                                                                                                             ")


# 5.
list1 = [1,2,3,3,4,4,5]
list2 = []
def noyob():
    for i in list1:
        if i == 1:
            list2.append(i)
        elif i == 2:
            list2.append(i)
        elif i == 5:
            list2.append(i)
    
    print(list2)

noyob()



print("                                                                                                                                             ")


# 7.

son1 = int(input("1-Sonni kiriting:"))
son2 = int(input("2-Sonni kiriting:"))
son3 =  son1 ** 2
son4 =  son2 ** 2
def kvadrat(): 
    print("     1-Sonning kvadrati",son3,"\n     2-Sonni kvadrati",son4,"ga teng")

kvadrat()



print("                                                                                                                                             ")


# 8.
a = int(input("8. Sonni kiriting:"))


def test():
    natija = a ** 0.5
    print(natija)

test()



print("                                                                                                                                             ")



# 9.
student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
    "Ball": 99
}
def ism():
    print("9. Ism: Ibrohim,\nYosh:13,\nBall:99,\nUniverstitet: Mars It School")

ism()



print("                                                                                                                                             ")

# 10.
son = int(input("10. Sonni kiriting:"))

def baravar():
    son2 = son*2
    print(son2)

baravar()


print("                                                                                                                                             ")



# 11.

def func(a,b):
    num = a + b
    return num + 5
print(func(4,5))

print("                                                                                                                                             ")





# 12.
son = int(input("12. Sonni kiriting:"))

def juft():
    if son % 2 == 0:
        print("Bu son juft son")
    else: print("Bu toq son")  

juft()  


print("                                                                                                                                             ")


# 13.

a = int(input("13.Sonni kiriting:"))


def faktor():
    n=1
    for i in range(1,a+1):
        n = n*i
    print(n)
faktor()








print("                                                                                                                                             ")


# 16.
son = int(input("16. Sonni kiriting:"))


def kub():
    son2 = son ** 3
    print(son2)

kub()


