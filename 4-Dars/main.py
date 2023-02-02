# Operatorlar 

print(10+5)
print(3**2)
print(5%2)
print(7//2)

# 1. Arifmetik Operatorlar 


# + => Qoshish   ----   print(5+8)
# - => Ayirish   ----   print(10-3)
# * => Kopaytirish   ----   print(5*5)
# / => Bolish    ----   print(30/6)
# ** => Darajaga kotarish    ----   print(7**2)
# % => Qoldiqli bolish   ----   print(11%2)
# // => Butun qismni olib beradigan  ----   print(7//2)

# 2. Bjarish (Assigment) operatori


x = 4
x= x+3
print(x)

y = 4
y += 3
print(y)

# 1) +=, -=, *=, **=, /=, //=, %=,

# 3. Farqlash (Comparasion) operatori

a=5
a == 5

hamyon = 20000
if hamyon>12000:
    print("Marojni olsak bo'ladi")

    if hamyon<12000:
        print("Marojni olmaymiz")


# -------------------------------------------------------------------------------------------------------------------------------------------->
son = 7
if son <= 7:
    print("Mars IT school")

# 1) == => Teng yoki teng emasmi()       aniq emas
#  Teng (tekshirib olish uchun ishlatiladi)
# 2) !=     => Teng emas    --- a! = 5
# 3) <      => kichkina belgisi  ----    a<5
# 4) >      => katta belgisi      ----    a>5
# 5) <=     => Kichkina yoki teng      ----    a<5
# 6) >=     => Katta yoki teng       ----    a>5

# ____________________________________________________________________________________________________________________________________________>


# 4. Mantiqiy operatorlar

# 1) and => Va  (TRUE holatda bajariladi)
# 2) or => Yoki  (Bittasi TRUE bolsa) 
# 3) not => Emas

a=3
b=5

if a == 4 and b == 5:
    print("Hello world")

if a == 4 or b == 5:
    print("Hello")
 
if not a == 4 or b == 5:
    print("Hello WORLD")


# -------------------------------------------------------------------------------------------------------------------------------------------------->

# 5. Identity (shaxs) operatorlar

# 1) is => O'zgaruvchidagi qiymatlar bir xil bolsa
# 2) is not => O'zgaruvchidagi qiymatlar bir xil bolmasa

x = ['olma', 'anor', 'banan']
y = ['kiwi', 'olma', 'ananas']

x = y

print(x is y)


x=3
y=4
print(x is not y)

# 6. Membership operatorlar

ism = "Abduazim"
print("z" in ism)