n=int(input("Nechta raqam kiritmoqchisiz? "))
lst=[]
while  True:
    try:
        for i in range(n):
            lst.append (input(f"{i+1}chi raqamni kiriting: "))
        indeks=int(input("Qaysi indeksdagi raqamni chiqarmoqchisiz? "))
        print(lst[indeks])
        break
    except IndexError:
        print(f"Iltimos 0 va! {n-1} oralig'ida index kiriting!")
    except ValueError:
        print("Iltimis faqat son kiritng!")
