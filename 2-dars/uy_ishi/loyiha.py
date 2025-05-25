import random
print("""Qaysi darajani tanlaysiz:
   1.oson
   2.o'rta
   3.qiyin
   0.chiqish""")
son=int(input("(0-3) oraliqda son kiriting: "))
while True:
   if son>=0 and son<=3:
      if son==1:
        print("Oson o'yin")
        boshi=1
        oxiri=5
        break
      elif son==2:
         print("O'rta o'yin")
         boshi=10
         oxiri=20
         break
      elif son==3:
         print("qiyin o'yin")
         boshi=30
         oxiri=50
         break
      elif son==0:
         print("O'yindan chiqildi!")
         break
   else:
      son=int(input("Xato daraja, qyata kiritng:  "))
sana=0
for i in range(1,4):
   if son==0:
      break
   son1=random.randint(boshi,oxiri)
   son2=random.randint(boshi,oxiri)
   amal=random.choice(["-","+","*","//"])
   if amal=="-":
      javob=int(input(f"Javobni yozing: {son1}-{son2}="))
      if javob==(son1-son2):
         print("To'g'ri javob🫡")
         sana+=1
      else:
         print("""Xato kiritdingiz❌
   To'g'ri javob: """,son1-son2)
   elif amal=="+":
      javob=int(input(f"Javobni yozing: {son1}+{son2}="))
      if javob==(son1+son2):
         print("To'g'ri javob🫡")
         sana+=1
      else:
         print("""Xato kiritdingiz❌
   to'g'ri javob: """,son1+son2)
   elif amal=="*":
      javob=int(input(f"Javobni yozing: {son1}*{son2}="))
      if javob==(son1*son2):
         print("To'g'ri javob🫡")
         sana+=1
      else:
         print("""Xato kiritdingiz❌
   To'g'ri javob: """,son1*son2)
   else:
      javob=float(input(f"Javobni yozing: {son1}/{son2}="))
      if javob==(son1/son2):
         print("To'g'ri javob🫡")
         sana+=1
      else:
         print("""Xato kiritdingiz❌
   To'g'ri javob: """,son1/son2)
if son!=0:
   print(f"3 ta misoldan {sana} tasi to'g'ri")




