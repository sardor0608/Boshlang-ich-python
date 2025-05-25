son = 15 #int(input("Son: "))

for i in range(0, son):
    for j in range(0, son):
        if i==0 or j==0 or i==son-1 or j==son-1 or j==son-i-1 or j==son-i:
            print("* ", end='')
        else:
            print("  ", end='')
    print()