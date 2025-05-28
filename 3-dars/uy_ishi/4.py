lst = [1, 2, 33, 5, 6, 7, 7]
son=int(input("Son kiriting: "))
for i in range(0,len(lst)):
   for j in range(0,len(lst)):
      if lst[i]+lst[j]==son:
         print(i," ",j)
         break
