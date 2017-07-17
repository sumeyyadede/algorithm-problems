from ll import LinkedList

def find_duplicates(linked_list):
	ht = dict()
	node = linked_list.head
	prev_node = None
	while node:
		if node.data in ht:
			prev_node.next = node.next
		else:
			ht[node.data] = 1
			prev_node = node
		node = node.next

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
	print("----")


def main():
	ll = LinkedList()
	ll.insert(1)
	ll.insert(2)
	ll.insert(10)
	ll.insert(20)
	ll.insert(30)
	ll.insert(1)
	ll.insert(20)
	ll.insert(30)
	print_ll(ll.head)
	find_duplicates(ll)
	print_ll(ll.head)



if __name__ == "__main__":
	main()
