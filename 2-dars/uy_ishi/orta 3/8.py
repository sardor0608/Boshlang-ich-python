a=int(input(" a sonni kiriting: "))
b=int(input(" b sonni kiriting: "))
sana=0
for i in range(b,a,-1):
   if i%2!=0 and sana!=3:
      print(i," ",end='')
      sana+=1