x = int(input("Enter the number "))

even = 0
odd = 0

while x > 0:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    x = x//10 
print("Even number ", even)
print("Odd number ", odd)           