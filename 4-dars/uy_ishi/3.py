set1={1,2,3,4,5,6}	
set2={4,5,6,7,8,9}
y1,y2=0,0
set3=set1.intersection(set2)
set1=set1.difference(set2)
print(f"{sum(set3)-sum(set1)}")