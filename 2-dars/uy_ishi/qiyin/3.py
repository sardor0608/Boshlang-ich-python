a=int(input(" a sonni kiriting: "))
b=int(input(" b sonni kiriting: "))
for i in range((a*2),(b*2)+1):
   if i%2==0:
      belgi=i
      teskari=0
      while i!=0:
         teskari=teskari*10+i%10
         i//=10
      print(f"juft son {belgi}, teskarisi: {teskari}")