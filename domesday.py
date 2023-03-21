import requests

def get_manor_ids(placeId):
    res = requests.get('https://opendomesday.org/api/1.0/place/'+str(placeId))
    data = res.json()
    if 'manors' in data.keys():
        return data['manors']
    else:
        return []