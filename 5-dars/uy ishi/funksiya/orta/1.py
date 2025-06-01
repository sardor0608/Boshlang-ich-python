def raqamli_ildizi(n):
    y=0
    y1=0
    y2=0
    while n!=0:
        y+=n%10
        n//=10
    while y!=0:
        y1+=y%10
        y//=10
    while y1!=0:
        y2+=y1%10
        y1//=10
    print(y2)
raqamli_ildizi(45893)
# Shu masalaga yaxshi tushina olmadim