file = open("fayl1.txt", "r")
qatorlar = file.readlines()
maks = len(qatorlar[0])
index = 0
i = 0

for qator in qatorlar:
    if len(qator) > maks:
        maks = len(qator)
        index = i
    i += 1
print(maks)
print(qatorlar[index])
print(index+1)

file.close()
