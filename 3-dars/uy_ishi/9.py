s=[(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
for i in range(len(s)-1,-1,-1):
   if s[i]==():
      s.pop(i)
print(s)
