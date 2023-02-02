# 1. Berilgan listdagi elementlarini teskari shaklda yozib oling
list = [100, 200, 300, 400, 500]
list_2 = list.reverse()

lst1 = [100, 200, 300, 400, 500]

print("1.",list_2)
# ------------------------------------------------------------------------------------------------------------------------------------------

# 2. Ikkita roʻyxatni indeks boʻyicha qoʻshish dasturini yozing. 
# Ikkala ro'yxatdagi 0-indeks elementini, so'ngra 1-indeks elementini va oxirgi elementgacha davom etadigan yangi ro'yxat yarating.
# Qolgan narsalar yangi ro'yxatning oxiriga qo'shiladi.

list1 = ["M", "na", "i", "Jo"]
list2 = ["y", "me", "s", "hn"]

LIST = list1[0]+list2[0]
LIST2 = list1[1]+list2[1]
LIST3 = list1[2]+list2[2]
LIST4 = list1[3]+list2[3]
print("2.",LIST,LIST2,LIST3,LIST4)
# --------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Raqamlar ro'yxati berilgan. Ro'yxatning har bir elementini kvadratga aylantirish uchun dastur yozing.

raqamlar = [1, 2, 3, 4, 5, 6, 7]
Raqamlar = [1, 2, 3, 4, 5, 6, 7]
RAQAMLAR = raqamlar[0]*Raqamlar[0]
RAQAMLAR1 = raqamlar[1]*Raqamlar[1]
RAQAMLAR2 = raqamlar[2]*Raqamlar[2]
RAQAMLAR3 = raqamlar[3]*Raqamlar[3]
RAQAMLAR4 = raqamlar[4]*Raqamlar[4]
RAQAMLAR5 = raqamlar[5]*Raqamlar[5]
RAQAMLAR6 = raqamlar[6]*Raqamlar[6]
print("3.", raqamlar)
print("[",RAQAMLAR,RAQAMLAR1,RAQAMLAR2,RAQAMLAR3,RAQAMLAR4,RAQAMLAR5,"]")
# -----------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Raqamlardan tashkil topgan a va b listlar berilgan. Shu ikkita listni umumiy bo'lgan elementlaridan tashkil topgan dastur tuzing(ikkalasida ham boridan tashkil topgan dastur).

a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("4. a = 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,\n"
      "b = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,")
print(a[0],a[1],a[2],a[3],a[4],a[5],
      b[0],b[1],b[2],b[4],b[7],b[12])
 #   --------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Massiv elementlaring birinchi va oxirgi elementlarini chiqaruvchi dastur tuzing(Format Stiringni ishlatgan holda).
a = [1, 2, 3, 4, 5]
print("5. a = [1, 2, 3, 4, 5]")
print("Birinchisi:",a[0],"oxirgisi:",a[4],)
# -------------------------------------------------------------------------------------------------------------------------------------------------

# 6. a va b listlar berilgan,b ro'yhatda a ro'yxatda bo'lmagan elementlarni chiqaradigan dasturni yozing.

ruyhat1 = (['oq', 'qora', 'qizil'])
ruyhat2 = (['qizil', 'yashil'])
print("6.",ruyhat2[0])
# ------------------------------------------------------------------------------------------------------------------------------------------------

# 7. List berilgan shu listning uzunligini topadigan dastur tuzing.

thislist = ["apple", "banana", "cherry"]
print("7.",len(thislist))
# -----------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Uzunligi 10 ga teng bo'lgan list berilgan. Shu listning sanoq sonidagi 2 elementdan boshlab oxirgi elementigacha chiqaradigan dastur tuzing.

mashina = ["Mercedes","Audi","BMW","Ferrari","Porsche","Lamborghini","Bugatti","Maseratti","Mazda","Nissan"]
print("8.",mashina[2:10])
# --------------------------------------------------------------------------------------------------------------------------------------------------

# 9.Biror bir list berilgan oxirgi elementidan bitta oldingi element oldidan boshqa bir yangi element qo'shib qoyadigan dastur tuzing.

thoselist = ["9. apple", "banana", "cherry"]
thoselist.append("Watermelon")
print(thoselist)
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Mevalardan ibort bo'lgan list berilgan shu listdagi elementlarni alifbo tartibida saralab chiqarib beradigan dastur turing.

fruit = ["orange", "mango", "kiwi", "pineapple", "banana"]

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# 11. a list berilgan.a listdan nusxa olib b listni tuzuvchi dastur tuzing.

A = ["Olma","Banan","Nok"]
B = A
print(B)
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# 12. Ismlar listi berilgan. Undan hohlagan bir ismni kiritganinggizda Ismlar listida necha marotaba qatnashganing topuvchi dastur tusing.
name = "alice, john, bob, alice, bob, john, alice"
print("3")
# --------------------------------------------------------------------------------------------------------------------------------------------------

# 13. Ismlar listi berilgan. Shu listni teskari tartibda chiqaradigan dastur tuzing.

names = ["john", "alice", "bob"]
names.reverse()
names.sort(reverse=True)
print(names)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 14. a list berilgan uning oxirgi elementini o'chirib yuboradigan dastur tuzing

lst = [1,2,3,4,5,6,7,8,9]

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# 15. Ushbu listning yi'g'indisini hisoblab beradigan dastur tuzing.
lst3=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

for i in lst3: 
      num = i+i

#------------------------------------------------------------------------------------------------------------------------------------------------------

# 16.Quyidagi listdagi eng katta raqamni aniqlab beradigan dastur tuzing.
number_list = [22, 5, 76, 100, 12.3, 9]
print("16. Listdagi eng katta son",max(number_list)) 

# --------------------------------------------------------------------------------------------------------------------------------------------------

#17. Quyidagi listdagi eng kichkina raqamini topib beradigan dastur tuzing.
number_list2 = [22, 5, 76, 100, 12.3, 9]
print("16. Listdagi eng katta son",min(number_list2)) 
# ----------------------------------------------------------------------------------------------------------------------------------------------------

# 18. Listdagi elementlarni o'sish tartibida yozing

numbr = [22, 5, 76, 100, 12.3, 9]
numbr.sort()
print("18.",numbr)


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# 19. Listdagi elementlarni pasayish tartibida yozing

num = [22, 5, 76, 100, 12.3, 9]
num.sort(reverse=True)
print("",num)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# 22. 2018-8-8 va 2018-9-3 oʻrtasidagi kunlar sonini hisoblash uchun python dasturini yozing.

yil1 = 2018-8-8
yil2 = 2018-9-3
kun = 30*8
kun2 = 30*9
kun3 = 8
kun4 = 3
jami = kun2+kun4
jami2 = kun+kun3
jami3 = jami-jami2
print("22. 2018-8-8 va 2018-9-3 oʻrtasidagi kunlar soni",jami3,"ga teng")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# 23. Quyidagi chiqishda ko'rsatilganidek, ikkita aniqlangan koordinatalar, coordinate_1 va coordinate_2 orasidagi masofani hisoblash uchun python dasturini yozing.

coordinate_1 = [5, 1]
coordinate_2 = [8, 7]
cord = 8-5
cord2 = 7-1
print("23.",cord,",",cord2)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# 25. Foydalanuvchi tomonidan kiritilgan soniyalarni kun, soat va daqiqaga aylantirish uchun python dasturini yozing.

son = int(input("Iltimos, soniyalarni kiriting:"))
minut = son/60
hour = minut/60
day = hour/24
year = day/365
print(son)
print(year,":",day,":",hour,":",minut)


# -----------------------------------------------------------------------------------------------------------------------------------------------------

# 26. Foydalanuvchidan 3 ta tasodifiy sonni kiritishni so'rash uchun python dasturini yozing, shuning uchun ularni shartli bayonotdan foydalanmasdan o'sish tartibida tartiblang.

son = int(input("Iltimos, birinchi raqamni kiriting:"))
son2 = int(input("Iltimos, ikkiinchi raqamni kiriting:"))
son3 = int(input("Iltimos, uchinchi raqamni kiriting:"))
print("26.",son)
print(son2)
print(son3)
son4 = son,son2,son3

print(son4)

