n=int(input(" n sonni kiriting: "))
m=int(input(" m sonni kiriting: "))
k=int(input(" k sonni kiriting: "))
y=0
sana=0
for i in range(n+k,m+k+1):
   if i%k!=0:
      y+=i
      sana+=1
      if sana==1:
         print(f"({i}+",end='')
      elif sana==(m+k+1)-(n+k):
         print(f"{i})",end='')
      else:
         print(f"{i}+",end='')
print(y)