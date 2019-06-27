from ll import Node

def main():

	node = Node(5)
	head = node
	node.next = Node(3)
	node.next.next = None
	temp = Node(5)
	head2 = temp
	temp.next = Node(8)

	print(temp.data)
	print(node.data)
	node.data = 3
	print(temp.data)
	print(node.data)


if __name__ == "__main__":
	main()
