# Tuple()

# O'zgartirsa bolmaydi
# Takrorlab boladi
# tartinblasa boladi
# ()

phones = ("Samsung",)
phones = ("Samsung","Apple","Xiaomi","Honor")
thistuple = tuple(("Apple"))

print(type(phones))
print(len(phones))
print(type(thistuple))

print(phones[2])
print(phones[-2])
print(phones[2:])
print(phones[:2])
print(phones[:3])
print(phones[1:4:1])
print(phones[-3:-1])

# Tuple ni listga o'zgartirish

y = list(phones)
print(type(y))
# y.append("Tesla")
y[0]="Tesla"

phones = tuple(y)
print(phones)


# Unpacking tuple

fruits = ("Apple","Banana","Strawberry")

(a,b,c) = fruits

print(a)
print(b)
print(c)

# * (Asterix dan foydalanish)


fruits = ("Apple","Banana","Strawberry","Cherry","Orange")
(a,b,*c) = fruits

print(a)
print(b)
print(c)


fruits = ("Apple","Banana","Strawberry","Cherry","Orange")
(a,*b,c) = fruits

print(a)
print(b)
print(c)


fruits = ("Apple","Banana","Strawberry","Cherry","Orange")
(*a,b,c) = fruits

print(a)
print(b)
print(c)


# Tuple ni qoshish

tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1+tuple2
tuple4 = tuple2*3

print(tuple3)
print(tuple4)



# index() => nechinchi pozitsiyada joylashganini korsatib beradi

thistuple = (1,3,7,7,8,5,4,6,8,5)
x = thistuple.index(8)
print(x)


# list
cars = ["Bugatti"]
thislist = list(("Bugatti","Ferrari","Chevolet"))
print(type(cars))
print(type(thislist))