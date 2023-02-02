import tkinter as tk
from datetime import date

bugun = date.today()

oyna = tk.Tk()
oyna.geometry('800x600')
oyna.title("Yoshni hisoblab beradigan dastur")
oyna.config(bg="#F7DC6F")
oyna.resizable(width=False, height=False)



def malumotni_aniqlash():
    d = int(e1.get())
    m = int(e2.get())
    y = int(e3.get())

    yosh = bugun.year-y-((bugun.month,bugun.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END, yosh)
    t1.config(state='disabled')



def dasturni_yakunlash():
    oyna.destroy()














l1 = tk.Label(oyna, text="Yoshni hisoblab beradigan python dasturi", font=('Arial',20),fg='black', bg='#F7DC6F')
l2 = tk.Label(oyna, text="Tug'ilgan yil , oy, kun ni kiriting", font=('Arial',12),fg='black', bg='#F7DC6F')
l3 = tk.Label(oyna, text="Sizning yoshingiz:", font=('Times New Roman', 20, 'bold'), fg='red', bg='#F7DC6F')


t1 = tk.Text(oyna, width=5, height=2, state='disabled')


sana = tk.Label(oyna, text="Tug'ilgan sanani kiriting:", font=('Arial',12,'bold'), fg='darkgreen', bg='#F7DC6F')
oy = tk.Label(oyna, text="Tug'ilgan oyni kiriting:", font=('Arial',12,'bold'), fg='darkgreen', bg='#F7DC6F')
yil = tk.Label(oyna, text="Tug'ilgan yilni kiriting:", font=('Arial',12,'bold'), fg='darkgreen', bg='#F7DC6F')


e1 = tk.Entry(oyna, width=8)
e2 = tk.Entry(oyna, width=8)
e3 = tk.Entry(oyna, width=8)

btn = tk.Button(text="Hisoblash", font=('Arial', 12, 'bold'), fg='red', bg='green',command=malumotni_aniqlash)
btn2 = tk.Button(text="Chiqish", font=('Arial', 12, 'bold'), fg='red', bg='green',command=dasturni_yakunlash)





l1.place(x=120, y=5)
l2.place(x=250, y=40)
l3.place(x=100, y=250)
t1.place(x=320, y=250)
e1.place(x=325, y=70)
e2.place(x=325, y=95)
e3.place(x=325, y=120)
btn.place(x=300, y=180)
btn2.place(x=300, y=500)
sana.place(x=100, y=70)
oy.place(x=100, y=95)
yil.place(x=100, y=120)












oyna.mainloop()