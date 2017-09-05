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
	queue = Queue()
	print("is empty?")
	print(node.is_empty())
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
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	data = queue.peek()
	print(data)
	print("is empty?")

	print(queue.is_empty())
if __name__ == "__main__":
	main()
