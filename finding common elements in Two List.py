lst1 = []

n = int(input("Enter the number of elements"))

for i in range(0,n):
    ele = int(input())
    lst1.append(ele)

print("The list is",lst1)

lst2 = []

o = int(input("Enter the number of elements"))

for i in range(0,o):
    ele = int(input())
    lst2.append(ele)

print("The list is",lst2)

lst3 = []
lst3 = [k for k in lst1 if k in lst2]
lst3.append

print("the common elements in two lists are",lst3)
