import json
lst=[]
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
         lst.append(odam['city'])
    for odam in odamlar:
         for i in range(len(lst)):
            if lst[i] in odam['city']:
               print(f"{odam['name']}|   {odam['city']}")
               