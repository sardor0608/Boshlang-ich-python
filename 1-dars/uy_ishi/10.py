a=int(input("a son: "))
b=int(input("b son: "))
sana=0
bosh_qism=int(0)
while a!=0:
   a//=b
   bosh_qism=a%b
   a/=b
   sana+=1
print(f" A kesmada {sana} ta B bor\nBo'sh qism {bosh_qism}")