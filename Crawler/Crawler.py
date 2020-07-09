import requests
from bs4 import BeautifulSoup

#get ETtoday traveling Taoyuan
response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

#find() h3 context
result = soup.find("h3")
print(result)

#find all include h3
result = soup.find_all(["h3", "p"], limit=2)
print(result)