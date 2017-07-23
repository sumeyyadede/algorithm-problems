from ll import LinkedList

def sum_lists(l1,l2,l3):
	node = l1.head
	temp = l2.head
	counter = 0 
	while node or temp:
		if node:
			x = node.data
			node = node.next
		else:
			x=0
		if temp:
			y = temp.data
			temp = temp.next
		else:
			y=0
		if counter == 0:
			z = x + y
		else:
			z = x + y + 1
		if z < 10:
			l3.insert_front(z) 
			counter = 0
		else:
			l3.insert_front(z%10)
			counter = 1
	if counter == 1:
		l3.insert_front(1)

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
	print("----")

def main():
	l1 = LinkedList()
	l1.insert(8)
	l1.insert(8)
	l1.insert(8)
	print_ll(l1.head)
	l2 = LinkedList()
	l2.insert(9)
	l2.insert(9)
	l2.insert(7)
	#l2.insert(8)
	#l2.insert(9)
	print_ll(l2.head)
	l3 = LinkedList()
	sum_lists(l1,l2,l3)
	print_ll(l3.head)

if __name__ == "__main__":
	main()
