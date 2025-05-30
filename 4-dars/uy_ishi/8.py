set1={"Artel","Alif","Yandex", "Google", "Meta"}
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}
set3=set2.intersection(set3,set1,set2)
print(set3)
set1=set1.difference(set3)
print(set1)