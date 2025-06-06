import json

i = 0
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
        for s in odam['work_experience']:
            if s["end_year"]==None:
               print(f"{odam['name']}|   {s['company']} | {s['position']}")
               