# 1, -0.5, 0.25, -0.125

x = int(input("insert number of elements in the series"))

y = 1
z = 0
sum = 0

while z < x:
    sum = sum + y
    y = y/-2
    z = z + 1

print(sum)    