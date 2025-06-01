def sarala(lst)->dict:
   dct={}
   for i in range(len(lst)):
      dct.update(lst[i])
      for key,val in dct.items():
         if dct["age"]>18 and dct["cars"]>1:
            return dct[i]




lst=[
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]
print(sarala(lst))


