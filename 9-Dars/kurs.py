qiymat = int(input("Iltimos qiymatni kiriting:"))
import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()['conversion_rate']

# Your JSON object
print("Natija:",data*qiymat,"so'mga teng")