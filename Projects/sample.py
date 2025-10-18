import requests

base_url = "https://indian-railway-irctc.p.rapidapi.com/api/trains-search/v1/train"

querystring = {"isH5":"true","client":"web"}

headers = {
	"x-rapidapi-key": "9d564e0c49msh1b1c244670fae75p14249ejsn10b696b219b2",
	"x-rapidapi-host": "indian-railway-irctc.p.rapidapi.com",
	"x-rapid-api": "rapid-api-database"
}

def train_info(trainno):
    url=f"{base_url}/{trainno}"
    res = requests.get(url,headers=headers,params=querystring)

    if res.status_code == 200:
       print("Train Details are fetched")
       data=res.json()
       return data
           
    else:
        print(f"its invalid {res.status_code}")

    
train_number="12027"

train_details=train_info(train_number)

train=train_details["body"][0]["trains"][0]

print(f"Train Name:{train['trainNumber']} \n Train Name:{train['trainName']} \n Origin : {train['origin']} ")

print(train.keys())
 