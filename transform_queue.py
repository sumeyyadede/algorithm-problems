from stack import Stack

class StackedQueue(object):
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
		self.is_pushed = False
	
	def _move_to_stack1(self):
		if not self.is_pushed:
			while not self.stack2.is_empty():
				self.stack1.push(self.stack2.pop())
		self.is_pushed = True

	def _move_to_stack2(self):
		if self.is_pushed:
			while not self.stack1.is_empty():
				self.stack2.push(self.stack1.pop())
		self.is_pushed = False

	def push(self, data):
		self._move_to_stack1()
		self.stack1.push(data)

	def pop(self):
		self._move_to_stack2()
		return self.stack2.pop()

	def is_empty(self):
		return self.stack1.is_empty() and self.stack2.is_empty()

	def peek(self):
		self._move_to_stack2()
		return self.stack2.peek()

def main():
	queue = StackedQueue()
	print("is empty?")
	print(queue.is_empty())
	print(queue.pop())
	print(queue.pop())
	queue.push(3)
	queue.push(6)
	queue.push(8)
	queue.push(0)
	queue.push(4)
	queue.push(5)
	print(queue.is_empty())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	# print(queue.pop())
	# print(queue.pop())
	queue.push(7)
	queue.push(9)
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	queue.push(8)
	queue.push(0)
	queue.push(4)
	queue.push(5)
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	queue.push(101)
	queue.push(102)
	print(queue.pop())
	queue.push(103)
	print(queue.pop())
	queue.push(104)
	print(queue.pop())
	print(queue.peek())
	print(queue.peek())
	print(queue.peek())
	queue.push(101)
	print(queue.peek())
	queue.push(101)
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	# data = queue.peek()
	# print(data)
	# print("is empty?")

	# print(queue.is_empty())

if __name__ == "__main__":
	main()
