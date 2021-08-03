def binary(array, x):
    first = array[0]
    last = len(array) - 1
    midpoint = 0
    while first <= last:
        midpoint = (first + last) // 2
        if array[midpoint] < x:
            first = midpoint + 1
        elif array[midpoint] > x:
            last = midpoint - 1
        else:
            return midpoint
    return -1

x=int(input()) 
array = list(map(int ,input().split(" ")))
result = binary(array, x)
 
if result != -1:
    print("Element is present at index", (result))
else:
    print("Element is not present in array")
