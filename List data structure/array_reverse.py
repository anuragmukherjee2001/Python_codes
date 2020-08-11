
# Reversing a list using reversed() 

lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 




def Reverse(lst): 
    return [ele for ele in reversed(lst)] 
      
# # Driver Code 
# # lst = [10, 11, 12, 13, 14, 15] 
# print(lst)
# # print(Reverse(lst)) 
c = Reverse(lst)
print(c)
res_list = [lst[i] + c[i] for i in range(len(c))]
# # d = lst + c
print(res_list)