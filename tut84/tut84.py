'''
    TODO: Requests Module in Python | Python Tutorial - Day #89 
'''

from bs4 import BeautifulSoup
import requests

res = requests.get("https://dummyjson.com/products/1")
# print(res.json())

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    'Content-type': 'application/json;charset=UTF-8'
}

data = {
    "title": "Leader",
    "body": "Silence",
    "userId": 1
}

res = requests.post(url, headers=headers, json=data)

# print(res.json())

# web scraping

res = requests.get(
    "https://www.geeksforgeeks.org/prepare-facebook-hacker-cup/")

print(res.text)

soup = BeautifulSoup(res.text, "html.parser")

for heading in soup.find_all("h1"):
    print(heading.text)
