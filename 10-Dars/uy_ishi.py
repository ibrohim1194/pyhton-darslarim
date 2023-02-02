num1 = int(input("sonni kiriting:"))
if num1 > 0:
    print("Bu musbat son")

if num1 < 0:
    print("Bu manfiy son")


# -----------------------------------------------------------------------------------------------------------------------------------------------------------

a = int(input("1dan 7 gacha bo'lgan sonlarni kiriting.Bu sonlar hafta kunlariga tog'ri keladi:"))
if  a==1:
    print("Dushanba")

elif a==2:
    print("Seshanba")

elif a==3:
    print("Chorshanba")

elif a==4:
    print("Payshanba")

elif a==5:
    print("Juma")

elif a==6:
    print("Shanba")

elif a==7:
    print("Yakshanba")

# -------------------------------------------------------------------------------------------------

# 3. 

son = int(input("Sonni kiriting:"))

natija = son % 10

print(f"Bu sonni oxirgi raqami {natija}")


# ------------------------------------------------------------------------------------------------------------------------------------------------
# 4
num = int(input("enter the number: "))
ldigit = num%10

if ldigit/3 == 0:
    print("Bu raqam 3 ga bo'linadi")
else:
    print("Bu raqam 3 ga bo'linmidi")