l = [[1,2,3],[4,5,6],[7,8,9]]
f = l
for j in range(3):
    if(f==l):
        for i in range(3):
            print(l[i][j],end=" ")
            f=0
    if(f==0):
        for i in range(2,-1,-1):
            print(l[i][j],end=" ")
            f=l        