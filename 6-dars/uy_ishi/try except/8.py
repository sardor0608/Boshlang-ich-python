
def qiymatni_ol(lst,indx):
   return lst[indx]
n=int(input("Nechta raqam kiritmoqchisiz? "))
lst=[]
for i in range(n):
   lst.append (input(f"{i+1}chi raqamni kiriting: "))
while True:
   try:
      indx=int(input("Qaysi indexni chiqarmoqchisiz? "))
      print(qiymatni_ol(lst,indx))
      break
   except IndexError:
      print(f"Iltimos 0 va {n-1} oralig'ida index kiriting!")