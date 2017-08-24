
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

	def __repr__(self):
		return "({})".format(self.data)

def in_order_successor(node):
	if not node:
		return None
	if node.right:
		n = node.right
		while n.left:
			n = n.left
		return n
	elif node.parent:
		n = node.parent
		c = node
		while n and n.left != c:
			c = n
			n = n.parent
		return n
	return None

def main():
	root = Node(15)
	root.left = Node(8)
	root.left.parent = root
	root.right = Node(20)
	root.right.parent = root
	root.right.left = Node(16)
	root.right.left.parent = root.right
	root.right.right = Node(30)
	root.right.right.parent = root.right
	root.left.left = Node(5)
	root.left.left.parent = root.left
	root.left.right = Node(10)
	root.left.right.parent = root.left
	root.left.right.left = Node(9)
	root.left.right.left.parent = root.left.right
	root.left.right.right = Node(12)
	root.left.right.right.parent = root.left.right
	print(in_order_successor(root.left.right.right))

if __name__ == "__main__":
	main()

