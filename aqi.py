import requests
import json  

with open('TOKEN.json', "r", encoding="utf8") as jsonf:
    jdata = json.load(jsonf)

def now_aqi():
    url = "https://data.moenv.gov.tw/api/v2/AQX_P_432"
    params = {
        "format": "json",
        "api_key": jdata["apikey"],
        "filters": "SiteName,EQ,大里",
    }

    r = requests.get(url,params=params)
    return r.json()[0].get("aqi")
