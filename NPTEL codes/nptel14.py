def find(list1,num):
    for each in list1:
        if(each!=num):
            print(each)
        else:
            break

t = []
for i in range(30):
    t.append(i)

find(t,29)                