nums1=[7,8,1,2,3,4,5]
nums2=[3,4,1,29,1,5,1]
nums3= [4,1,69,2,7,3,6]
add = map(lambda x, y,z: (x + y)*z, nums1, nums2,nums3)
print(list(add))

inputlist = [21, 24, 12, 34, 10, 15, 41]
even_num = list(filter(lambda x : x % 2 == 0, inputlist))
print(even_num)


import functools
inp = [10, 24, 34, 42, 19]
multi= functools.reduce(lambda x,y:x*y,inp)
div= functools.reduce(lambda x,y:x/y,inp)
print(multi)
print(div)

import functools
s=[1,2,3]
add=functools.reduce(lambda x,y:x+y,s)
print(add)
print(max(s))
