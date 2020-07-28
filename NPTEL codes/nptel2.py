# for i in range(100):
#     if(i%10==0):
#         print(i)

# list = ["hi","we","are","the","elements","in","a","list"]
# for i in range(4):
#     print(list[i])

# def add(int a,int b):
#     print(a+b)
# add(2,3)  

import random

# word = "lion"
# join(random.sample(word))  
word = input("enter a word in which no letter is repeated")
l = []
total = 1
for i in range(1,len(word)+1):
    total = total + i
while(len(l)<total):
    j="".join(random.sample(word,len(word)))
    l.append(j)
for each in l:
    print(each)        