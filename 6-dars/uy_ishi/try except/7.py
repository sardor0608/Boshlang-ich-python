try:
   def sonni_ol(s)->int:
      return int(s)
   s=input("Son kiriting: ")
   print(sonni_ol(s))
except ValueError:
   print(f"{s} ni songa o'girib bo'lmadi")