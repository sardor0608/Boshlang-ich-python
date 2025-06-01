def birlashtir(list1,list2)->dict:
    dct={}
    for i in range(len(list1)):
        dct[list1[i]]=list2[i]
    return dct
list1 = ["Jon", "Jeyms", "Piter", "Tony"]
list2 = ["Vik", "Bond", "Parker", "Stark"]
print(birlashtir(list1,list2))