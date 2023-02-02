# If else statement => Agar ma'lum bir shart bajarilgan bo'lsa, biz kodni bajarishni xohlaganimizda qaror qabul qilish talab qilinadi.
# Shartlar : 
# 1) Teng: a == b
# 2) Teng emas: a!=b
# 3) Katta: a>b
# 4) Kichik: a<b 
# 5) Katta yoki teng: a>=b
# 6) Kichik yoki teng: a<=b


# If statement ning syntax ko'rinishi :

"""
    if shart:
        holat

"""



# Misol uchun:

"""
Agar raqam musbat bo'lsa, o'sha qismdagi kod blok bajariladi.

raqam = 3
if raqam > 0:
    print(raqam, "musbat son")
print("Ishladi")

raqam2 = -1
if raqam2 > 0:
    print(raqam2, "bu musbat son")
print("Ishladi")

"""



# If else statementning syntax ko'rinishi. Else => else kalit so'zi oldingi shartlar bajarilmagan holatda elsedan foydalanamiz.

"""
    if shart:
        if ning tana qismi
    else:
        else ning tana qismi

"""



# Misol uchun: 

"""
Dastur son musbat yoki manfiy ekanligini tekshirib beradi

raqam = 3

if raqam <= 0:
    print("Musbat son yoki nol")
else:
    print("Manfiy son")

"""


# elif => Elif kalit so'zi "agar oldingi shartlar to'g'ri bo'lmasa, bu shartni sinab ko'ring" deyishning usulidir. Syntax ko'rinishi


"""
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
    
"""
# Misol uchun



num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Nested if 
# Boshqa if...elif...else ifodasi ichida if...elif...else ifodasi bo‘lishi mumkin. Bu kompyuter dasturlashda uyalar deb ataladi.
# Ushbu bayonotlarning istalgan soni bir-birining ichiga joylashtirilishi mumkin. Indentatsiya - bu joylashtirish darajasini aniqlashning yagona yo'li. Ular chalkash bo'lishi mumkin, shuning uchun kerak bo'lmasa, ulardan qochish kerak.


num = 8

if num >= 0:
    if num == 0:
        if num!=13:
            if num+3==14:
                print("Zero")
    else:
        print("Positive number")
            
elif num == 18:
    if num+8>=8:
        print("Null")
else:
    print("Negative number")
    
    
    
    
# Agar sizda faqat bitta amalni bajarish kerak bo'lsa, uni if operatori bilan bir qatorga qo'yishingiz mumkin.
a=4.5
b=8

if a > b: print("a is greater than b")


a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



9

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Ikkala xolat xam to'g'ri")
  
  
  
# OR => kalit so'zi mantiqiy operator bo'lib, shartli gaplarni birlashtirish uchun ishlatiladi:


a = 200
b = 33
c = 500
if not a==b:
  print("Kamida bitta holat to'g'ri bo'lishi kerak")
  
  
  
# pass => agar iboralar bo'sh bo'lmasa, 
# lekin sizda biron sababga ko'ra mazmunsiz if iborasi mavjud bo'lsa, xatolikka yo'l qo'ymaslik uchun pass bayonotini kiriting.
  
  
  
a = 33
b = 200

if b > a:
  pass