def string(sinfo,find):
    c=0
    for s in sinfo:
        print(s)

    for s in sinfo:
        if find=='a' or find=='e' or find=='i' or find=='o' or find=='u':
            c+=1

    print("name=",sinfo,"vowels found",find,"present",c,"times")

    ss = input("enter the name")

string()    
