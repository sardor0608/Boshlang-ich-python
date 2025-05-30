n=int(input("Nechta maxsulot kiritmoqchisiz? "))
meva={}
for i in range(1,n+1):
   nomi=input(f"{i} chi meva nomi: ")
   narxi=int(input(f"{i} chi meva narxi: "))
   meva.update({nomi:narxi})
maxsulot=input("Qaysi maxsulotni qidirayabsiz? ")
for key,val in meva.items():
   if key==maxsulot:
      print(f"{key} narxi:  {val}")
      break
else:
   print("Bu meva ro'yxatda yo'q")