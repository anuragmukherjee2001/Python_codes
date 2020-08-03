import math

x = int(input("Insert any number to check: "))

if x < 2:
    print("Please insert a number greater thean or equal to 2")
    quit()

elif x == 2:
    print("This is a prime number")
    quit()

y = 2
num = int(math.sqrt(x))

while y <= num:
    if x % y == 0:
        print(("This is not a prime number"))
        quit()
    y = y + 1

print("This is a prime number")        