
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return "({})".format(self.data)

def check_balanced(node):
	if not node:
		return 0
	left = check_balanced(node.left)
	if left == -1:
		return -1
	right = check_balanced(node.right)
	if right == -1:
		return -1
	if abs(left - right) > 1:
		return -1
	return max(left, right) + 1

def main():
	root = Node(1)
	a = Node(2)
	b = Node(3)
	c = Node(4)
	d = Node(5)
	e = Node(6)
	f = Node(7)
	g = Node(8)
	h = Node(9)
	i = Node(10)
	j = Node(11)
	k = Node(12)
	root.left = a
	root.right = b
	b.left = c
	c.left = d
	c.right = j
	b.right = e
	a.left = h
	a.right = k
	h.left = i
	print(check_balanced(root))

if __name__ == "__main__":
	main()
