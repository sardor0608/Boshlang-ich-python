from random import randint

with open("sonlar.txt", "w") as file:
    for i in range(10):
        son = randint(1, 10)
        file.write(f"{son} ")
