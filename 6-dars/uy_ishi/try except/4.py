ish_stavkasi=int(input("Ish soatlarini kiritng: "))
while True:
   try:
      soatlik_maosh=int(input("Soatlik maoshingizni kiriting: "))
      ortiqcha_soat=0
      if ish_stavkasi>40:
         ortiqcha_soat=ish_stavkasi-40
         print(f"To'lov {(ish_stavkasi-ortiqcha_soat)*soatlik_maosh+ortiqcha_soat*(soatlik_maosh*2.5)}")
         break
      else:
         print(f"To'lov {ish_stavkasi*soatlik_maosh}")
         break
      
   except ValueError:
      print("Iltimos raqam kiritng!")
   except:
      print("Qandaydir xatolik, qayta kiritng!")
