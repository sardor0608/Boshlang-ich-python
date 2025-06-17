class Library:
    def __init__(self,ids,name,books=dict(),members=dict()):
        self.__id=ids
        self.__name=name
        self.__books=books 
        self.__members=members
        


    def get_azolar(self)->list:
        return self.__members
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
        assert kitob in self.__books, "Kitob kutbxonada yo'q"
        if self.__books[kitob]>0:
            if xaridor in self.__members:
                self.__members[xaridor].append(kitob)
            else:
                self.__members[xaridor] = [kitob]
            self.__books[kitob]-=1
        else:
            print("Kitob yetarli emas!")

                    

                
    def returnBook(self,member,book):
        assert isinstance(member,str),"Iltimos a'zo ismini to'g'ri kiriting!"
        assert isinstance(book,str),"Iltimos kitob nomini to'g'ri kiriting!"
        self.addBook(book,1)
        for key, value in self.__members.items():
            if key == member:
                if book in value:
                    value.remove(book)
                    break
        if not self.__members[member]:
            del self.__members[member]

            
                
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