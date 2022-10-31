a = 1
b = 2

for i in range(2, 11):
    print("")
    if(a > 1):
        print(a, end=" ")
    else:
        print(a)
    for j in range(i):
        a *= 2
        print(a, end=" ")
    b += 1
    a = b
