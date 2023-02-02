# SET => bitta o'zgaruvchida bir nechta qiymat saqlash uchun ishlatamiz
# Set => o'zgartirib bo'lmaydi, tartiblab bo'lmaydi, elementlarni tartiblab bo'lmaydi, qavs b-n farq qiladi {}

# 1. O'zgartirib bo'lmaydi

mevalar = {'Olma','Apelsin','Banan','Kiwi'}  
print(type(mevalar))
print(mevalar)

# Tartibsiz
# print(mevalar[2]) - xato

#mevalar[1] = {'Olcha'}  - Bu xato.
# print(mevalar)


# Yangi element qoshish imkoniyati bor
mevalar = {'Olma','Apelsin','Banan','Kiwi'}  
mevalar.add("Shaftoli")
print(mevalar)

mevalar = {'Olma','Apelsin','Banan','Kiwi'}
sabzavotlar = {'Kartoshka','Sabzi','Tarvuz'}

mevalar.update(sabzavotlar)
print(mevalar)


# Elementlarni o'chirish
sabzavotlar = {'Kartoshka','Sabzi','Tarvuz'}

sabzavotlar.remove("Tarvuz")
print(sabzavotlar)

sabzavotlar.discard("Kartoshka")
print(sabzavotlar)


# Eng oxirigi o'chiradi
mevalar = {'Olma','Apelsin','Banan','Kiwi'}
mevalar.pop()
print(mevalar)

# clear() => toliq tozalab beradi
mevalar = {'Olma','Apelsin','Banan','Kiwi'}
mevalar.clear()
print(mevalar)


# del
mevalar = {'Olma','Apelsin','Banan','Kiwi'}
del mevalar
# print(mevalar)

# union()

mevalar = {'Olma','Apelsin','Banan','Kiwi'}
sabzavotlar = {'Kartoshka','Sabzi','Tarvuz'}

set3 = mevalar.union(sabzavotlar)
print(set3)


# intersection_update()

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

x.intersection_update(y)

print(x)


# intersection()

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

z = x.intersection(y)
print(z)


# Symmetric_difference_update()


x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

x.symmetric_difference_update(y)

print(x)