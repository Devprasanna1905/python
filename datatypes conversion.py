a=56
#int to str
b=str(a)
#str to list 
print(list(b))
#list of string to list of int
c=list([int(x) for x in list(b)])
print(c)
#list to int 
for i in range(0,len(list(c))):
    print(c[i],end=" ")
