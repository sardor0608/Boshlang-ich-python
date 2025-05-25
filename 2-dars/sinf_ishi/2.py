import random

count = 0
xato = 0
for i in range(1,6):
    son = random.randint(1,10)
    son1 = random.randint(1,10)
    amal = random.choice(["+","-","*","//"])
    if amal == "+":
        natija = son + son1
    elif amal == "-":
        natija == son - son1
    elif amal == "*":
        natija = son * son1
    else:
        natija = son // son1
    fson = int(input(f"{son} {amal} {son1} = "))
    if natija == fson:
        print("tog'ri")
        count+=1
    else:
        print("xato")
        xato +=1 
print(f"{count} togri javob,{xato} xatolar")
