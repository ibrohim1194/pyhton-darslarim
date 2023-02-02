for i in range(1,10):
    print(i, end=",")

# _____________________________________________________________________________________________________________________________________________________

son = 0


for i in range(1,10):
  
    son = son+i
print(son)


# _____________________________________________________________________________________________________________________________________________________


lazy_students = ["Muhammad Sodiq","Odil","Alibek"]
print(len(lazy_students))

for i in range(len(lazy_students)):
    print(f"Bu guruhda eng dangasa o'quvchi {lazy_students[i]}")


# _____________________________________________________________________________________________________________________________________________________

yosh = 13

print(f"Mening yoshim {yosh} da")

# _____________________________________________________________________________________________________________________________________________________

for i in range(1,5):
    print(i)
else: 
    print("Xayr") #Agar True bolsa "for" va "else" ham ishlaydi. Agar False bolsa avtomatik faqat "else" ishlaydi.


# _____________________________________________________________________________________________________________________________________________________


for i in range(1,20):
    if i==15: break
    print(i)
else:
    print("Toxta")


mevalar = ["olma","Banan","Gilos"]

for i in mevalar:
    if i == "banan":
        break
    print(i)
else:
    print("Invalid")

# _____________________________________________________________________________________________________________________________________________________

mevalar = ["olma","Banan","Gilos"]

for i in mevalar:
    if i == "Banan":
        continue
    print(i)
else:
    print("Invalid")

# _____________________________________________________________________________________________________________________________________________________

rang = ["qizil","sariq","yashil"]
mevalar3 = ["gilos","banan","olma"]
holati = ["eski","yangi"]
son = [1,2]
for x in rang:
    for y in mevalar3:
        for i in holati:
            for a in son:

             print(x,y,i,a)

# _____________________________________________________________________________________________________________________________________________________

for i in rang:
    pass

# _____________________________________________________________________________________________________________________________________________________

# topshiriq

# son = [1]
# son2 = [1,2]
# son3 = [1,2,3]
# son4 = [1,2,3,4]
# son5 = [1,2,3,4,5]

# for a in son:
#     print(a)
#     for b in son2:
#         print(b)
#     for c in son3:
#         print(c)
#     for d in son4:
#         print(d)
#     for i in son5:
#         print(i)
son = 5

for i in range(1,son+1,1):
    for j in range(1,i+1,1):
        print(j, end=" ")
    print("")


