# Python-dagi for tsikli ketma-ketlik (list, tuple , set       ) yoki boshqa takrorlanadigan ob'ektlarni takrorlash uchun ishlatiladi. Ketma-ketlikni takrorlash traversal deb ataladi.

# For loop ning syntax ko'rinishi


"""
for qiymat in ketma-ketlik:
    loopning tana qismi
    
"""

# Bu erda qiymat - har bir iteratsiyada ketma-ketlik ichidagi element qiymatini oladigan o'zgaruvchi.
# Loop biz ketma-ketlikdagi oxirgi elementga yetguncha davom etadi. For tsiklining tanasi chekinish yordamida kodning qolgan qismidan ajratiladi.

# Misol uchun: Listdagi elementlar yig'indisni hisoblash dasturini tuzamiz.

sonlar=[10,23,7,9,6]

yigindi=0

for i in sonlar:
    yigindi=yigindi+i

print("Quyidagi listdagi sonlar yig'indisi", yigindi)

# Stringda foydalanib ko'ramiz

for i in "Mustang":
    print(i, end=",")

# < ---------------------------------------------------------------------------------------------------------------------------- >

# range() => funksiyasidan foydalanib raqamlar ketma-ketligini yaratishimiz mumkin. diapazon (10) 0 dan 9 gacha (10 ta raqam) raqamlarni hosil qiladi.

for i in range(10):
    print(i)  


# Shuningdek, biz boshlash, to'xtatish va qadam hajmini diapazon sifatida belgilashimiz mumkin (start, to'xtatish, step_size). Agar taqdim etilmagan bo'lsa, step_size standarti 1 ga teng.

for i in range(1,10):
    print(i)


for i in range(1,20,2):
    print(i)
    

# range() funksiyasi qaysidir ma'noda "dangasa"dir, chunki biz uni yaratganimizda u "o'z ichiga olgan" har bir raqamni yaratmaydi. Biroq, u iterator emas, chunki u len va __getitem__ operatsiyalarini qo'llab-quvvatlaydi.

games = ['CS GO', 'PUBG', 'Blur']

for i in range(len(games)):
    print("Men", games[i], "o'yini yoqtiraman.")
    
# < ---------------------------------------------------------------------------------------------------------------------------- >

#1 For tsiklida ixtiyoriy else bloki ham bo'lishi mumkin. Agar ketma-ketlikdagi elementlar for loopda ishlatilsa, else qismi bajariladi.
#2 break keyword for tsiklini to'xtatish uchun ishlatilishi mumkin. Bunday hollarda, else qismi e'tiborga olinmaydi.

# 1 (else ning qo'llanilshi)
sonlar = [0, 1, 5]

for i in sonlar:
    print(i)
else:
    print("No items left.")  
    

#2 (else va break ning birgalikdagi qo'llanilishi)
for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Tugadi!")
  
  
  
# < ---------------------------------------------------------------------------------------------------------------------------- >


#      =>ushbu statement yordamida biz siklni barcha elementlardan o'tmasdan oldin to'xtatishimiz mumkin:
# Misol uchun

mevalar = ["olma", "banan", "gilos"]
for x in mevalar:
  if x == "banan":
    break
  print(x)
  
  

moshinalar=["Lamborghini", "Bugatti", "McLaren"]
for i in moshinalar:
    print(i)
    if i == "Lamborghini":
        break



# < ---------------------------------------------------------------------------------------------------------------------------- >

# continue statement => ushbu ibora bilan biz tsiklning joriy iteratsiyasini to'xtatib, keyingisini davom ettirishimiz mumkin.
# Misol uchun


noutbuk = ["Apple", "Lenovo", "Hp", "Acer"]
for x in noutbuk:
  if x == "Lenovo":
    continue
  print(x)



# < ---------------------------------------------------------------------------------------------------------------------------- >

# Nested loop => halqa ichidagi halqa. "Ichki halqa" "tashqi halqa" ning har bir iteratsiyasi uchun bir marta bajariladi.

rang = ["qizil", "sariq", "yashil"]
mevalar3 = ["gilos", "banan", "olma"]
holati=["eski", "yangi"]
son=[1,2]

for x in rang:
  for y in mevalar3:
      for i in holati:
          for a in son:
            print(x, y,i,a)
    
    
# < ---------------------------------------------------------------------------------------------------------------------------- >
# for tsiklda bo'sh joy bo'lishi mumkin emas, lekin agar sizda biron sababga ko'ra kontentsiz for tsikli mavjud bo'lsa, xatolikka yo'l qo'ymaslik uchun pass keyworddan foydalanamiz.

for x in [0, 1, 2]:
    pass