# List - bitta o'zgaruvchida bir nechta qiymat saqlash uchun ishatiladi
# List har doim [] qavis orqali yoziladi

# Built-in Data type ----- 1. List        2.Tuple         3.Set          4.Dictionaryy

moshinalar = ["Ferrari","Bugatti","Lamborghini",]
print(moshinalar)

mevalar = ["Olma"]
print(mevalar)

# Tartiblasa boladi  (ordered)
# o'zgartirsa boladi  (changable)
# elementlarni takrorlasa boladi  (allow duplicates)
# []


# 1. Tartiblsa bo'ladi

print(moshinalar[1])
print(moshinalar[0:2])
print(moshinalar[-1])
print(moshinalar[2:])
print(moshinalar[:2])
print(moshinalar[0:2:1])
moshinalar = ["Ferrari","Bugatti","Lamborghini","Cherolet","Ford"]
print(moshinalar[-4:-1])

# O'zgartirsa boladi (Changable)
moshinalar = ["Ferrari","Bugatti","Lamborghini","Cherolet","Ford"]
moshinalar[0]="Toyotta"
print(moshinalar)

moshinalar[0:3] = ["Mercedes", "Honda", "Kia"]
print(moshinalar)

# insert() => listga element qo'yish uchun ishlatamiz
moshinalar.insert(2, "Lexus")
print(moshinalar)


# Append()  =>  listga yangi element qoshish uchun ishlatamiz
moshinalar.append("BMW")
print(moshinalar)


# extend() => 2ta listni biriga qoshish uchun ishlatiladi

moshinalar = ["Ferrari","Bugatti","Lamborghini","Cherolet","Ford"]
mevalar = ["Olma","anor"]

moshinalar.extend(mevalar)
print(moshinalar)