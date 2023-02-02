# remove() => olib tashlash

ism = ["Laziz","Umid","Odil","Hojakbar"]

ism.remove("Umid")
# print(ism)


# pop() => listdagi elementlarni o'chirish

list1 = ["olma","olcha","anor","banan"]

list1.pop(2) # elementga murojat qilish
list1.pop() # oxirgi elementni ochirib beradi
# print(list1)


# del => listdagi elementlarni o'chirish

list1 = [1,2,3,4,5,6,7,8,9]

del list1[5]
# del list1      listni butunlay ochirib tashlaydi

# print(list1)


# clear() => tozalash
list1 = [1,2,3,4,5,6,7,8,9]

list1.clear()
# print(list1)


# Loop in list

element = ["Hakim",1,5,3,4]

for a in element:
    print(a)


# Sort in list

number = [32,4,53,9999,1]
ismlar = ["Ali","Behruz","Zaynab","Odil","Hakim"]

number.sort()
ismlar.sort()
print(number)
# print(ismlar)


# reverse() => 

ismlar = ["Ali","Behruz","Zaynab","Odil","Hakim"]
ismlar.reverse()
ismlar.sort(reverse=True)


print(ismlar)



Mevalar = ["Ali", "Behruz", "Zaynab", "odil", "hakim"]

Mevalar.sort(key = str.lower)

print(Mevalar)


# copy() => nusxalash
mevalar = ["banana","Apelsin","Kiwi", "olcha"]
mevalar2 = mevalar.copy()
print(mevalar2)