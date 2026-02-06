def gcd(a,b):
    t = min(a,b)
    while t>0:
        if a%t == 0 and b%t == 0:
            return t
        t = t-1

n1 = float(input("Enter n1:"))
n2 = float(input("Enter n2:"))

print(gcd(n1,n2))