import requests

def main():
    res = requests.get('https://opendomesday.org/api/1.0/county/dby')
    places = res.json()
    print(places)

if __name__ == "__main__":
    main()