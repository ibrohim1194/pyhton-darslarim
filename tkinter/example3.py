from tkinter import *
 

oyna = Tk()
oyna.title("Mening birinchi dasturim")
oyna.geometry('600x400')
oyna.config(background='green')


lbl = Label(oyna, text="Salom", font=("Arial Bold", 50), bg="green", fg="red")
lbl.place(x=50,y=50)

btn = Button(oyna, text="Yuborish", fg="red", bg="black")
btn.grid(column=1, row=0)


txt = Entry(oyna, width=30)
txt.place(x=120, y=150)


chk = Checkbutton(oyna, text="Tanlang")
chk.place(x=300, y=200)


rd = Radiobutton(oyna, text="O'zbekiston")
rd.place(x=500,y=300)

spn = Spinbox(oyna, from_=0, to=100)
spn.place(x=100, y=100)









oyna.mainloop()