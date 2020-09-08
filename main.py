import requests


username = "dentifriciosbiancante"


if requests.get("https://t.me/" + username).text.find('<meta name="robots" content="noindex, nofollow">') >= 0:
    print("Username found")

else:
    print("username not found")
