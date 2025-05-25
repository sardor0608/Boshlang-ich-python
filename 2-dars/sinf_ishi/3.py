import random


son = random.randint(0, 100)
print(son)

fson = None
count = 3

while fson != son and count != 0:
    print(f"Sizda {count} ta urinish qoldi")
    fson = int(input("Son kiriting: "))
    
    if fson > son:
        print("Siz kiritgan son katta")
    else:
        print("Siz kiritgan son kichik")

    count -= 1

if fson == son:
    print("Siz topdingiz")
else:
    print("Siz yutqazdingiz")
