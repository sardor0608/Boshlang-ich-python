d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key,v in d2.items():
   if key in d1.keys():
      d1[key]=d1.values+d2.values
   # else:
   #    d1.update(d2)