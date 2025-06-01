def musbatlar_son (list1)->list:
    lst=[]
    for i in list1:
        if i>0:
            lst.append(i)
    return lst
    

print(musbatlar_son([1, -1, 2, 9, -3, -11, 20, 5, -8, 4]))
