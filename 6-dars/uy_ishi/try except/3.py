while True:
    try:
        son1=int(input("Birinchi sonni kiriting: "))
        son2=int(input("Ikkinchi sonni kiritng: "))
        print(f"{son1} / {son2} = {son1/son2}")
        break
    except ValueError :
        print("iltimos faqat son kiritng!")
    except:
        print("Qandaydir xatolik, qayta kiritng!")
