def eng_yaqin_son  (lst,k):
    k=[x for x in lst if x<k]
    if k:
        return max(k)
    else:
        return  None

print(eng_yaqin_son([1,6,3,9,11],8))
