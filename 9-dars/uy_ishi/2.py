class Cinema:
   def __init__(self,id,name,movies=dict(),income=0):
      self.__name=name
      self.__movies=movies
      self.__id=id
      self.__income=income


   def chiqar(self)->str:
      """Kinoteatr nomi, ID si, mavjud filmlar va sotilgan chiptalarning umumiy narxini qaytaradi!"""
      return f"Kinoteatr nomi: {self.__name}\nKinoteatr ID si: {self.__id}\nMavjud filmlar: {self.__movies}\nSotigan chiptalarning umumiy narxi: {self.__income}"

   def get_name(self)->str:
      """Kinoteatrning nomini qaytaradi!"""
      return self.__name
   
   def get_income(self)->int:
      """Kinoteatrda sotilgan jami chiptalar narxini qaytaradi!"""
      return self.__income
   

   def get_movies(self)->dict:
      """Kinoteatrda mavjud filmlarni qaytaradi!"""
      return self.__movies



   def addMovie(self,film,joyi):
      """Kinoteatrga yangi film qo'shadi, agar bo'lsa bo'sh joyni ko'paytiradi!"""
      if film in self.__movies:
         self.__movies[film]+=joyi
      else:
         self.__movies.update({film:joyi})



   def sellTicket(self,kino,soni,narxi):
      """Ko'rsatilgan film uchun ko'rsatilgan narxda ko'rsatilgan chiptani sotadi va sotilgan umumiy narxa qo'shib qo'yadi"""


      assert kino in self.__movies,f"Bunday film mavjud emas"
      if self.__movies[kino]>=soni:
         self.__movies[kino]-=soni
         self.__income+=soni*narxi
      else:
         print(f"Joy yetarli emas\n"
               f"Mavjud joy: {self.__movies[kino]}")

   def checkAvailability(self,move)->int:
      """So'ralgan filmdagi bo'sh joylar sonini qaytaradi"""

      assert move in self.__movies, "Bunday film mavjud emas!"
      return self.__movies[move]

   
kino=Cinema(1,"Ilm")
kino.addMovie("Qasoskorlar",30)
print(kino.get_movies())
print("=======")
kino.addMovie("Qasoskorlar",20)
print(kino.get_movies())
print("=======")
kino.addMovie("Forsaj",20)
print(kino.get_movies())
print("=======")
print(kino.checkAvailability("Forsaj"))
print("=======")
kino.sellTicket("Forsaj",19,25_000)
print(kino.get_movies())
print("=======")
print(kino.get_income())
print("=======")
kino.sellTicket("Qasoskorlar",60,20_000)
print(kino.get_movies())
# print("=======")
# print(kino.get_income())
# print("=======")


# print(kino.chiqar())