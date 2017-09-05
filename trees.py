class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		# return "({}, {}, {})".format(self.data, self.left.data if self.left else None, self.right.data if self.right else None)
		return "({})".format(self.data)

class Tree(object):
	def __init__(self):
		self.head = None

	def in_order_traversal(self, node):
		if node:
			self.in_order_traversal(node.left)
			print(node)
			self.in_order_traversal(node.right)			
		else:
			return None

	def pre_order_traversal(self, node):
		if node:
			print(node)
			self.pre_order_traversal(node.left)
			self.pre_order_traversal(node.right)			
		else:
			return None

	def post_order_traversal(self, node):
		if node:
			self.post_order_traversal(node.left)
			self.post_order_traversal(node.right)			
			print(node)
		else:
			return None

def main():

	root_node = TreeNode(1)
	root_node.left = TreeNode(2)
	root_node.right = TreeNode(3)
	root_node.left.left = TreeNode(4)
	root_node.left.right = TreeNode(5)
	
	print(root_node)
	print(root_node.left)
	print(root_node.right)

	tree_impl = Tree()

	print("inorder")
	tree_impl.in_order_traversal(root_node)
	print("---")
	print("preorder")
	tree_impl.pre_order_traversal(root_node)
	print("---")
	print("postorder")
	tree_impl.post_order_traversal(root_node)

if __name__ == "__main__":
	main()
