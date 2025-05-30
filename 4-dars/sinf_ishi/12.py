shaxslar = [
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]
for i in shaxslar:
   for j in i.keys():
      if i["age"]>18 and i["cars"]>1:
         print(i["Name"])
         break