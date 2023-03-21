# Python TD8/9 

## Exercise 1: Working directory

1. `mkdir td4`, `cd td4`
2. `git init`
3. `sudo apt-get install python3-pip`
4. `pip3 install VirtualEnv`
5. `virtualenv .env`
6. A new folder `.env` was created
7. `source .env/bin/activate`, `(.env)` is now written at the beginning
8. This is not a good idea, every user who forks the repo should be able to initialize his environment himself. If packages are installed and updated there is no point to commit these files to Git.
9. `nano .gitignore`, added line `.env` 
10. Gits want me to commit the `.gitignore` file now.
11. `git commit -m "Added .gitignore"`

## Exercise 2: Python Script

1. `pip install Requests`
2. `nano script.py`
```python
import requests

def main():
    res = requests.get('https://opendomesday.org/api/1.0/county/dby')
    county = res.json()
    places = county['places_in_county']
    print(places)

if __name__ == "__main__":
    main()
```
3. `git add script.py`, `git commit -m "Added script.py"`

## Exercise 3: Python Module

1. `nano domesday.py`
```python
import requests

def get_manor_ids(placeId):
	res = requests.get('https://opendomesday.org/api/1.0/place/'+placeId)
	data = res.json()
	if  'manors'  in data.keys():
		return data['manors']
	else:
		return []
```
2. `.env/bin/python3 domesday.py`
3. `.env/bin/python3`, `import domesday`, `domesday.get_manor_ids(1036)`, `exit()`

## Exercise 4: Python Program

Files are in Github
