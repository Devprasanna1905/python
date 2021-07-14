import random
lower=int(input("enter the lower range"))
upper=int(input("enter the upper range"))
num=int(input("enter the number of random numbers"))
for i in range(0,num):
    print(random.randint(lower,upper),end=" ")
    
