qatorlar = []
with open("mevalar.txt", "r") as file:
    qatorlar = file.readlines()

with open("natija.txt", "w") as file:
    for qator in qatorlar:
        file.write(f"{len(qator.strip())}\n")
