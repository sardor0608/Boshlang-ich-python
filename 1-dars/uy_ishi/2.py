n=int(input("n kirgazing: "))
m=int(input("m kirgazing: "))
k=int(input("k kirgazing: "))
y=0
sana=0
for i in range(n,m):
   if i%2==0 and sana<=k:
      sana+=1
      y+=i
      print(i," ",end='')
print(y)