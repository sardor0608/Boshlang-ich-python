def lst_q(lst)->dict:
    dct={}
    for i in range(len(lst)):
        dct[lst[i][0]]=lst[i][1:]
    return dct
print(lst_q([[1, "Jean Castro", "V"],[2, "Lula Powell", "V"],[3, "Brian Howell", "VI"],[4, "Lynne Foster", "VI"],[5, "Zachary Simon", "VII"]]))
