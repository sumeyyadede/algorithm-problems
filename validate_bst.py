
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return "({})".format(self.data)

def validate_bst(node):
	if not node:
		return True, None, None
	if (node.left and node.data < node.left.data) or \
		(node.right and node.data > node.right.data):
		return False, None, None
	if node.left:
		left_is_bst, left_left_min, left_right_max = validate_bst(node.left)
		if not left_is_bst:
			return False, None, None
		if left_right_max and left_right_max > node.data:
			return False, None, None
	else:
		left_left_min = node.data
		left_right_max = node.data
	if node.right:
		right_is_bst, right_left_min, right_right_max = validate_bst(node.right)
		if not right_is_bst:
			return False, None, None
		if right_left_min and right_left_min < node.data:
			return False, None, None
	else:
		right_left_min = node.data
		right_right_max = node.data
	left_min = min(left_left_min, right_left_min)
	right_max = max(left_right_max, right_right_max)
	print(left_min, right_max)
	return True, left_min, right_max

last_item = None
def validate_bst_last(node):
	global last_item
	if not node:
		return True
	if not validate_bst_last(node.left):
		return False
	if not last_item:
		last_item = node.data
	elif last_item > node.data:
		return False
	else:
		last_item = node.data
	if not validate_bst_last(node.right):
		return False
	return True

def validate_bst_min_max(node, mi = None, ma = None):
	if not node:
		return True
	if (mi and mi > node.data) \
		or (ma and ma < node.data) \
		or not validate_bst_min_max(node.left, mi, node.data) \
		or not validate_bst_min_max(node.right, node.data, ma):
		return False
	return True

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
	# root.left = a
	# root.right = b
	# b.left = c
	# c.left = d
	# c.right = j
	# b.right = e
	# a.left = h
	# a.right = k
	# h.left = i
	# root = e
	# root.left = c
	# root.right = g
	# c.left = a
	# c.right = d
	# f.left = Node()
	root = Node(15)
	root.left = Node(8)
	root.right = Node(20)
	root.right.left = Node(16)
	root.right.right = Node(30)
	root.left.left = Node(5)
	root.left.right = Node(10)
	root.left.right.left = Node(7)

	print(validate_bst(root))
	print(validate_bst_last(root))
	print(validate_bst_min_max(root))

if __name__ == "__main__":
	main()
