from stack import Stack

# STACK FILO
class StackMin(Stack):
	def __init__(self):
		super(StackMin, self).__init__()
		self._stack_min = Stack()

	def push(self, data):
		n = super(StackMin, self).push(data)
		if self._stack_min.is_empty() or self._stack_min.peek().data > n.data:
			self._stack_min.push(n)

	def pop(self):
		if self.peek_node() == self._stack_min.peek():
			self._stack_min.pop() 
		return super(StackMin, self).pop()

	def stack_min(self):
		return self._stack_min.peek().data if not self._stack_min.is_empty() else None

def main():
	stack = StackMin()

	stack.push(3)
	stack.push(5)
	stack.push(1)
	stack.push(2)
	stack.push(9)
	stack.push(1)
	print(stack.stack_min())  
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.stack_min()) 
	print(stack.pop())	 	
	print(stack.stack_min())				
	print(stack.stack_min())
	print("POP", stack.pop())
	print(stack.pop())
	stack.push(3)
	stack.push(5)
	stack.push(1)
	stack.push(2)
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	print(stack.pop())
	print(stack.stack_min())
	# print(stack.stack_min())
	# print(stack.pop())
	# print(stack.stack_min())
	# print(stack.pop())
	# stack.push(0)
	# stack.push(8)
	# stack.push(1)
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.stack_min())
	# print(stack.stack_min())

if __name__ == "__main__":
	main()
