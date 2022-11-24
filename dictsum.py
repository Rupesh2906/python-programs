d=eval(input('enter dict:'))
sum=0
for item in d.items():
	sum=sum+item[1]
print('Sum of values is:',sum)