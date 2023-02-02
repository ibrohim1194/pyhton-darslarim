# Pythonda funktsiya - ma'lum bir vazifani bajaradigan bir-biriga bog'liq bo'lgan bayonotlar guruhidir.
# Funktsiyalar dasturimizni kichikroq va modulli qismlarga ajratishga yordam beradi. Bizning dasturimiz tobora kattalashib borar ekan, funksiyalar uni yanada tartibli va boshqariladigan qiladi.
# Bundan tashqari, u takrorlanishni oldini oladi va kodni qayta foydalanishga yaroqli qiladi.


# Funksiyaning sintaktik ko'rinishi :


def funksiya_nomi(parametr):
    """ docstring """
    # bayanot(bayonotlar)
    



# Yuqorida quyidagi komponentlardan tashkil topgan funksiya ta'rifi ko'rsatilgan.
# 1) funksiya sarlavhasini boshlanishini belgilovchi def kalit so'zi
# 2) Funksiyani noyob identifikatsiyalash uchun funksiya nomi 
# 3) Funksiya nom berishda o'zining qonun qoidalari bor.
# 4) Parametrlar va argumentlar => funksiyaga qiymat o'tkazish uchun foydalanamiz. Bunda foydalanish ixtiyoriy
# 5) Funksiya sarlavhasining oxirini belgilash uchun ikki nuqta (:) qo'yiladi.
# 6) Funktsiya nima qilishini tasvirlash uchun ixtiyoriy hujjatlar qatori (docstring).
# 7) Funktsiya tanasini tashkil etuvchi bir yoki bir nechta haqiqiy python iboralari. Bayonotlar bir xil chekinish darajasiga ega bo'lishi kerak (odatda 4 bo'sh joy).
# 8) Funksiyadan qiymat qaytarish uchun ixtiyoriy qaytish bayonoti.



# Misol uchun :


def mars(bolalar):
    """Bu funksiya marsdagi bolalar 
    funksiyani tushunib olishi uchun yozilgan"""
    print("Assalomu aleykum" +' '+bolalar + ". Marsga xush kelibsizlar !!!")
    

mars("Saydazam")
    
    
"""
Funktsiya sarlavhasidan keyingi birinchi satr docstring deb ataladi va hujjat satrining qisqartmasi. Funktsiya nima qilishini tushuntirish uchun qisqacha foydalaniladi.
Ixtiyoriy bo'lsa-da, hujjatlashtirish yaxshi dasturlash amaliyotidir. O'tgan hafta kechki ovqatda nima qilganingizni eslay olmasangiz, har doim kodingizni hujjatlashtiring.
Yuqoridagi misolda bizda funktsiya sarlavhasi ostida hujjat satri mavjud. Docstring bir nechta satrgacha cho'zilishi uchun biz odatda uch qo'shtirnoqlardan foydalanamiz. Ushbu qator biz uchun funksiyaning __doc__ atributi sifatida mavjud.

"""


print(mars.__doc__)


# Natija 

# Bu funksiya marsdagi bolalar funksiyani tushunib olishi uchun yozilgan



# return => funksiyadan chiqish va u chaqirilgan joyga qaytish uchun ishlatiladi.

def asosiy_qiymat(raqam):
    """bu funksiya returnni tuwunib olishila uchun"""

    if raqam >= 0:
        return raqam*5
    else:
        return -raqam


print(asosiy_qiymat(2))
print(asosiy_qiymat(-4))



# O'zgaruvchining qamrovi - dasturning o'zgaruvchi tan olinadigan qismi. Funksiya ichida aniqlangan parametrlar va o‘zgaruvchilar funksiya tashqarisidan ko‘rinmaydi. Demak, ular mahalliy miqyosga ega.
# O'zgaruvchining ishlash muddati - bu o'zgaruvchining xotirada mavjud bo'lgan davri. Funktsiya ichidagi o'zgaruvchilarning ishlash muddati funktsiya bajarilgan vaqtga teng.
# Funktsiyadan qaytganimizdan keyin ular yo'q qilinadi. Demak, funktsiya o'zgaruvchining oldingi  qiymatini eslay olmaydi.
# Funktsiya ichidagi o'zgaruvchining qamrovini ko'rsatadigan misol.


# Misol uchun: 

def salom():
    x=10
    print(x)


salom()
x=20
print("X ning qiymati", x)





# Funksiyaning 2 xil turi mavjud : 

# 1. O'rnatilgan funksiyalar.
# 2. Foydalanuvchi tomonoidan yaratilgan funksiyalar. 

# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))



# Parametr => Parametr funksiya taʼrifida qavslar ichida koʻrsatilgan oʻzgaruvchidir.

def funksiya(davlat):
    print("Men" + ' '+ davlat + "danman.")
    
funksiya("Uzbekistan")



# Argument => Axborot funksiyalarga argument sifatida uzatilishi mumkin.

def mars(ism, xabar):
    """Bu misol argument uchun"""
    print("Salom", ism + ', ' + xabar)

mars("Baxtiyor", "Qalesan?")



# Agar funktsiyangizga qancha argument o'tkazilishini bilmasangiz, funksiya ta'rifida parametr nomidan oldin * belgisini qo'shing.
# Shunday qilib, funktsiya bir qator argumentlarni oladi va mos ravishda elementlarga kirishi mumkin:


def my_function(*bola):
    print("Eng kichkina bola bu" + bola[2])

my_function("Abdulaziz", "Abdurahim", "Muhammadbilol")




# Siz argumentlarni kalit = qiymat sintaksisi bilan ham yuborishingiz mumkin. Shunday qilib, argumentlar tartibi muhim emas.

def my_function(bola3, bola2, bola1):
    print("Eng kichkina bola bu " + bola3)

my_function(bola1 = "Abdulaziz", bola2 = "Abdurahim", bola3 = "Muhammadbilol")


# Agar funktsiyangizga qancha kalit so'z argumentlari o'tkazilishini bilmasangiz, ikkita yulduzcha qo'shing: ** funksiya ta'rifidagi parametr nomidan oldin.
# Shunday qilib, funktsiya argumentlar lug'atini oladi va shunga mos ravishda elementlarga kirishi mumkin:


def my_function(**bolalar):
      print("Uning familyasi " + bolalar["familya"])

my_function(ism = "Abdulaziz", familya = "Baxtiyorov")




# Quyidagi misol standart parametr qiymatidan qanday foydalanishni ko'rsatadi.
# Agar funktsiyani argumentsiz chaqirsak, u standart qiymatdan foydalanadi:


def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Har qanday turdagi argumentlarni funksiyaga yuborishingiz mumkin (string,list,tuple, dict va h.k.) va u funksiya ichida bir xil maʼlumotlar turi sifatida koʻrib chiqiladi.
# Masalan, Agar siz Ro'yxatni argument sifatida yuborsangiz, u funktsiyaga kelganda ham Ro'yxat bo'lib qoladi:



def my_function(food):
      for x in food:
        print(x)
        
fruits = ["apple", "banana", "cherry"]

my_function(fruits)












