n=int(input('enter number'))
if n<1:
	print('Not a Prime')
else:
	is_prime=True                #0(1)
	for i in range(2,n//2+1):    #O(n)
		if n%i==0:             #O(1)
			is_prime=False   #O(1)
			break
	if is_prime==True:           #O(1)
		print('Prime number')
	else:
		print('Not a Prime number')

Total Time complexity : O(n)
      space complexity: O(1)


2nd code:


def solution(arr,t):
    map={}
    for i,n in enumerate(l1):    #O(n)
        d=t-n                    #0(1)
        if d in map:             #O(1)
            return [n,d]         #O(1)
        map[n]=i            
    return
arr=[3,5,-4,8,11,1,-1,6]
t=10
print(solution(l1,t))

Total Time complexity : O(n)
      space complexity: O(n)




Other questions:

1.Highest degree achieved - Bachelors
2.Degree specification - B.Tech
3.Degree specialisation - Information Technology
4.Fresher







			





