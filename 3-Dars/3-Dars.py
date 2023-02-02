"""String"""

# String qiymatli o'zgaruvchi yaratib olish uchun " " yoki ' ' foydalanamiz
ism1 = "Abdurahmon"
ism2 = "Asilbek"
ism3 = "Muhammadali"
ism4 = "O'lmas"


# Agar tutuq belgisi kelib qolsa xatolikni yoqotish uchun \ belgidan foydalanib ketamiz
ism5 = 'O\'tkir'
print(ism5)


# String bu massiv element
word = "Python"
print(word[0])

til = "O'zbek tili"
print(til[7])


# Len() => stringni uzunligini aniqlab beradigan funksiya
word2 = "Python"
print(len(word2))
print(word2[2:7])
print(word2[2:7:2])
print(word2[1:])
print(word2[:4])
word3 = "Python 3"
print(word3[-5:-2])


# Upper() va Lower() method. Stringni katta yoki kichkina qilib beradigan
ism = "Saidamir"
print(ism.upper())
print(ism.lower())


# strip() => Stringdagi boshidan yoki oxiridan bosh joy olib tashlaydigan funksiya
example = "  Hello world  "
print(example.strip())


# replace() => Stringdagi elementni boshqa elementga almashtirish uchun ishlatiladi
futbolchi = "S.Ronaldo"
print(futbolchi.replace("S","C"))


# Count() =>
name =  "Laziz"
print(name.count("z"))


# Format() => String ichida o'zgaruvchida foydalanish u-n ishlatamiz
issm = "Abdurauf"
mtn = "Savolga {} javob berdi"
print(mtn.format(issm))

olma = 2
anor = 3
text = "Bozordan {} kg olma va {} kg anor oldim"
print(text.format(olma,anor))


olma = 2
anor = 3
text = "Bozordan {0} kg olma va {1} kg anor oldim"
print(text.format(olma,anor))



# f string
old = 13
print(f"Mening yoshim {old} da\n Mening ismim Ibrohim")