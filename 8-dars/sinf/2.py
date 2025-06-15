class Person:
   def __init__(self,name,adress):
      self.__name=name
      self.__adress=adress


   def get_name(self)->str:
      return self.__name
   


   def get_adress(self)->str:
      return  self.__adress
   def set_adress(self,new_adress):
      if not isinstance(new_adress,str):
         raise TypeError("Qiymat faqat so'z bo'lishi kerak!")
      else:
         self.__adress=new_adress
   


   def __str__(self):
      return f"Ism: {self.__name}\nManzili: {self.__adress}"
   

class Student(Person):
   def __init__(self, name, adress,courses=[],grades=[]):
      super().__init__(name, adress)
      self.courses=courses
      self.grades=grades


   def add_course_grade(self,course,grade):
      if not course in self.courses:
         self.courses.append(course)
      if not grade in self.grades:
         self.grades.append(grade)


   

   def print_grades(self)->str:
      for i in range(len(self.grades)):
         print(f"{self.courses[i]}--{self.grades[i]}")

   def get_average_grade(self)->float:
      return sum(self.grades)/len(self.grades)
   
   def __str__(self):
      return f"Student:\n{super().__str__()}"


class Teacher(Person):
   def __init__(self, name, adress,courses=[]):
      super().__init__(name, adress)
      self.courses=courses


   def add_course(self,course):
      if not course in self.courses:
         self.courses.append(course)


   def remove_course(self,course):
      if course in self.courses:
         self.courses.remove(course)


   def print_grades(self)->str:
      print(f"Kurs: {self.courses}\n")

   def __str__(self):
         return f"O'qituvchi:\n{super().__str__()}"


s1 = Student("Ali", "Tashkent")
s1.add_course_grade("Math", 90)
s1.add_course_grade("English", 80)


print(s1)  # Student: Ali(Tashkent)
s1.print_grades()
print(f"O'rtacha baho: {s1.get_average_grade()}\n\n")


t1 = Teacher("Gulbahor", "Samarqand")
t1.add_course("Math")
t1.add_course("Physics")
# t1.remove_course("Math")



print(t1)  # Teacher: Gulbahor(Samarqand)
t1.print_grades()