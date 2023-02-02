# while tsikli bilan biz shart to'g'ri bo'lsa, bir qator bayonotlarni bajarishimiz mumkin.


# Syntax of while loop: 
""" 
  while test_expression:
        Body of while
"""  

i = 1
while i < 6:
  print(i)
  i += 1


# 1 dan n gacha bo'lgan sonlarning yig'indisini hisoblab beradigan dastur tuzamiz: 

n = int(input("n ni kiriting: "))

# yig'indini va sanagichni kiritamiz
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # sanagich

print("Umumiy yig'indi", sum)




# For looplar bilan bir xil, while looplarida ixtiyoriy else bloki ham bo'lishi mumkin.
# while siklidagi shart False deb baholansa, else qismi bajariladi.
# while tsikli break operatori bilan tugatilishi mumkin. Bunday hollarda, boshqa qismi e'tiborga olinmaydi. Demak, agar break bo'lmasa va shart noto'g'ri bo'lsa, while siklining else qismi ishlaydi.


'''While loop va else ning foydalanilishi'''

sanagich = 0

while sanagich < 3:
    print("Abdulaziz")
    sanagich = sanagich + 1
else:
    print("Baxtiyor")
    
    
    

# Pythonda break va continue iboralari oddiy sikl oqimini o'zgartirishi mumkin.
# Shart noto'g'ri bo'lgunga qadar tsikllar kod bloki bo'ylab takrorlanadi, lekin ba'zida biz joriy takrorlanishni yoki hatto butun tsiklni test ifodasini tekshirmasdan tugatishni xohlaymiz.
# Bunday hollarda break va continue iboralari ishlatiladi.



""""
Break operatori uni o'z ichiga olgan siklni tugatadi. Dasturni boshqarish tsiklning tanasidan so'ng darhol bayonotga o'tadi.
Agar break iborasi o'rnatilgan sikl ichida bo'lsa (boshqa tsikl ichidagi tsikl), break operatori eng ichki tsiklni tugatadi. 

"""

# Misol uchun 

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
# continue iborasi bilan biz joriy iteratsiyani to'xtatib, keyingisini davom ettirishimiz mumkin:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  



# Topshiriq :

""""
a) 
*
**
***
****

b) Berilgan sonni 10 dan kichik yoki teng bo'lgunga qadar 3 ga necha marta bo'lish mumkinligini tekshiring.
c) Kiritilgan raqamdan 1 gacha bo'lgan juft va toq raqamlarni chop eting.

"""
