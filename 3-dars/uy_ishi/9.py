s=[(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
for i in s:
   if i==():
      s.remove(i)
print(s)
