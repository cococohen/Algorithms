class Node(object):
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev
	
	def __str__(self):
		return "Node[Data=" + str(self.data) + "]"

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		
	def insert(self, data):
		if (self.head == None):
			self.head = Node(data)
			self.tail = self.head
		else:
			current = self.head
			while (current.next != None):
				current=current.next
			
			current.next = Node(data, None, current)
			self.tail = current.next

	def delete(self, data):
		current = self.head
		if (current.data == data):
			self.head = current.next
			self.head.previous = None
			return True
			
		if (current is None):
			return False
			
		if self.tail == data:
			self.tail = self.tail.prev
			self.tail.next = None
			return True
		
		while current is not None:
			if current.data == data:
				current.prev.next = current.next
				current.next.previous = current.prev
				return True
			current = current.next
		return False
			
	def fwdprint(self):
		current = self.head
		if self.head is None:
			print ("no elements in list")
			return False
		while current is not None:
			print (current.data)
			current = current.next
		return True
		
	def revprint(self):
		current = self.tail
		if self.tail is None:
			print("no elements in list")
			return False
		while current is not None:
			print (current.data)
			current=current.prev
		return True

	def search(self, data):
		current = self.head
		count = 0
		if self.head is None:
			print("there is no list")
			return False
		while current is not None:
			if current.data == data:
				print("found " + str(data) + " in list at count: " + str(count))
				return True
			current=current.next
			count += 1
		print ("did not find " + str(data) + " in list")
		return False
		

print ("making list")
ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(9)

ll.fwdprint()
ll.search(10)
ll.search(9)
