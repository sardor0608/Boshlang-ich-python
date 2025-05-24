son=int(input("son: "))
teskari=0
while son!=0:
   teskari=teskari*10+son%10
   son//=10
if son>=teskari:
   print("Farqi ",son-teskari)
print(teskari)