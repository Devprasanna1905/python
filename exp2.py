import random
lower=int(input("enter the lower range"))
upper=int(input("enter the upper range"))
num=int(input("enter the number of random numbers"))
for i in range(0,num):
    print(random.randint(lower,upper),end=" ")
    
terms = int(input("number of terms "))
n1, n2 = 0, 1
count = 0
x=int(input("enter the value of x:"))

if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("invalid")
else:
   while count < terms:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       if(x==nth):
           print("largest number smaller than x",n1)
           print("smallest number larger than x",n1+nth)

items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
