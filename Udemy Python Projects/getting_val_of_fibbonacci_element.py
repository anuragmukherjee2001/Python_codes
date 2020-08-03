x = abs(int(input("Enter an element vto find its value ")))

f1 = f2 = 1

y = 2

while y < x:
    f1, f2 = f2, f1 + f2
    y = y + 1
print("The value of the fibonacci number in that position is ", f2)    