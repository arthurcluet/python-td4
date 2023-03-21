import requests
import domesday

def main():
    res = requests.get('https://opendomesday.org/api/1.0/county/dby')
    county = res.json()
    manors = domesday.get_manor_ids(county['places_in_county'][0]['id'])
    print(manors)

if __name__ == "__main__":
    main()