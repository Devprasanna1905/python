'''def sort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if(array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
data=[1,12,10,14,7,2]
(sort(data))
print(data)'''

'''def sort(list):
    for i in range(len(list)):
        value=list[i]
        j=i-1
        while j>=0:
            if(value<list[j]):
                list[j+1]=list[j]
                list[j]=value
                j=j-1
            else:
                break
                
data=[1,12,10,14,7,2]            
sort(data)
print(data)'''

def sort(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if(array[j]<array[min]):
                min=j
        temp=array[i]
        array[i]=array[min]
        array[min]=temp
    return array
array=[1,12,10,14,7,2]   
sort(array)
print(array)
