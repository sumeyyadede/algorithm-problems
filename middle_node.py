from ll import LinkedList

def middle_node(node):
	node.data = node.next.data
	node.next = node.next.next

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
	print("----")

def main():

	ll = LinkedList()
	ll.insert("a")
	ll.insert("b")
	ll.insert("c")
	ll.insert("d")
	ll.insert("e")
	ll.insert("f")
	print_ll(ll.head)
	node = ll.head.next.next
	middle_node(node)
	print_ll(ll.head)

if __name__ == "__main__":
	main()
