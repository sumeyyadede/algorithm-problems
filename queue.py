from ll import Node

# Queue FIFO
class Queue(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def push(self,data):
		n = Node(data)
		if self.head == None:
			self.head = n
		if self.tail != None:
			self.tail.next = n
		self.tail = n
	
	def pop(self):
		if self.is_empty():
			return None
		data = self.head.data
		self.head = self.head.next
		return data

	def is_empty(self):
		return self.head == None

	def peek(self):
		return self.head.data if self.head else None

def main():
	node = Queue()
	print("is empty?")
	print(node.is_empty())
	node.push(3)
	node.push(8)
	node.push(6)
	node.push(0)
	node.push(4)
	node.push(5)
	print(node.is_empty())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	print(node.pop())
	data = node.peek()
	print(data)
	print("is empty?")
	print(node.is_empty())

if __name__ == "__main__":
	main()
