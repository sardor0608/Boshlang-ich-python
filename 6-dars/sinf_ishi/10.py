import json

i = 0
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        if odam['education']['graduation_year']>=2020:
            print(f"{odam['name']} {odam['age']} {odam['education']['university']}")
            