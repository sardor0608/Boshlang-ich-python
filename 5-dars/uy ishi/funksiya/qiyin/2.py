def tartibla(lst)->list:
   lst1=[]
   lst2=[]
   for i in lst:
      if i%2==0:
         lst1.append(i)
      else:
         lst2.append(i)
   lst1.sort()
   lst1.reverse()
   lst2.sort()
   lst1.extend(lst2)
   return(lst1)
print(tartibla([1,2,3,4,5,6,7,8,9,10]))