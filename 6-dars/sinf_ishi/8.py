import json  # JSON modulini import qilamiz

# Ma'lumotlarni tayyorlaymiz
talabalar = [
        {"ism": 'Ali', "yosh": None},
        {"ism": "Oygul", "yosh": 22},
        {"ism": "Hasan", "yosh": 21}
    ]

# JSON fayliga yozamiz
with open('sonlar.txt', 'w', encoding='utf-8') as fayl:
    json.dump(talabalar, fayl, indent=4)  # JSON ma'lumotlarini yozamiz
