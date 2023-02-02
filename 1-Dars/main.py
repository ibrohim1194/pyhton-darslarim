"""Bu yerda a o'zgaruvchi"""
#Bu yerda 5 qiymat 
a=5   #a o'zgaruvchi


print(a)


#O'zgaruvchini nomlash shartlari


# 1. Raqam bilan boshlanmaydi
talaba1 = "Ahmad"


# 2. A-z, 0-9, _ bilan yaratib olishimiz mumkin 

tugilgan_yil = 2000
talaba_1 = "Ahmad"


# 3. Bu 3 lasi turli xil o'zgaruvchi 


Yosh = 13
YOSH = 22

print(Yosh)



# Bitta qatorda bir nechta o'zgaruvchi olish mumkin 

meva1,meva2,meva3 = "Olma","Banan","Qulupnay"

print(meva2)


x=y=z=13
print(x)
print(y)
print(z)




ism = "Ibrohim"
yosh = 13

print("Mening ismim" ,ism, ", va mening yoshim" ,yosh, "da")

print("Mening ismim" +'  '+ism+",mening yoshim"+str(yosh))




#global variable

word =  "Perfect"

#local reviable

def myfunc():
    word = "Good"
    print("Python is"+' '+word)

    

myfunc()
print("Java is"+' '+word)



#Global keyword

def myfunc():
    global P
    P = "awesome"


myfunc()
print("Javascript is"+' '+P)
