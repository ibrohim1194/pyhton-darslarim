# 1. Set yaratib beradigan dastur tuzing.
soz = str(input("SET uchun so'z kiriting:"))
print({soz})

# 2. Setga yangi element qo'shadigan dastur tuzing.
set = str(input("SET uchun so'z kiriting:"))
set2 = str(input("SET uchun yangi so'z kiriting:"))
print({set,set2})


# 3. Setdan elementni o'chirib beradigan dastur tuzing.




# 4. Ikkila to'plamdagi bir xil elementlarning yangi to'plamda chiqarib beradigan dastur tuzing.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)


# 5. Ikkala to'plamdagi bir xil bo'lgan elementlarni va boshqa elementlarni yangi to'plamda chiqarib beradigan dastur tuzing.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
