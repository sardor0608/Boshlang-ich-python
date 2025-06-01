def musbat_list (dic1)->dict:
    dic={}
    for key,v in dic1.items():
        dic[key]=v.upper()
    return dic
    

print(musbat_list({"Ism": "Ali", "Familya": "Kamolov", "Manzil": "Angren shahri"}))
