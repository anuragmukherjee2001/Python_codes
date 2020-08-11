lst = []

n = int(input("Enter the number of elements"))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print("The list is",lst)

j = int(input("enter the elements to find the number of occurances"))

k = lst.count(j)

print("The number of times the element occured in the list is ",k)
