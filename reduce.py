from functools import *
l=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,l)
print(result)