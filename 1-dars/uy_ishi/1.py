y=0
p=0
for i in range(1,500):
   if i%2!=0:
      y+=i
son=y
teskari=0
while y!=0:
   teskari=teskari*10+y%10
   y//=10
print(teskari)
if son==y:
   print("palindrom")
else:
   print("palindrom emas")
