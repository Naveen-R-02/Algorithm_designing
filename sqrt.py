# n = int(input("Enter number:"))
# sqrt_n = float(n**0.5)
# print(sqrt_n)

n = int(input("Enter n:"))
a = 0.0000001
while a*a<n:
    a=a+0.0000001
print(a)

