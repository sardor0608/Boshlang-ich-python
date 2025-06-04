file=open("talabalar.txt","r")
file2=open("dostlar.txt")
qator=file.readlines()
m=len(qator[0])
soz=qator[0]
for i in qator:
   if m<len(i):
      m=len(i)
      soz=i
print(m)
print(soz)