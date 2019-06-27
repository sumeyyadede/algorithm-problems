from stack import Stack

class SetOfStacks(object):
	def __init__(self):
		self.setof_stacks = Stack()
		self.counter = 0
		self.threshold = 3
		self.sub_index = 0

	def _is_there_child_stack(self):
		if self.counter == 0:
			self.setof_stacks.pop()
			if self.setof_stacks.is_empty():
				return False
			self.sub_index = self.sub_index - 1
			self.counter = self.threshold
		return True

	def push(self, data):
		if self.setof_stacks.is_empty() or self.counter == self.threshold:
			self.setof_stacks.push(Stack())
			self.sub_index = self.sub_index + 1
			self.counter = 0 					
		self.setof_stacks.peek().push(data)
		self.counter = self.counter + 1

	def pop(self):
		if not self._is_there_child_stack():
			return None
		data = self.setof_stacks.peek().pop()
		self.counter = self.counter - 1
		return data 

	def peek(self):
		if not self._is_there_child_stack():
			return None
		return self.setof_stacks.peek().peek()

	def is_empty(self):
		return self.setof_stacks.is_empty()
	
	def pop_at(self, sub_stack):
		diff = self.sub_index - sub_stack
		if diff < 0:
			return None
		temp_stack = Stack()
		for _ in xrange(diff):
			temp_stack.push(self.setof_stacks.pop())
		dt = self.setof_stacks.peek().pop()
		for _ in xrange(diff):
			self.setof_stacks.push(temp_stack.pop())
		return dt

def main():

	stack = SetOfStacks()
	# print(stack.pop())
	# print(stack.peek())	
	# print(stack.is_empty())
	stack.push(3)
	print("counter", stack.counter)
	# stack.push(5)
	# print("counter", stack.counter)
	# stack.push(3)
	# print("counter", stack.counter)
	# stack.push(2)
	# print("counter", stack.counter)
	# print(stack.pop())
	# print(stack.peek())
	# stack.push(9)
	# print("counter", stack.counter)
	# stack.push(5)
	# print("counter", stack.counter)
	# print(stack.pop())
	# print(stack.pop())
	print("popat", stack.pop_at(1))
	# print("popat", stack.pop_at(1))
	# print("popat", stack.pop_at(1))
	# print("popat", stack.pop_at(1))
	print(stack.pop())
	# print(stack.is_empty())
	# # print(stack.pop())
	# print(stack.is_empty())
	# # print(stack.pop())
	# # print(stack.pop())
	# stack.push(6)
	# stack.push(7)
	# print("popat", stack.pop_at(2))
	# print("popat", stack.pop_at(2))
	# print("popat", stack.pop_at(3))
	# print("popat", stack.pop_at(2))
	# print("self", stack.sub_index)
	# print("popat", stack.pop_at(5))
	# print(stack.peek())
	# print(stack.pop())
	# # print(stack.peek())
	# # print(stack.pop())
	# stack.push(6)
	# stack.push(7)
	# stack.push(6)
	# stack.push(7)
	# print("popat", stack.pop_at(3))
	# # print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.is_empty())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.is_empty())
	# print(stack.peek())
	# stack.push(5)
	# stack.push(1)
	# stack.push(2)
	# stack.push(9)
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())


if __name__ == "__main__":
	main()
