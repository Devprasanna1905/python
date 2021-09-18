def intersection(l1,l2):
    return list(set(l1) & set(l2))
print(intersection([1,2,3],[1,2]))  

#another method
res=[]
    for i in l1:
        if i in l2:
            res.append(i)
    return res 
