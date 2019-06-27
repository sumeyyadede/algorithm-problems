from ll import Node
from queue import Queue

class AnimalNode(Node):
	def __init__(self,name=None,data=None):
		super(AnimalNode, self).__init__(name,data)
		self.next_same_kind = None

class AnimalQueue(Queue):
	def __init__(self):
		self.head = None
		self.tail = None
		self.headc = None
		self.headd = None
		self.queueDog = Queue()
		self.queueCat = Queue()

	def enqueue(self,name,kind):
		if kind == "cat":
			ani_kind = 1
			print("cat", name)
		elif kind == "dog":
			ani_kind = 2
			print("dog", name)
		else:
			return False
		n = AnimalNode(name,ani_kind)
		if self.head == None:
			self.head = n
		print("head", self.head.data)
		if self.tail != None:
			self.tail.next = n
		self.tail = n
		if ani_kind == 1:
			if self.headc == None:
				self.headc = n
				print("headc", name)
			self.queueCat.push(n)
		if ani_kind == 2:
			if self.headd == None:
				self.headd = n
				print("headd", name)
			self.queueDog.push(n)

	def dequeueDog(self):
		if self.queueDog.is_empty():
			return None
		if self.head == self.headd:
			data = self.head.data
			self.head = self.head.next
		else:
			if self.headd.next != None:
				print("1111")
				self.headd.data = self.headd.next.data
				self.headd.next = self.headd.next.next
				print("dog self.head.data", self.head.data)
			else:
				print("222")
				self.headd.data = None
				self.headd.next = None
			data = self.headd.data
		self.queueDog.pop()
		print("QueueDog")
		if self.queueDog.peek() != None:
			self.headd = self.queueDog.peek()
		else:
			self.headd = None
		return data 

	def dequeueCat(self):
		if self.queueCat.is_empty():
			return None
		if self.head == self.headc:
			data = self.head.data
			self.head = self.head.next
			self.prev = self.head		
		else:
			if self.headc.next != None:
				print("33333")
				# self.prev.next = self.prev.next.next
				self.headc.data = self.headc.next.data
				self.headc.next = self.headc.next.next
			else:
				print("444444")
				self.headc.data = None
				self.headc.next = None
			data = self.headc.data			
		print("QueueCat")
		self.queueCat.pop()
		if self.queueCat.peek() != None:
			self.headc = self.queueCat.peek()
		else:
			self.headc = None
	 	return data 

def main():

	queue = AnimalQueue()
	queue.enqueue("flow","dog")
	queue.enqueue("heyyo","cat")
	queue.enqueue("kara","dog")
	queue.enqueue("beyaz","cat")
	queue.enqueue("boncuk","cat")
	queue.enqueue("kar","dog")
	queue.enqueue("zeytin","cat")
	# queue.enqueue("minnak","cat")
	# queue.enqueue("pamuk","dog")
	# queue.enqueue("catName","cat")
	# queue.enqueue("bulut","dog")

	print("dequeueDog", queue.dequeueDog())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueDog", queue.dequeueDog())
	print("dequeueCat", queue.dequeueCat())
	print("dequeueCat", queue.dequeueCat())

						
if __name__ == "__main__":
	main()

