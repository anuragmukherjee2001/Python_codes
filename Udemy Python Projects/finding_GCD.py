x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

while x != 0 and y!= 0:
    if x > y:
        x %= y
    else:
        y %= x

gcd = x + y

print("The greatest common divisor is ", gcd)
