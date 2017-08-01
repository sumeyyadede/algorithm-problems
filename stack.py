from ll import Node

# STACK FILO
class Stack(object):
	def __init__(self):
		self.head = None

	def push(self,data):
		n = Node(data)
		n.next = self.head
		self.head = n

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
	node = Stack()
	print("is empty?")
	print(node.is_empty())
	node.push(3)
	node.push(5)
	node.push(7)
	node.push(9)
	node.push(2)
	node.push(5)
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
	print(node.pop())
	print(node.pop())
	data = node.peek()
	print(data)
	print("is empty?")
	print(node.is_empty())

if __name__ == "__main__":
	main()
