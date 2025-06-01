def toq_chiqar(n):
    if n==0:
        return
    toq_chiqar(n-1)
    if n%2!=0:
        print(n," ",end='')
            
toq_chiqar(5)
