from ll import Node

def loop_detection(node):
	fr = node.next.next
	sr = node.next
	
	while fr != sr:
		fr = fr.next.next
		sr = sr.next
	
	sr = node
	while fr != sr:
		fr = fr.next
		sr = sr.next

	return sr

def main():
	node = Node("A")
	node.next = Node("B")
	node.next.next = Node("C")
	node.next.next.next = Node("D")
	node.next.next.next.next = Node("E")
	node.next.next.next.next.next = Node("F")
	node.next.next.next.next.next.next = Node("G")
	node.next.next.next.next.next.next.next = node.next.next.next
	node2 = loop_detection(node)
	print(node2.data)


if __name__ == "__main__":
	main()
