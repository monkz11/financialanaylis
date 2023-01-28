import requests

response = requests.get("https://api.pushshift.io/reddit/search/comment/?q=science")
print(response.json())