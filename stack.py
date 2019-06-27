from ll import Node

# STACK FILO
class Stack(object):
	def __init__(self):
		self.head = None

	def push(self, data):
		n = Node(data)
		n.next = self.head
		self.head = n
		return self.head

	def pop(self):
		if self.is_empty():
			return None
		data = self.head.data
		self.head = self.head.next
		return data

	def is_empty(self):
		return (self.head == None)

	def peek(self):
		return self.head.data if self.head else None

	def peek_node(self):
		return self.head if self.head else None

def main():
	stack = Stack()
	print("is empty?")
	print(stack.is_empty())
	stack.push(3)
	stack.push(5)
	stack.push(7)
	stack.push(9)
	stack.push(2)
	stack.push(5)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	data = stack.peek()
	print(data)
	print("is empty?")
	print(stack.is_empty())

if __name__ == "__main__":
	main()
