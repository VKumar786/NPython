'''
    TODO: Exercise 10 - News App Solution & Shutout | Python Tutorial - Day #93 
'''


import requests

apiKey = "9d1a3af982af4a3d867ce0db13fa4696"
categories = ["business", "entertainment",
              "general", "health", "science", "sports", "technology"]

print("Select which category you are interested in")
print("Option are")

for idx, category in enumerate(categories):
    print(f"{idx+1}. {category}")

el = int(input("Enter from (1-7) :: ")) - 1

res = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=in&category={categories[el]}&apiKey=9d1a3af982af4a3d867ce0db13fa4696")

for idx, article in enumerate(res.json()["articles"]):
    print(f"{idx+1}. {article['title']}")
