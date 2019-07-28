import requests

URL = "https://api.noopschallenge.com/wordbot"
#PARAMS = {"count": 10, "set": }

# r = requests.get(url = URL, params = PARAMS)

#data = r.json()

#print(data)

def get_sets():
    turl = "https://api.noopschallenge.com/wordbot/sets"
    r = requests.get(url=turl)
    data = r.json()
    return data

sets = get_sets()

for item in sets:
    print(item)
