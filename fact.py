def fact(n):
	if n==0:
		result=1
	else:
		result=n*fact(n-1)
	return result
for i in range(11):
	print('factorial of {} is {}'.format(i,fact(i)))