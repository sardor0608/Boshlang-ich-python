a=int(input("a son: "))
b=int(input("b son: "))
for i in range(a,b+1):
   if i%2==0:
      i*=-1
   print(i)