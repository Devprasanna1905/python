def find(l):
    res=set()
    dup=set()
    for i in l:
        if(i in res):
            dup.add(i)
        else:
            res.add(i)
    return dup        
print(find([1,2,3,4,2,3]))            
