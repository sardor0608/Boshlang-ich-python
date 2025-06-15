class Library:
    def __init__(self,ids,name,books=dict(),members=dict()):
        self.__id=ids
        self.__name=name
        self.__books=books 
        self.__members=members
        self.__azolar=list()
        
    def get_azolar(self)->list:
        return self.__azolar
    def get_name(self)->str:
        return self.__name
    def get_books(self)->dict:
        return self.__books

    
        
    def addBook(self,kitob,soni):
        kitoblar=self.__books
        assert isinstance(kitob,str)== True and isinstance(soni,int), "Iltimos qiymatlarni to'gri kiriting!"
        if kitob in kitoblar:
            kitoblar[kitob]+=soni
        else:
            self.__books[kitob]=soni
            
            
    def lendBook(self,xaridor,kitob)->list:
        azolar=self.get_azolar()
        kitoblar=self.get_books()
        assert kitob in kitoblar, "Kitob kutbxonada yo'q"
        if kitoblar[kitob]>0:
            self.get_azolar().append({xaridor:kitob})
            self.get_books()[kitob]-=1
        else:
            print("Kitob yetarli emas!")

                    


                
    def returnBook(self,members,books):
        kitoblar=self.get_books() 
        azolar=self.get_azolar()
        assert isinstance(members,str),"Iltimos a'zo ismini to'g'ri kiriting!"
        assert isinstance(books,str),"Iltimos kitob nomini to'g'ri kiriting!"
        assert books in kitoblar,"Bu kitob foydalanuvchiga berilmagan!"
        self.addBook(books,1)

            
                


    def chiqar(self)->str:
        for kitob in self.__books.keys():
            print( f"Kitob nomi: {kitob}, soni: {self.__books[kitob]}" )              
                
                
library = Library(1, "Central Library")
library.addBook("Python Basics", 5)
library.addBook("Qora oqqush", 5)

library.lendBook("Ali", "Python Basics")
library.lendBook("Sardor", "Python Basics")
library.lendBook("Sardor", "Qora oqqush")
print(library.get_azolar())    
print("=======")

library.returnBook("Ali", "Python Basics")
print(library.get_azolar())    

