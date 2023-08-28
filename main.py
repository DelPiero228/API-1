import requests
import json

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)


names_of_characters = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}
sorted_intelligence = dict(sorted(intelligence.items()))
for names in names_of_characters:
    for character in response.json():
        if character['name'] in names_of_characters:
            intelligence[character['powerstats']['intelligence']] = character['name']
print(intelligence)