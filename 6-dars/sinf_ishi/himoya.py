def toqlar(lst)->int:
   y=0
   for i in lst:
      if i%2!=0:
         y+=i
   return y
# print(toqlar([1,2,3,4,5,6,7]))

#  FILTER ga oid masala
lst=[1,2,3,4,5,6,7]
print(sum(list(filter(lambda x:x%2!=0, lst))))


#  MAP ga oid masala
print(list(map(lambda x:x*2,lst)))