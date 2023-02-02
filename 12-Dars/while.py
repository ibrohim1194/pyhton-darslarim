i = 1
while i < 6:
  print(i)
  i += 1

print("__________________________________________________________________________________________________________")


# while True:
#     print("salom")  =>  Forever

a = 1
n = int(input("Sonni kiriting:"))
sum = 0

while a<=n:
    sum = sum + a
    a = a+1  #=> sanagich
print(sum)

print("__________________________________________________________________________________________________________")


sanagich = 0

while sanagich < 3:
    print("Abdulaziz")
    sanagich = sanagich + 1
else:
    print("Baxtiyor")

print("__________________________________________________________________________________________________________")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i = i+1

print("__________________________________________________________________________________________________________")


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  