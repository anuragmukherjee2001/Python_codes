lst = []

n = int(input("Enter the number of elements"))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print("The list is",lst)
    
a = max(lst)
b = min(lst)
print("the Biggest element in the list is ",a)
print("the smallest element in the list is",b)
