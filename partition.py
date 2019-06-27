from ll import LinkedList

def partition(linked_list, x):
	node = linked_list.head
	prev_node = None
	head2 = None
	tail2 = None
	while node:
		if node.data < x:
			if head2 == None:
				head2 = node
				tail2 = node
			else:
				tail2.next = node
				tail2 = node
			if prev_node is None:
				linked_list.head = node.next
			else:
				prev_node.next = node.next
		else:
			prev_node = node
		node = node.next
	tail2.next = linked_list.head
	linked_list.head = head2 

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
	print("----")

def main():
	ll = LinkedList()
	ll.insert(2)
	ll.insert(1)
	ll.insert(3)
	ll.insert(9)
	ll.insert(4)
	ll.insert(6)
	print_ll(ll.head)
	partition(ll, 6)
	print_ll(ll.head)

if __name__ == "__main__":
	main()
