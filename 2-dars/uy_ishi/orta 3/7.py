a=int(input(" a sonni kiriting: "))
b=int(input(" b sonni kiriting: "))
for i in range(a,b):
   for j in range(2,i//2+1):
      if i%j==0:
         break
      print(i," ",end='')
      break
