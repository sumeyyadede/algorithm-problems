from stack import Stack
from queue import Queue

class Node(object):
	def __init__(self, data):
		self.data = data
		self.nodes = []

	def __repr__(self):
		return "({})".format(self.data)

def create_ll(node, depth_lists, level = 0):
	if not node:
		return
	if not level in depth_lists:
		depth_lists[level] = []
	depth_lists[level].append(node.data)
	for child_node in node.nodes:
		create_ll(child_node, depth_lists, level + 1)

def bfs(node):
	q = Queue()
	q.push(node)
	while not q.is_empty():
		n = q.pop()
		print(n.data)
		for cn in n.nodes:
			q.push(cn)

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
	root.nodes = [a, b, c, d]
	b.nodes = [e, f, g]
	c.nodes = [h, i]
	i.nodes = [j]
	j.nodes = [k]
	main_depth_lists = {}
	create_ll(root, main_depth_lists)
	print(main_depth_lists)

if __name__ == "__main__":
	main()
