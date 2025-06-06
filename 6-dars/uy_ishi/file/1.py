from random import randint
fayl=open("numbers.txt","w")
for i in range(10):
   fayl.write(f"{str(randint(1,100))} ")