class Dorixona:
    
    def __init__(self, nomi: str, manzili: str) -> None:
        self.nomi = nomi
        self.manzil = manzili
        self.__dorilar = []
        self.balans = 0 



    def dori_kirit(self, nomi, narxi, soni):
        """ Dorixonaga dori qo'shish metodi"""

        assert isinstance(nomi, str), "Nomi satr bo'lishi kerak"
        assert isinstance(soni, (int, float)), "Soni int yoki float bo'lishi kerak"
        self.__dorilar.append({"nomi": nomi, "narxi": narxi, "soni": soni})



    def get_medicines_info(self)->None:
        """ Dorixonadagi dorilar va ularning ma'lumotlarini chiqarish"""

        for i in self.__dorilar:
            print(f"Nomi {i["nomi"]}, soni {i["soni"]}, narxi {i["narxi"]}")
        print(f"Dorixona balansi: {self.balans}")




    def remove_medicine(self,dori):
        """Dorixonadan dorini o'chirib tashlash"""

        for i in self.__dorilar.copy():
            if dori in i.values():
                self.__dorilar.remove(i)



    def add_money(self,add_money):
        """Dorixona balansiga pul kiritish"""

        assert isinstance(add_money,(int,float))==True and add_money>0, "Iltimis 0 dan katta raqam kiritng!"
        self.balans+=add_money
    


# Dorini sotish, sotilgan miqdorni ayirish, xaridning jami summasini hisoblash
    def sell_medicine(self,dori,soni):
      

        narx=0
        jami_sum=0
        for i in self.__dorilar:
            narx=i["narxi"]
            assert isinstance(dori,str), "To'gri qiymat kiriting!"
            if dori == i['nomi']:
               if soni<=i["soni"]:
                  i["soni"]-=soni
                  if i["soni"]==0:
                     self.__dorilar.remove(i)
                  jami_sum+=i["narxi"]*soni
                  
               else:
                  print(f"{dori} soni yetarli emas!")
               return
          
        print(f"Dorixonada {dori} mavjud emas!")

        self.add_money(narx)



# Dori narxini o'zgartirish
    def update_medicine_price(self,medicine,new_price):
        assert new_price>0,"Musbat son kiriting!"
        for dori in self.__dorilar:
            if medicine==dori["nomi"]:
               dori["narxi"]=new_price
        

#Dorixonada berilgan doridan qancha qolganini ko'rsatish
    def check_medicine_stock(self,medicine)->int:
        for dori in self.__dorilar:
            if medicine==dori["nomi"]:
                return dori["soni"]
        else:
            return 0




# Dorixonadagi jami dorilar summasini qaytaradi
    def total_medicines_value(self)->float:
        jami=0
        for dori in self.__dorilar:
            jami+=dori["narxi"]*dori["soni"]
        return jami

dorixona = Dorixona(nomi="Shifokor Dorixonasi", manzili="Toshkent, O'zbekiston")
dorixona.dori_kirit(nomi="Ibuprofen", narxi=3000, soni=30)
dorixona.dori_kirit(nomi="Paracetamol", narxi=2000, soni=50)

# dorixona.get_medicines_info()
# dorixona.remove_medicine("Paracetamol")
# print()
dorixona.get_medicines_info()
dorixona.add_money(25_000)
print()
dorixona.get_medicines_info()
print('=====')

# Output: 30 dona Ibuprofen dori qo'shildi.

dorixona.sell_medicine("Paracetamol",5)
print('=====')
dorixona.get_medicines_info()
print("=======")
dorixona.update_medicine_price("Ibuprofen",45_000)
dorixona.get_medicines_info()
print("=======")
print(dorixona.check_medicine_stock("Paracetamol"))
print("=======")
print(f"Dorixonadagi dorilarning jami summasi: {dorixona.total_medicines_value()}")




