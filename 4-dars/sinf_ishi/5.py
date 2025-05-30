words = {"apple", "banana", "cherry", "kiwi"}
for i in words.copy():
   if len(i)>5:
      words.remove(i)
print(words)