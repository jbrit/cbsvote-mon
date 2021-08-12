import requests

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.io)"
}

categories = [
    "fashionablemale", 
    "nextgenmale", 
    "entrepreneurmale", 
    "facemale", 
    "sociablemale",
    "sportspersonmale",
    "innovativemale",
    "fashionablefemale",
    "nextgenfemale", 
    "entrepreneurfemale", 
    "facefemale", 
    "sociablefemale",
    "sportspersonfemale",
    "innovativefemale"
]
category = "facemale"
def get_category(category=category):
    reqUrl = f"http://cbsvote.lmu.edu.ng/api/category/{category}"
    response = requests.request("GET", reqUrl, headers=headersList)
    response = response.json()
    category_data = list(map(lambda option: {"id": option["_id"]["$oid"], "name": option["name"], "votes": option["category"][0]["votes"],"category": option["category"][0]["name"],"img": option["img"]}, response))
    return category_data