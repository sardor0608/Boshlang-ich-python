class Developer:
   def __init__(self,surname,position,salary):
      self.__surname=surname 
      self.__position =position 
      self.__salary=salary 
   
   def get_surname(self)->str:
      return self.__surname
   
   def get_position(self)->str:
      return self.__position
   
   def get_salary(self)->str:
      return self.__salary
   
class SoftwareEngineer(Developer):
   def __init__(self, surname, position, salary,bonus,department):
      super().__init__(surname, position, salary)
      self.__bonus=bonus
      self.__department=department


   def umumiy_summa(self)->int:
      return self.__bonus+self.get_salary()


   def bolim(self)->int:
      return self.__department
   
lst=[]
n=2
print(f" {n} ta hodim malumotini to'ldiring\n")
for i in range(n):
   ism=input(f"{i+1} chi hodim ismi: ")
   mansab=input(f"{i+1} chi hodim mansabi: ")
   oylik=input(f"{i+1} chi hodim oyligi: ")
   bonus=input(f"{i+1} chi hodim bonusi: ")
   bolim=input(f"{i+1} chi hodim Bo'limi: ")
   h1=SoftwareEngineer(ism,mansab,oylik,bonus,bolim)
   lst.append(h1.umumiy_summa)


dct={}
for i in lst:
   dep=i.bolim
   if dep not in dct:
      dct[dep]={
         "soni":0,
         "jami_summasi":0
         }
      dct[dep]["soni"]+=1
      dct[dep]["jami_summasi"]=i.umumiy_summa()
print(dct)








