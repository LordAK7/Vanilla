import requests
from bs4 import BeautifulSoup


def temp():
    search = "temperature in mumbai"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    print(f"The Temperature Outside Is {temperature} celcius")

