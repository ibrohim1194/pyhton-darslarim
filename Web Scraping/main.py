import requests
from bs4 import BeautifulSoup
from tkinter import *

oyna = Tk()
oyna.title("Ob-havo dasturi")
oyna.geometry("600x400",)
oyna.resizable(width=False,height=False)








result = ""
def func():
    global result
    shahar = input.get()
    url = f"https://obhavo.uz/{shahar}"
    us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

  

    toliq_sayt = requests.get(url, headers=us)
    malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')

    malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
    natija = malumot_olish[0].text
    text1.insert('1.0',natija)


def clear():
    text1.delete('1.0',END)






input = Entry(oyna, width=35)
input.place(x=180,y=50)














button = Button(oyna,text="Qidirish",command=func)
button.place(x=260,y=100)

text1 = Text(oyna,font=("Times New Roman",15),width=50,height=11)
text1.place(x=50,y=150)


btn = Button(oyna,text="Tozalash",command=clear)
btn.place(x=420,y=50)























oyna.mainloop()