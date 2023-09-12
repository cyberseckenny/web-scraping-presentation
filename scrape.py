import requests
from bs4 import BeautifulSoup

url = "https://compsci.uncg.edu/people/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

people = soup.find_all("div", class_="person-box")

for person in people:
    name = person.find("h4");
    print(name)