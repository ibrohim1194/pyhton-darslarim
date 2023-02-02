"""For"""

# list1 = [1,2,3,4,15,]
# son = 0

# for i in list1:
#     print(i**2)

# for a in list1:
#     son = son+a
# print(son)



list2 = [65,2,25,68,74,16]


son = 0



for a in list2:
    son = son+a
print(son)

list3 = son






ldigit = list3%10

if ldigit/3 == 0:
    print("Bu raqam 3 ga bo'linadi")
else:
    print("Bu raqam 3 ga bo'linmidi")




num = [65,2,25,68,74,16]
num2 = []
for i in num:
    if i%2 == 0:
        num2.append(i)
print(num2)