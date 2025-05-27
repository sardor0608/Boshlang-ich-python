sonlar= [1,2,3,4,0,5,6,7]
min=sonlar[0]
for i in range(0,len(sonlar)):
   if min>sonlar[i]:
      min=sonlar[i]
print(min)