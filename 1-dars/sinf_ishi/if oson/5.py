son=int(input("Son kiriting: "))
if son%3==0 and son%5!=0:
   print("Fizz")
elif son%5==0 and son%3!=0:
   print("Buzz")
elif  son%5==0 and son%3==0:
   print("FizzBuzz")