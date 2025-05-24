s=0
for i in range(100,1000):
   while i!=0:
      if s==3:
         print(i)
      s=i%10
      i//=10


