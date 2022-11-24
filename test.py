#given an array of numbers, find out if it is sorted or not. If sorted indicate in what order - ascending or descending?

def fun(l1):
	for i in l1:

		if l1[i]<l1[j]:
			print('sorted')
		else:
			print('not')
l1=[1,3,7,6,5]
fun(l1)













