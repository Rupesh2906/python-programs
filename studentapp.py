n=int(input('enter no of students:'))
d={}
for i in range(n):
	name=input('enter name:')
	marks=int(input('enter marks:'))
	d[name]=marks
print('*'*30)
print('NAME','\t\t','MARKS')
print('*'*30)
for k,v in d.items():
	print(k,'\t\t',v)
print('search operation started')
while True:
	name=input('enter name to find marks')
	marks=d.get(name,-1)
	if marks==-1:
		print('student not found')
	else:
		print('marks of',name,'are:',marks)
	option=input('do you want to find another student marks[yes/no]:')
	if option.lower()=='no':
		break
print("thanks for using our application")

