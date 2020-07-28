t=[]
for i in range(10):
    a=int(input("enter the number you want to insert in the list"))
    if(len(t)==0):
        t.append(a)
    else:
        if(a>t[len(t)-1]):
            t.append(a)
print(t)               
