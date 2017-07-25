
class Node(object):
	def __init__(self, data, node = None):
		self.data = data
		self.next = node

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def insert(self, data):
		n = Node(data)
		n.next = self.head
		self.head = n
	def insert_front(self,data):
		n = Node(data)
		if self.head == None:
			self.head = n
		if self.tail != None:
			self.tail.next = n
		self.tail = n
	def pop(self):
		t = None
		if self.head:
			t = self.head.data
			self.head = self.head.next
		return t

	def is_empty(self):
		return self.head == None


def main():
	ll = LinkedList()
	ll.insert(1)
	ll.insert(2)
	ll.insert(10)
	ll.insert(20)
	ll.insert(30)
	ll.insert(40)
	ll.insert(50)
	ll.insert(60)
	ll.insert(70)
	ll.insert(80)
	ll.insert(90)
	sr = ll.head
	fr = ll.head
	while sr:
		print("sr", sr.data)
		sr = sr.next
		if fr:
			print("fr", fr.data)
			if fr.next:
				fr = fr.next.next
			else:
				fr = None
		print("----")

if __name__ == "__main__":
	main()
