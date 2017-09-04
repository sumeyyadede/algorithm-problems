from stack import Stack		

class SortStack(Stack):
	def push(self, data):
		if super(SortStack, self).is_empty():
			return super(SortStack, self).push(data)
		temp_stack = Stack()
		while not super(SortStack, self).is_empty() and super(SortStack, self).peek() <= data:
			temp_stack.push(super(SortStack, self).pop())
		data = super(SortStack, self).push(data) 
		while not temp_stack.is_empty():
			super(SortStack, self).push(temp_stack.pop())
		return data

def main():

	stack = SortStack()
	stack.push(6)
	stack.push(1)
	stack.push(4)
	stack.push(9)
	stack.push(8)
	stack.push(888)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.peek())
	print(stack.peek())
	print(stack.peek())
	print(stack.peek())
	print(stack.peek())

	# stack.push(1)
	# stack.peek()
	# stack.push(0)
	# stack.peek()
	# stack.push(9)
	# stack.push(8)
	# stack.push(5)
	# stack.peek()
	# stack.push(4)
	# stack.peek()
	# print(stack.pop())
	# print(stack.peek())
	# print(stack.is_empty())

if __name__=="__main__":
	main()
