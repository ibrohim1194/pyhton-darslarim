"""Dictionary"""

# Tartiblasa boladi (3.7* dan baland vetrsiyada)
# O'zgartirsa boladi
# Takrorlab bolmaydi
# {}

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287
}
print(student)
print(student["ism"])

# type() => turni aniqlash uchun ishlatamiz
print(type(student))

# dictionary elementga murojat qilish mumkin
print(student["maktab"])

# len() => uzunligini aniqlash mumkin
print(len(student))

# Dictionary da qiymatga boshqa turdagi ma'lumot turlarini saqlash mumkin

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
    "moshinalar": ['Gentra','Cobalt','Malibu']
}


# dict() metodi orqali dictionary yaratib olishimiz mumkin

student = dict(name="Ibrohim", yosh=13, maktab=287)

# get() metodi orqali dictionary ga murojat qilib elememntlarni olishimiz mumkin

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
    "moshinalar": ['Gentra','Cobalt','Malibu']
}

x = student.get("ism")
print(x)


# keys() kalit so'zlarni olish mumkin
student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
    "moshinalar": ['Gentra','Cobalt','Malibu']
}
x = student.keys()
print(x)


# key va Value ni o'zgartirish

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student["ism"]="Baxtiyor"
student["yosh"]=14
print(student)

# update() => yangilash uchun

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student.update({"yosh":14})
print(student)

# yangi element qo'shish

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}
student["bp'yi"]=1.6
print(student)


# update() metodi orqali xam yangi element qoshish

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student.update({"bo'yi":1.6})
print(student)


# pop() => elementlatrni o'chirish uchun ishlatamiz

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student.pop("maktab")
print(student)


# popitem() => 3.7* versiyadan yuqorida  eng oxiridagi elementni o'chiradi


student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student.popitem()
print(student)



# del() elementni o'chirish mimkin

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}
del student["yosh"]
# del student  =>  to'liq o'chiradi
print(student)

# clear() dict ichidagi elementlarni o'chiradi

student = {
    "ism": "Ibrohim",
    "yosh": 13,
    "maktab": 287,
}

student.clear()
print(student)


# copy() => nusxalash

# Nested dictionary
my_family = {
    "child1": {
        "name": "Jack",
        "year": 2004
    },
        "child2": {
        "name": "Tobias",
        "year": 2007
    },
        "child3": {
        "name": "Lisa",
        "year": 2011
    }
}

print(my_family)

