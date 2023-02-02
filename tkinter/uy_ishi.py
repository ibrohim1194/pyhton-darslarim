import tkinter as tk
from tkinter import * 


oyna = tk.Tk()
oyna.geometry('600x600')
oyna.title("Calculator")
oyna.config(bg="#EFF5F5")
oyna.resizable(width=False,height=False)


def clear():
    entry.set('')


def insert(son):
    qiymat = entry.get()
    if qiymat or qiymat != "":
        result = str(qiymat) + str(son)
        entry.set(result)
    else:
        entry.set(son)


def oper(operator):
    global son_1
    global amal
    son_1 = entry.get()
    amal = operator
    entry.set('')


def barobar():
    global son_1
    global amal
    son_1 = int(son_1)
    son_2 = int(entry.get())

    if amal == "+":
        entry.set(son_1 + son_2)

    elif amal == "-":
        entry.set(son_1 - son_2)

    elif amal == "*":
        entry.set(son_1 * son_2)

    elif amal == "÷":
        if son_1 % son_2 == 0:
            entry.set(son_1 // son_2)
    else:
        entry.set(son_1 / son_2)










grid = Frame(oyna, width=0, height=0, )

entry = StringVar()
question = Entry(oyna, width=30,  fg="lime", font=("Roboto", 15), textvariable=entry).pack()






# text_result = tk.Text(oyna,  state='disabled',text="",font=("arial",30))
# text_result.pack()

btn1 = tk.Button(oyna,text="1",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn2 = tk.Button(oyna,text="2",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn3 = tk.Button(oyna,text="3",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn4 = tk.Button(oyna,text="+",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: oper())

btn5 = tk.Button(oyna,text="4",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn6 = tk.Button(oyna,text="5",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn7 = tk.Button(oyna,text="6",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn8 = tk.Button(oyna,text="-",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: oper())

btn9 = tk.Button(oyna,text="7",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn10 = tk.Button(oyna,text="8",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn11 = tk.Button(oyna,text="9",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert())
btn12 = tk.Button(oyna,text="/",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: oper())

btn13 = tk.Button(oyna,text=".",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: insert(oper))
btn14 = tk.Button(oyna,text="CE",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: clear())
btn15 = tk.Button(oyna,text="=",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: barobar())
btn16 = tk.Button(oyna,text="*",font=("arial",20,'bold'),fg="white",bg="black",width=5,height=2,command=lambda: oper())















grid.place(x=65,y=50)

btn1.place(x=65,y=120)
btn2.place(x=155,y=120)
btn3.place(x=245,y=120)
btn4.place(x=335,y=120)

btn5.place(x=65,y=210)
btn6.place(x=155,y=210)
btn7.place(x=245,y=210)
btn8.place(x=335,y=210)

btn9.place(x=65,y=300)
btn10.place(x=155,y=300)
btn11.place(x=245,y=300)
btn12.place(x=335,y=300)

btn13.place(x=65,y=390)
btn14.place(x=155,y=390)
btn15.place(x=245,y=390)
btn16.place(x=335,y=390)









oyna.mainloop()