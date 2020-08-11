lst = []

n = int(input("Enter the number of elements"))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)


print("the list is :", lst)
lst.sort()
print("the list now is ", lst)


