import requests

url = "https://irctc1.p.rapidapi.com/api/v1/searchTrain"

querystring = {"query":"190"}

headers = {
	"x-rapidapi-key": "9d564e0c49msh1b1c244670fae75p14249ejsn10b696b219b2",
	"x-rapidapi-host": "irctc1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())