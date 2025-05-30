login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04",
}

log=input("Loginni kiriting: ")
par=input("Parolni kiritng: ")
for k,v in login.items():
   if log==k and par==v:
      print("Hisobga kirdingiz")
      break
else:
   print("Login yoki parol xato!")