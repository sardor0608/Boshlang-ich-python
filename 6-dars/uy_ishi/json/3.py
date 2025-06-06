import json
konikma=input("Qanday ko'nikmaga ega bo'lgan odamlarni chiqarmoqchisiz? ")
i = 0
with open("hodimlar.json", "r") as file:
    odamlar = json.load(file)
    for odam in odamlar:
         for i in odam['skills']:
            if konikma in i:
               print(f"{odam['name']}  |  {odam['skills']}")

               