def Miss(x): 
    n = len(x) 
    total = (n + 1)*(n + 2)/2
    sum_of_x = sum(x) 
    return total - sum_of_x 
  
 
x = [] 
  
 

  
 
for i in range(0, 4): 
    ele = int(input()) 
  
    x.append(ele)  
miss = Miss(x) 
print(int(miss)) 
