bins={}
def mbin():
    max_=0
    max_i=-1
    for each in bins:
        if(bins[each]>max_):
            max_i=each
            max_=bins[each]
    print(max_i)
    return max_i

    
while(len(bins)>0):
    b=mbin()
               