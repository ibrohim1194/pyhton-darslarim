import tkinter as tk 
from tkinter import *
import requests
from datetime import datetime


window = Tk()
window.geometry("600x400")
window.title("Weather report")



city_label = tk.Label(window,text="Enter city name",width=30,font="Times 30 bold",bg="black",fg="white",height=1)
city_label.grid(row=0,column=0)


city_entery = tk.Entry(window,text="city",width=30,borderwidth=5)
city_entery.config(font=("Arial",25,"bold"))
city_entery.grid(row=1)


submit_btn = Button(window,text="get weather data",bd=3, bg="black",fg="white",command="weather_data")
submit_btn.grid(row=2)








window.mainloop()