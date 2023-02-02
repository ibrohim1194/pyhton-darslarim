from tkinter import *
import wikipedia


oyna = Tk()
oyna.title("Wikipedia dasturi",)
oyna.geometry("600x400",)
oyna.resizable(width=False,height=False)
wikipedia.set_lang("uz")


p1 = PhotoImage(file='wikipedia/wikipedia.png')
oyna.iconphoto(False,p1)

result = ""

def search():
    global result
    result = input.get()
    natija = wikipedia.summary(result,sentences=3)
    text.insert('1.0',natija)

def clear():
    text.delete('1.0',END)








input = Entry(oyna, width=35)
input.place(x=180,y=50)

button = Button(oyna,text="Qidirish",command=search)
button.place(x=260,y=100)

text = Text(oyna,font=("Times New Roman",15),width=50,height=11)
text.place(x=50,y=150)


btn = Button(oyna,text="Tozalash",command=clear)
btn.place(x=420,y=50)













oyna.mainloop()