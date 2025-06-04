import json

with open("sonlar.txt", "r") as file:
    obj = json.load(file)
    print(obj['talabalar'][0]['yosh'])
