s1 = input("enter  astring")
s2 = input("enter another string")

for each in list(s2):
    for each2 in list(s1):
        if(each == each2):
            print("yes")
        else:
            print("no")    
            break