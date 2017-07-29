from ll import Node

def ll_intersection(node1,node2):
	temp1 = node1
	temp2 = node2
	len1 = 0
	len2 = 0
	while temp1 or temp2:
		if temp1:
			len1 = len1 + 1
			temp1 = temp1.next
		if temp2:
			len2 = len2 + 1
			temp2 = temp2.next
	
	diff = abs(len2 - len1)
	for _ in xrange(diff):
		if len2 > len1:
			node2 = node2.next
		else:
			node1 = node1.next

	while node1: 
		if node1 == node2:
			return node2
		node1 = node1.next
		node2 = node2.next
	return None

def main():
	
	node2 = Node(2)
	node2.next = Node(5)
	node2.next.next = Node(7)
	node2.next.next.next = Node(8)
	node2.next.next.next.next = Node(9)
	node1 = Node(2)
	node1.next = Node(1)
	node1.next.next = Node(8)
	node1.next.next.next = Node(6)
	node1.next.next.next.next = node2.next.next
	node3 = ll_intersection(node1, node2)
	if not node3:
		print(node3)
	else:
		while node3:
			print(node3.data)
			node3 = node3.next

if __name__ == "__main__":
	main()

