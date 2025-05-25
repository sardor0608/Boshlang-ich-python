n=int(input(" n sonni kiriting: "))
m=int(input(" m sonni kiriting: "))
y=0
for i in range(n,m+1):
   for j in range(2,(i//2)+1):
      if i%j==0:
         break
      else:
         print(i)
         y+=i
         break
print("Yig'indi:",y)
   