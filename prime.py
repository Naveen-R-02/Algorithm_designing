n = int(input("Enter n:"))
i = 2
print("Prime Factors are")
while n>1:
    while n%i == 0:
        print(i)
        n//=i
    i += 1
