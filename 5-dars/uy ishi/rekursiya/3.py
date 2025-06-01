def juft_chiqar(n):
    if n==0:
        return
    
    if n%2==0:
        print(n," ",end='')
    juft_chiqar(n-1)
            
juft_chiqar(5)
