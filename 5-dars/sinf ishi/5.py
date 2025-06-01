
def factorial (son)->list:
    lst=[]
    for i in range(2,son):
        if son%i==0:
            lst.append(i)
    return lst
    

print(factorial(10))
