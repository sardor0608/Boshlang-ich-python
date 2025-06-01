def birxil_harflar(lst1,lst2):
    harf=0
    for i in range(len(lst1)):
      if lst1[i] in lst2:
          harf+=1
    return harf
print(birxil_harflar ("python", "pathon"))
