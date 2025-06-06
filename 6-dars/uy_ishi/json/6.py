import json

i = 0
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        for s in odam['work_experience']:
            if odam["age"]>=40:
               print(f"{odam['name']}|   {odam['city']}  | {s['position']}")

               