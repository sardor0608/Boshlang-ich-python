import os

class ToDoList:
    def __init__(self, fayl_nomi="todo_list.txt"):
        self.fayl_nomi = fayl_nomi
        self.vazifalar = []
        self.yukla()

    def yukla(self):
        """Vazifalar ro'yxatini fayldan yuklaydi."""
        if os.path.exists(self.fayl_nomi):
            with open(self.fayl_nomi, "r") as fayl:
                for qator in fayl:
                    nom, holat = qator.strip().split(", ")
                    self.vazifalar.append({"nom": nom, "bajarildi": holat == "True"})

    def saqlash(self):
        """Vazifalar ro'yxatini faylga yozadi."""
        with open(self.fayl_nomi, "w") as fayl:
            for vazifa in self.vazifalar:
                fayl.write(f"{vazifa['nom']}, {vazifa['bajarildi']}\n")

    def vazifa_qosh(self, nom):
        """Yangi vazifa qo'shadi."""
        self.vazifalar.append({"nom": nom, "bajarildi": False})
        print(f"Vazifa qo'shildi: {nom}")
        self.saqlash()

    def vazifalarni_korish(self):
        """Vazifalar ro'yxatini ko'rsatadi."""
        if not self.vazifalar:
            print("Vazifalar ro'yxati bo'sh!")
            return
        print("\nVazifalar:")
        for i, vazifa in enumerate(self.vazifalar, 1):
            holat = "✅" if vazifa["bajarildi"] else "❌"
            print(f"{i}. {vazifa['nom']} - {holat}")

    def bajarilgan_ozgartir(self, indeks):
        """Vazifaning holatini bajarilgan deb belgilaydi."""
        if 0 <= indeks < len(self.vazifalar):
            self.vazifalar[indeks]["bajarildi"] = not self.vazifalar[indeks]["bajarildi"]
            print(f"Vazifa holati o'zgartirildi: {self.vazifalar[indeks]['nom']}")
            self.saqlash()
        else:
            print("Noto'g'ri indeks!")

    def vazifa_ochir(self, indeks):
        """Vazifani ro'yxatdan o'chiradi."""
        if 0 <= indeks < len(self.vazifalar):
            ochirilgan = self.vazifalar.pop(indeks)
            print(f"Vazifa o'chirildi: {ochirilgan['nom']}")
            self.saqlash()
        else:
            print("Noto'g'ri indeks!")
class Bajar(ToDoList):
    def bajarilgan(self):
        pass
    


    def bajarilmagan(self):
        pass



   
# Loyihani boshqarish
todo = ToDoList()
bajar=Bajar()

while True:
    print("\n[1] Vazifalarni ko'rish\n[2] Vazifa qo'shish\n[3] Bajarilgan deb belgilash\n[4] Vazifani o'chirish\n[5] Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        todo.vazifalarni_korish()
    elif tanlov == "2":
        nom = input("Yangi vazifa nomini kiriting: ")
        todo.vazifa_qosh(nom)
    elif tanlov == "3":
        indeks = int(input("Bajarilgan deb belgilash uchun vazifa indeksini kiriting: ")) - 1
        todo.bajarilgan_ozgartir(indeks)
    elif tanlov == "4":
        indeks = int(input("O'chirish uchun vazifa indeksini kiriting: ")) - 1
        todo.vazifa_ochir(indeks)
    elif tanlov == "5":
        print(f"Bajarilganlar ro'yxati: {bajar.bajarilgan}")

    elif tanlov=="6":
        pass
    else:
        print("Noto'g'ri tanlov!")
