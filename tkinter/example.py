import tkinter as tk
from datetime import date

bugun =  date.today()


oyna = tk.Tk()
oyna.geometry('900x500')
oyna.title("Yoshni hisoblab beradigan dastur")
oyna.config(bg="#F7DC6F")
# oyna.resizable(width=False,height=False) => Bu KOD oynani katta kichik qilib bo'maydigan qilib beradi



def yoshni_aniqlash():
    d = int(inp.get())
    m = int(inp2.get())
    y = int(inp3.get())

    yosh = bugun.year-y-((bugun.month,bugun.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert()
    t1.config(state='disabled')

def dasturni_yakunlash():
    oyna.destroy()





l1 = tk.Label(oyna, text="Yoshni hisoblab beradigan Python dasturi", font=('Arial',20),fg='black',bg="#F7DC6F")
l2 = tk.Label(oyna, text="Tug'ilgan yil , oy, kunni kiriting", font=('Arial',12),fg='black',bg="#F7DC6F")


sana = tk.Label(oyna, text="Tug'ilgan sanani kiriting:",font=('bold',12),fg="black",bg="#F7DC6F")
oy = tk.Label(oyna, text="Tug'ilgan oynini kiriting:",font=('bold',12),fg="black",bg="#F7DC6F")
yil = tk.Label(oyna, text="Tug'ilgan yilni kiriting:",font=('bold',12),fg="black",bg="#F7DC6F")





inp = tk.Entry(oyna, width = 6)
inp2 = tk.Entry(oyna, width = 6)
inp3 = tk.Entry(oyna, width = 6)


btn = tk.Button(text="Hisoblash",font=("Arial",12, "bold"), fg="red",bg="green",command=yoshni_aniqlash())
btn2 = tk.Button(text="Chiqish", font=('Arial', 12, 'bold'), fg='red', bg='green',command=dasturni_yakunlash())


l3 = tk.Label(oyna, text="Sizning yoshingiz:", font=("Arial",12,"bold"), fg='red',bg="#F7DC6F")
t1 = tk.Text(oyna,width=8,height=1.2,state='disabled')












l1.place(x = 170,y = 5)
l2.place(x = 300,y = 40)


sana.place(x=100,y=70),
inp.place(x=300,y=70)

oy.place(x=100,y=100)
inp2.place(x=300,y=100)

yil.place(x=100,y=130)
inp3.place(x=300,y=130)

btn.place(x=300,y=180)

l3.place(x=100,y=250)
t1.place(x=275,y=250)

btn2.place(x=300, y=500)












oyna.mainloop()