import http.client
import urllib.parse
import json

conn = http.client.HTTPSConnection("rapidapi.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "chicken-coop.p.rapidapi.com",
    'x-rapidapi-key': "e930d07731mshe00718d0d6136eap1ae483jsnf6cea31e0367"
    }

# The title typed by the user
searchTitle = "battlefield 4"
searchTitle = urllib.parse.quote(searchTitle)

conn.request("GET", f"/games?title={searchTitle}", headers=headers)

# Games found with that title
searchResult = json.loads(conn.getresponse().read())

# User selection of the game
selectedGame = searchResult["result"][0]
selectedPlatform = selectedGame["platform"].replace("PS", "playstation-")
selectedTitle = urllib.parse.quote(selectedGame['title'])

conn.request("GET", f"/games/{selectedTitle}?platform={selectedPlatform}", headers=headers)

result = json.loads(conn.getresponse().read())["result"]

print(result)
