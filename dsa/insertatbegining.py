class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class SinglyLL:
	def __init__(self):
		self.head=None
	def traversal(self):
		if self.head is None:
			print("Linked list is empty")
		else:
			a=self.head
			while a is not None:
				print(a.data,end=" ")
				a=a.next
	def insert_at_big(self,data):
		print()
		nb=Node(data)
		nb.next=self.head
		self.head=nb
n1=Node(5)
sll=SinglyLL()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4
sll.traversal()
sll.insert_at_big(2)
sll.traversal()

