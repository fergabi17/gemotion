import requests
import json
import urllib.parse

url = "https://chicken-coop.p.rapidapi.com/games"

title = "days gone"

querystring = {"title":title}

headers = {
    'x-rapidapi-host': "chicken-coop.p.rapidapi.com",
    'x-rapidapi-key': "e930d07731mshe00718d0d6136eap1ae483jsnf6cea31e0367"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

responseObject = json.loads(response.text)


gameEncoded = responseObject["result"][0]["title"].lower()

gameUrl = url + "/" + urllib.parse.quote(gameEncoded)
print(gameUrl)
# gameUrl = gameUrl.replace("%20", "%2520")

# Will be selected from user
gamePlatform = responseObject["result"][0]["platform"]

if gamePlatform == "PS4":
    gamePlatform = "playstaion-4"

gamePlatform = { "platform" : gamePlatform}


gameResponse = requests.request("GET", gameEncoded, headers=headers, params=gamePlatform)

print(gameResponse.text)
# print(gameUrl)