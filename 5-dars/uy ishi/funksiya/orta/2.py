def farq(soz,soz2):
    for i in range(len(soz)):
        if soz[i]!=soz2[i]:
            return [i]
    else:
        return -1
print(farq("Sardor","Sardor"))
