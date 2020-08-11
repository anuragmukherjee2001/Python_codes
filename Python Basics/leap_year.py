ly =[]
for i in range (1,2001):
    if (i%400 == 0 or (i%100!=0 and i%4==0)):
        ly.append(i)
print(ly)        