import random

soz=random.choice(["pul","dastur","fronted","bacend"])
print(soz)
q_soz=input("Qidirilayotgan harfni kiriting: ")
bormi=0
sana=5
lst=[]
while True:
   for i in soz:
      if q_soz==i:
         bormi+=1
         break
   if bormi>0:
      for i in range(0,len(lst)):
         if lst[i]==q_soz:
            print("Siz ilgari bu harfni kirgazgansiz!")
      print(f"Harf so'zda bor\nUrinishlar {sana}")
      q_soz=input("So'z kiriting: ")
      
      lst.append(q_soz)
   elif sana==0:
      print("Siz yutqazdingiz!")
      break
   else:
      for i in range(0,len(lst)):
         if lst[i]==q_soz:
            print("Siz ilgari bu harfni kirgazgansiz!")
      print(f"Bunday harf so'zda yo'q\nUrinishlar {sana}")
      q_soz=input("So'z kiriting: ")
      lst.append(q_soz)
      sana=sana-1
print(lst)