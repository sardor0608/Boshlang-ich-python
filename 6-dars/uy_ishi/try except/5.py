while True:
   try:
      # ball<=100
      ball=int(input("Ballarni kiritng: "))
      if 100>ball>=90:
         print('A')
         break
      elif 90>ball>=80:
         print('B')
         break
      elif 80>ball>=70:
         print('C')
         break
      elif 70>ball>=60:
         print('D')
         break
      elif ball<60:
         print('F')
         break
      else:
         print("Iltimos 0 va 100 oralig'ida son kiritng!")
   except ValueError:
      print("Iltimos raqam kiritng!")
      
