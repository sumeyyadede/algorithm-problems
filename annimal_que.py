from ll import Node

class AnimalNode(Node):
	def __init__(self,name=None,data=None):
		super(AnimalNode, self).__init__(name,data)
		self.next_same_kind = None

class AnimalQueue(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.headc = None
		self.tailc = None
		self.headd = None
		self.taild = None

	def enqueue(self,name,kind):
		if kind == "cat":
			ani_kind = 1
			print("cat")
		elif kind == "dog":
			ani_kind = 2
			print("dog")
		else:
			return False
		n = AnimalNode(name,ani_kind)
		if self.head == None:
			self.head = n
			print("head ", self.head.data)
		if self.tail != None:
			self.tail.next = n
		self.tail = n
		if ani_kind == 1:
			if self.headc == None:
				self.headc = n
				print("headc ",name)
			if self.tailc != None:
				self.tailc.next = n
			self.tailc = n
		if ani_kind == 2:
			if self.headd == None:
				self.headd = n
				print("headd ",name)
			if self.taild != None:
				self.taild.next = n
			self.taild = n





def main():

	queue = AnimalQueue()
	queue.enqueue("mamut","cat")
	queue.enqueue("kara","dog")
	queue.enqueue("beyaz","cat")
	queue.enqueue("boncuk","cat")
	queue.enqueue("kar","dog")
	queue.enqueue("zeytin","cat")


if __name__ == "__main__":
	main()


