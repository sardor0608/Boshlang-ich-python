son=int(input("Son kiriting: "))
def bol(a,b):
      return a/b
while True:
   try:
      boluv=int(input("Bo'luvchini kiriting: "))
      print(bol(son,boluv))
      break
   except ZeroDivisionError:
      print("0 ga bo'lish mumkin emas!")
