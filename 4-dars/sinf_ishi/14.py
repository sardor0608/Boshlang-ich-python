n=int(input("Nechta maxsulot kiritmoqchisiz? "))
meva={}
for i in range(1,n+1):
   nomi=input(f"{i} chi meva nomi: ")
   narxi=int(input(f"{i} chi meva narxi: "))
   meva.update({nomi:narxi})
narx=int(input("Necha pulgacha bo'lgan maxsulotlar kerak? "))
for key,val in meva.items():
   if val<narx:
      print(f"{key} narxi: {val}")