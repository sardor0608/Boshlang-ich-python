n=int(input("Nechta maxsulot kiritasiz? "))
bozor={}
narx=0
nomi='0'
for i in range(1,n+1):
   nomi=input("Maxsulot nomi: ")
   narx=int(input("Maxsulot narxi: "))
   bozor[nomi]=narx
print(bozor)

