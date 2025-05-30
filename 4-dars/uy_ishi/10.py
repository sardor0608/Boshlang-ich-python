set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}
for i in set1.copy():
   if i<60:
      set1.remove(i)
for i in set2.copy():
   if i<60:
      set2.remove(i)
set1=set1.intersection(set2)
print(sum(set1)//len(set1))
