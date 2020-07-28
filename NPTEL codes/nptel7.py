import random
def get_gates():
    r=random.randint(0,2)
    r1=random.randint(0,2)
    while(r==r1):
        r=random.randint(0,2)
    l=['x','x','x']
    l[r]='c'
    l[r1]='c'
    ind=[0,1,2]
    for each in ind:
        if(each!=r1 and each!=r):
            l[each]='g'
    print(l)
get_gates()                