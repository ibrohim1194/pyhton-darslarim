mevalar = ["olma","nok"]
print(mevalar[1])

mevalar = ['olma','nok','ananas','anor','banan']
mevalar.append('kiwi')
print(mevalar)

mevalar.clear()
print(mevalar)

mevalar.append('olma')
print(mevalar)

mevalar2 = mevalar.copy()
print(mevalar2)


mevalar = ['olma','nok', 'ananas','anor','banan','olma',]

print(mevalar.count('olma'))

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

a = mevalar.index('nok')
print(a)


mevalar.insert(2,'tarvuz')
print(mevalar)

cars = ['BMW','Mercedes','Audi','Rolls-Royce','Bugatti','Jeep','Nissan','Mazda','Toyota','Maseratti']
cars.append('Ferrari',)
cars.append('Mitsubishi',)
cars2 = cars.copy()
print(cars)
print(cars2)


