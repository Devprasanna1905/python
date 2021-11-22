a=int(input("enter the no.of rows:"))

matrix = []
for i in range(a):
   col = list(map(int, input("enter elements rowise:").split()))
   matrix.append(col)
print(matrix)
