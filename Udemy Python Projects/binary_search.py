from random import random

n = int(input("Enter how many numbers you want to enter "))

arr = []

for x in range(n):
    arr.append(int(random()*100))

arr.sort()

print(arr)

num = int(input("Search for any number in array: "))

mini = 0
maxi = n-1

while mini <= maxi:
    mid = (mini + maxi) // 2
    if num < arr[mid]:
        maxi = mid-1
    elif num > arr[mid]:
        mini = mid + 1
    else:
        print("The number is located at position: ",mid+1)
        break

else:
    print("There is no such number")   
             