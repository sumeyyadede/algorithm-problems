from ll import LinkedList

def kth_element(linked_list, counter):
	node = linked_list.head
	prev_node = linked_list.head

	i=0
	while node:
		if i == counter - 1:
			break
		node = node.next
		i = i + 1

	if i !=  counter - 1:
		print("not enough elements in the list")
		return #None

	#for i in xrange(counter-1):
	#	if node.next != None:
	#		node = node.next
	#	else:
	#		return "could not found this last number."

	while node.next != None:
		node = node.next
		prev_node = prev_node.next
	return prev_node.data

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
	print("----") 

def main():
	ll = LinkedList()
	ll.insert(100)
	ll.insert(90)
	ll.insert(80)
	ll.insert(70)
	ll.insert(60)
	ll.insert(50)
	ll.insert(40)
	ll.insert(30)
	ll.insert(20)
	ll.insert(10)
	print_ll(ll.head)
	print("return the 5th to last element.")
	print(kth_element(ll, 5))

if __name__ == "__main__":
	main()
