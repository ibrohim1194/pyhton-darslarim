son = lambda x: x*2

print(son(5))


print(" ")


list = [1,5,4,6,8,11,3,12]
list2 = []
def juft():
    for i in list:
        if i % 2 == 0:
            list2.append(i)
    print("Juft sonlar =",list2)
juft()


print(" ")




def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(22))

