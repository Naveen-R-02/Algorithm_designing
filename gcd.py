def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))

# step 1: start 
# step 2: take two integers a and b 
# step 3: while b is not 0:
#         set a = b
#          set b = a % b
# step 4: when b becomes 0, a is the gcd
# step 5: stop   