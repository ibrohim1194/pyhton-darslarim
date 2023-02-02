from tkinter import *
import requests
from bs4 import BeautifulSoup



oyna = Tk()
oyna.title("Kurslar",)
oyna.geometry("600x400",)
oyna.resizable(width=False,height=False)








result = ""
def func():
    global result
    
    

    
    

  
    if input1 == "dollar":
        input1.get()
        us = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        url = "https://bank.uz/uz/currency"
        toliq_sayt = requests.get(url, headers=us)
        malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')

        malumot_olish = malumot.findAll("span", {"class": "medium-text green-date"})
        natija = malumot_olish[0].text
        text.insert('1.0',natija)







# result = ""

# def search():
#     global result
#     result = input.get()
#     natija = wikipedia.summary(result,sentences=3)
#     text.insert('1.0',natija)

def clear():
    text.delete('1.0',END)


def clear():
    text.delete('1.0',END)






input1 = Entry(oyna, width=35)
input1.place(x=180,y=50)














button = Button(oyna,text="Qidirish",command=func)
button.place(x=260,y=100)

text = Text(oyna,font=("Times New Roman",15),width=50,height=11)
text.place(x=50,y=150)


btn = Button(oyna,text="Tozalash",command=clear)
btn.place(x=420,y=50)






















oyna.mainloop()