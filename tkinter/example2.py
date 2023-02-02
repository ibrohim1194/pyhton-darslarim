import tkinter as tk


oyna = tk.Tk()
oyna.title("Mening birinchi dasturim")
oyna.geometry("800x600")
oyna.config(background='#495579')


lbl = tk.Label(oyna, text="Choose a folder", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=50)

btn = tk.Button(oyna, text="Yuborish", fg="#00FFD1", bg="#495579")
btn.place(x=520,y=47)


txt = tk.Entry(oyna, width=60, background="#00FFD1" )
txt.place(x=150, y=50)

txt = tk.Entry(oyna, width=60,background="#00FFD1" )
txt.place(x=150, y=100)

lbl = tk.Label(oyna, text="Watermark text", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=100)


lbl = tk.Label(oyna, text="Font size", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=150)



chk = tk.Checkbutton(oyna, text="Normal",bg="#495579", fg="#00FFD1")
chk.place(x=200, y=150)


chk = tk.Checkbutton(oyna, text="Small",bg="#495579", fg="#00FFD1")
chk.place(x=300, y=150)


chk = tk.Checkbutton(oyna, text="Large",bg="#495579", fg="#00FFD1")
chk.place(x=400, y=150)

txt = tk.Entry(oyna, width=10,background="#00FFD1" )
txt.place(x=500, y=150)

lbl = tk.Label(oyna, text="Transparency(1-255)", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=200)

txt = tk.Radiobutton(oyna, width=60,background="#00FFD1",text="Tashkent" )
txt.place(x=150, y=200)

lbl = tk.Label(oyna, text="Save As:", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=260)


chk = tk.Checkbutton(oyna, text=".png",bg="#495579", fg="#00FFD1")
chk.place(x=200, y=255)


chk = tk.Checkbutton(oyna, text=",jpg",bg="#495579", fg="#00FFD1")
chk.place(x=250, y=255)


chk = tk.Checkbutton(oyna, text=".gif",bg="#495579", fg="#00FFD1")
chk.place(x=300, y=255)

chk = tk.Checkbutton(oyna, text=".bmp",bg="#495579", fg="#00FFD1")
chk.place(x=350, y=255)

lbl = tk.Label(oyna, text="Save to:", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=310)


chk = tk.Checkbutton(oyna, text="default(Desktop)   or",bg="#495579", fg="#00FFD1")
chk.place(x=200, y=310)

btn = tk.Button(oyna, text="Path", fg="#00FFD1", bg="#495579")
btn.place(x=350,y=310)

txt = tk.Entry(oyna, width=50,background="#00FFD1" )
txt.place(x=450, y=310)

lbl = tk.Label(oyna, text="Filename", font=("Arial Bold", 10), bg="#495579", fg="#00FFD1")
lbl.place(x=10,y=360)


chk = tk.Checkbutton(oyna, text="default(Watemarket)   or",bg="#495579", fg="#00FFD1")
chk.place(x=200, y=360)


txt = tk.Entry(oyna, width=35,background="#00FFD1" )
txt.place(x=450, y=360)


btn = tk.Button(oyna, text="Submit", fg="#00FFD1", bg="#495579")
btn.place(x=200,y=450)

btn = tk.Button(oyna, text="Cancel", fg="#00FFD1", bg="#495579")
btn.place(x=290,y=450)

oyna.mainloop()