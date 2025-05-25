son=(int(input("son kiriting: ")))
y=0
belgi=son
while son!=0:
   y+=son%10
   son//=10
print(belgi%y)