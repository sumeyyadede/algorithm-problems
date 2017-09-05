
class Kind(object):
	DOG = 1
	CAT = 2

class Animal(object):
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

	def __repr__(self):
		return "({}, {})".format(self.name, "dog" if self.kind == Kind.DOG else "cat" if self.kind == Kind.CAT else "unknown")

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return "({})".format(self.data)

class AnimalNode(Node):
	def __init__(self, data):
		super(AnimalNode, self).__init__(data)
		self.next_same_kind = None

	def __repr__(self):
		return "({}, {}, {})".format(self.data, self.next.data if self.next else None, self.next_same_kind.data if self.next_same_kind else None)

class Queue(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, n):
		if not n:
			return None
		if self.tail:
			self.tail.next = n
		self.tail = n
		if not self.head:
			self.head = self.tail
		return self.tail

	def dequeue(self):
		if self.head:
			n = self.head
			self.head = self.head.next
			if not self.head:
				self.tail = None
			return n
		return None

	def is_empty(self):
		return self.head == None

class AnimalQueue(Queue):
	def __init__(self):
		super(AnimalQueue, self).__init__()
		self.head_dog = None
		self.head_cat = None
		self.tail_dog = None
		self.tail_cat = None

	def enqueue(self, n):
		if self.head and not self.head.data:
			self.head = self.head.next
		if not super(AnimalQueue, self).enqueue(n):
			return None
		if self.tail.data.kind == Kind.DOG:
			if self.tail_dog:
				self.tail_dog.next_same_kind = self.tail
			self.tail_dog = self.tail
			if not self.head_dog:
				self.head_dog = self.tail_dog
		elif self.tail.data.kind == Kind.CAT:
			if self.tail_cat:
				self.tail_cat.next_same_kind = self.tail
			self.tail_cat = self.tail
			if not self.head_cat:
				self.head_cat = self.tail_cat
		return self.tail

	def dequeue_any(self):
		n = super(AnimalQueue, self).dequeue()
		if not n:
			return None
		if n.data.kind == Kind.DOG and self.head_dog:
			self.head_dog = self.head_dog.next_same_kind
			if not self.head_dog:
				self.tail_dog = None
		elif n.data.kind == Kind.CAT and self.head_cat:
			self.head_cat = self.head_cat.next_same_kind
			if not self.head_cat:
				self.tail_cat = None
		return n

	def dequeue_dog(self):
		print(self.head_dog)
		if self.head == self.head_dog:
			return self.dequeue_any()
		if not self.head_dog:
			return None
		n_data = self.head_dog.data
		nsk = self.head_dog.next_same_kind
		if self.head_dog.next:
			self.head_dog.data = self.head_dog.next.data
			self.head_dog.next_same_kind = self.head_dog.next.next_same_kind
			self.head_dog.next = self.head_dog.next.next
			self.head_dog = nsk
		else:
			self.head_dog.data = None
			self.head_dog = None
		if not self.head_dog:
			self.tail_dog = None
		return n_data

	def dequeue_cat(self):
		if self.head == self.head_cat:
			return self.dequeue_any()
		if not self.head_cat:
			return None
		n_data = self.head_cat.data
		nsk = self.head_cat.next_same_kind
		if self.head_cat.next:
			self.head_cat.data = self.head_cat.next.data
			self.head_cat.next_same_kind = self.head_cat.next.next_same_kind
			self.head_cat.next = self.head_cat.next.next
			self.head_cat = nsk
		else:
			self.head_cat.data = None
			self.head_cat = None
		if not self.head_cat:
			self.tail_cat = None
		return nsk

	def is_empty(self):
		if self.head and not self.head.data:
			self.head = self.head.next
		return super(AnimalQueue, self).is_empty()


def main():
	animals = [
		Animal("sumus", Kind.DOG), 
		Animal("teo", Kind.DOG),
		Animal("cito", Kind.CAT)
	]
	n = AnimalNode(animals[0])
	n.next = AnimalNode(animals[1])
	n.next_same_kind = AnimalNode(animals[2])

	q = AnimalQueue()
	q.enqueue(AnimalNode(Animal("Dog 1", Kind.DOG)))
	q.enqueue(AnimalNode(Animal("Cat 1", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Cat 2", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Cat 3", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Cat 4", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Cat 5", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Cat 6", Kind.CAT)))
	q.enqueue(AnimalNode(Animal("Dog 2", Kind.DOG)))

	print(q.dequeue_dog())

	while not q.is_empty():
		print(q.dequeue_any())

if __name__ == "__main__":
	main()
