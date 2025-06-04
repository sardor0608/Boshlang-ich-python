royxat=[1,2,3,4]
while True:
   try:
      ind=int(input("Index kiritng: "))
      print(royxat[ind])
      break
   except IndexError:
      print(f"0 va {len(royxat)-1} oralig'ida son kiriting")
   except ValueError:
      print("Faqat son kiritng")
   except:
      print("Qandaydir xatolik!")
      break