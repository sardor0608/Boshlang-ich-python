def teskarila(n):
    s=n
    if n==0:
        return
    print(n%10," ",end='')
    teskarila(s//10)

teskarila(7894)
