son=int(input("son kiriting: "))
for i in range(1,(son//2)+1):
   if son%i==0 and i%2!=0:
      print(i," ",end='')