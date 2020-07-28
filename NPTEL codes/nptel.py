a = int(input("enter the value of a"))
b = int(input("enter the value of b"))

for i in range(1,101):
    if(i%a==0):
        if(i%b!=0):
            print("fizz")
    else:                           
        if(i%a!=0):
            print("buzz")
        else:
            print("fizzbuzz")        