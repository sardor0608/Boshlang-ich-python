import json

def get_people():
    with open("hodimlar.json", "r") as file:
        return json.load(file)

def save_people(people):
    with open("hodimlar.json", "w") as file:
        json.dump(people,file,indent=4)

# Read
def read():
    with open("hodimlar.json", "r") as file:
        odamlar = json.load(file)
        print("_" * 40)
        print()
        print(f"|{'Ism familiya'.center(30)} | {'Yosh'.center(5)}|")
        print("_" * 40)
        for odam in odamlar:        
            print(f"|{odam['name'].center(30)} | {str(odam['age']).center(5)}|")
# Update        
def update():
    name = input("Kimni yoshini o'zgartirmoqchisiz")
    people = get_people()
    for person in people:
        if person['name'] == name:
            yosh = int(input("Yoshini kiriting"))
            person['age'] = yosh
            break
    save_people(people)

# Delete
def delete():
    name = input("Kimni o'chirish kerak")
    people = get_people()
    for person in people:
        if person['name'] == name:
            yosh = int(input("Yoshini kiriting"))
            person['age'] = yosh
            break
    save_people(people)

# Create
def create():    
    people = get_people()
    # ///
    name = input("Ism: ")
    age = input("Yoshi: ")
    skills = []
    soni = int(input("Malakangiz soni: "))
    for i in range(soni):
        skills.append(input("Malaka nomi"))
    work_experience = []
    yangi = {
        "name": name,
        "age": int(age),
        "city": "Brownmouth",
        "email": "dean05@example.org",
        "is_student": False,
        "skills":skills,
        "education": {
            "degree": input("Darajangiz"),
            "major": "business",
            "university": "Vaughn, Richmond and Schultz",
            "graduation_year": 2012
        },
        "work_experience": work_experience
    }
    
    people.append(yangi)

    save_people(people)

create()
