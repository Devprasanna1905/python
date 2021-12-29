                                                                   #interview problems
#1 to check element is there in list
f=[1,2,3]
t=1
print(t in f)#can be done using linear search too

#2 find duplicate in list
l=[1,2,3,3]
seen=[]
for i in l:
    if i in seen:
        print(i,end=" ")
    else:
        seen.append(i)
        
#3 to check anagrams
s1="Hello"
s2="holle"
if sorted(s1.lower())==sorted(s2.lower()):
    print(True)
else:
    print(False)

#4 remove duplicates in a list
a=[1,2,3,4,4]
print(set(a))

#5 integer pair sum in a list
l=[1,2,3,2]
k=4
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==k:
            print(l[i],l[j])

#6 check if string is palindrome
s="madam"
if s==s[::-1]:
    print(True)
else:    
    print(False)    
   
#7  list as stack ,queue

l=[1,2,3,4]
#as stack
l.append(1)
l.pop()
print(l)
#as queue
l.insert(0,5)
l.pop()
print(l)

#8 missing number in a list from n to n
l=[1,2,3,5,4,10]
l1=list(map(int,range(min(l),(max(l)))))
for i in l1:
    if i not in l:
        print(i)
#9 intersection of two lists
l1=[1,2,3,5]
l2=[3,4,5]
for i in l1:
    if i in l2:
        print(i,end=" ")
        
# or print(set(l1)&set(l2))        


