import requests
from bs4 import BeautifulSoup

url = "https://compsci.uncg.edu/people/" # url to faculty page
page = requests.get(url) # perform get request on url

soup = BeautifulSoup(page.content, "html.parser") # pass page into beautiful soup constructor

people = soup.find_all("div", class_="people-text") # get all children of people-text  class

for person in people:
    name = person.find("h4") # find all h4 tags in person

    if (name.find("a") is None): # if they DON'T have an "a" tag
        print(name.contents[0]) # print first index of name contents
    else:
        a = person.find("a") # find "a" tag in person
        print(a.contents[0]) # print first index of a contents
        