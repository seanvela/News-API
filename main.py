import requests
from send_email import send_email

api_key = '8b46ca12c1224ee48b7e892817d8adeb'

url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-06-25&sortBy=publishedAt&apiKey=8b46ca12c1224ee48b7e892817d8adeb'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Initialize a list to store article titles and description
articles = []

# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        title = article["title"]
        description = article["description"]
        articles.append(f"Title: {title}\nDescription: {description}\n")

# Create the email message content
message = "\n\n".join(articles)
message = message.encode("utf-8")

# Send the email
send_email(message)