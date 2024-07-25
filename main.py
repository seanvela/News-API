import requests

api_key = '8b46ca12c1224ee48b7e892817d8adeb'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-06-25&sortBy=publishedAt&apiKey=8b46ca12c1224ee48b7e892817d8adeb'

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
