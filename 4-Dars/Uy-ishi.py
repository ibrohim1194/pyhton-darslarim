# 1. Stringni uzunligini aniqlab beradigan dastur tuzing

word = str(input("Matnni kiriting:"))
print("1. Bu sozda",len(word),"harf bor.")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Kiritilgan satrning birinchi, o'rta va oxirgi belgilaridan tuzilgan yangi satr yaratish dasturini yatish.
ism = "Ahmad"
print(ism)
print(ism[0:5:2])

# ------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Uchburchakni asosini topish
s = int(input("Yuzani kiriting:"))
h = int(input("Blandlikni kiriting"))
a = (2*s)/h
print(" Uchburchakning asosi",a,"ga teng.")
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Sharning radiusi
radius = int(input("Radiusni kiriting:"))
rad = radius+radius
print("Sharning radiusi",rad,"ga teng")
# ------------------------------------------------------------------------------------------------------------------------------------------------


# 5. A, B, C tomonli uchburchak berilgan, uni yarim perimetrini topib beradigan dastur tuzing.
print("Uchburchakning yarim perimetrini topish uchun tomonlar uzunligini kiriting.")
A = int (input("3. A tomonining uzunligini kiriting:"))
B = int (input("B tomon uzunligini kiriting:"))
C = int (input("C tomon uzunligini kiriting:"))
D = A+B+C
E = D/2

print("Uchburchakning yarim perimetri",E,"ga teng")

# A = 5
# B = 4
# C = 7
# E = A+B+C
# D = E/2
# print("A = 5, B = 4, C = 7. Uchburchakning yarim perimetri",D, "ga teng")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Konus
h = int(input("Konusning balandligini kiriting:"))
r = int(input("Radiusni kiriting:"))
f = (r+r)*h
print("Silindrning o'g'irligi",f,"ga teng")

# 7. -----------------------------------------------------------------------------------------------------------------------------------------------------
print("Avtomobil ma'lum bir tezlikda ma'lum bir masofani qancha vaqatda bosib o'tganini topish uchun tezlik va masofani kiriting")
V = int (input("7. Avtomobil tezligini kiriting:"))
S = int  (input("Masofani kiriting:"))
T = S/V
M = T
print("Avtomobil",V,"tezlik bilan",S,"masofani",T,"vaqatda bosib o'tgan")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# 8.Osmondan erkin tushayotgan jism
h = 100
g = 9.8
d = h/g
print(d)

# -----------------------------------------------------------------------------------------------------------------------------------------------


# 9. Jo'mrakdaann 1s da  1ml suv tomadi, x yilda qancha suv tomadi

print("9. 1s da Jo'mrakdan 1ml suv tomadi, x yilda qancha suv tomadi")
yil = int(input("Yilni kiriting:"))
YIL = yil*365*24*60*60
Yil = YIL*0.001
print(yil,"yilda",Yil,"l  suv tomadi" )

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10.  1 dan n gacha bolgan sonlar berilgan. Berilgan yig'indisini toping
print("Istalgan ikki sonni kiriting va ularni javobini ko'ring")
son = int(input("10. 1-sonni kiriting:"))
son2 = int(input(" 2-sonni kiriting:"))
son3 = son+son2
print(son,"va",son2,"sonlarining yig'indisi",son3,"ga teng.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# 11. CRNAME nomli o'zgaruvchi yarating va unga "Volvo" qiymatini bering
CRNAME = "Volvo"

# ------------------------------------------------------------------------------------------------------------------------------------------------

# 12. X nomli o'zgaruvchi yarating va unga "50" qiymatini bering

X = 50

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# 14. 2my-first_name = "John"   - quyidagi o'zgaruvchidagi xatoni toping


print("14. O'zgaruvchilar hech qachon son bilan boshlanmaydi")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 15. 3 ta o'zgaruvchining qiymati bir xil boladigan o'zgaruvchi yarating

Pul=Raqam=Odam= 15000

print("15",Pul,)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

