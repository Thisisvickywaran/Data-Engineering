import requests

url = "https://indian-railway-irctc.p.rapidapi.com/api/trains-search/v1/train/12051"

querystring = {"isH5":"true","client":"web"}

headers = {
	"x-rapidapi-key": "9d564e0c49msh1b1c244670fae75p14249ejsn10b696b219b2",
	"x-rapidapi-host": "indian-railway-irctc.p.rapidapi.com",
	"x-rapid-api": "rapid-api-database"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())