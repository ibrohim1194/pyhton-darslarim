import requests
from bs4 import BeautifulSoup

shahar = str(input("Kerakli shaharni kiriting:"))

url = f"https://obhavo.uz/{shahar}"
us = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

toliq_sayt = requests.get(url, headers=us)
malumot = BeautifulSoup(toliq_sayt.content, 'html.parser')

malumot_olish = malumot.findAll("div", {"class": "current-forecast"})
print(malumot_olish[0].text)