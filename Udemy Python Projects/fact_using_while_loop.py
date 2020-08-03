x = abs(int(input("Enter any number ")))

fact = 1

while x > 1:
    fact = fact * x
    x = x - 1
print("The value of the factorial is ", fact)