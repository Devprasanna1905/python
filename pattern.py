  
a=1223
sum=0
while(a>0):
    rem=a%10
    sum=sum*10+rem
    a=a//10
print(sum)


rows = 6

for i in range(rows):

    for j in range(0,i+1):

        print("*", end=" ")

    print(" ")
        
for i in range(rows,0,-1):

    for j in range(0,i-1):

        print("*", end=" ") 


    print(" ")
for i in range(0,rows+1):
	for j in range(i):
	    print("*",end=" ")
	print(" ")
