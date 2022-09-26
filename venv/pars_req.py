import requests
from bs4 import BeautifulSoup

req = requests.get("https://rsue.ru/raspisanie/", data = {"type_d": "1", "kind_id":"2" , "category" :"2" })
src = req.text
soup = BeautifulSoup(src, 'lxml')
print (soup)