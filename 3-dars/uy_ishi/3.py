list1=['salom',123,True,'Hayr','world',3.14,'7214']
text=[]
other=[]
for str0 in list1:
   if isinstance(str0,str)==True:
      text.append(str0)
   else:
      other.append(str0)
text.sort()
other.sort()
other.reverse()
print(text)
print(other)