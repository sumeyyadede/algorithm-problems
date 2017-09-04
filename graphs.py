from queue import Queue

class GraphNode(object):
	def __init__(self,data):
		self.data = data
		self.is_visited = False
		self.nodes = []

	def __repr__(self):
		return "({}, {}, {})".format(self.data, self.is_visited, self.nodes if self.nodes else None)

class Graph(object):

	def breath_first_search(self,node):
		queue = Queue()
		if not node:
			return None
 		queue.push(node)
		self.is_visited = True
		while not queue.is_empty():
			popped_node = queue.pop()
			print(popped_node.data)
			for child_node in popped_node.nodes:
				if child_node.is_visited == False:
					child_node.is_visited = True
					queue.push(child_node)

	def depth_first_search(self,node):
		node.is_visited = True
		if not node:
			return None
		print(node.data)
		for child_node in node.nodes:
			if child_node.is_visited == False:
				self.depth_first_search(child_node)		


def main():

	root = GraphNode(1)
	a = GraphNode(2)
	b = GraphNode(3)
	c = GraphNode(4)
	d = GraphNode(5)
	e = GraphNode(6)
	f = GraphNode(7)
	g = GraphNode(8)
	h = GraphNode(9)
	i = GraphNode(10)
	j = GraphNode(11)
	k = GraphNode(12)
	root.nodes = [a, b, c, d]
	b.nodes = [e, f, g]
	c.nodes = [h, i]
	e.nodes = [b]
	f.nodes = [g]
	h.nodes = [j]
	i.nodes = [j]
	j.nodes = [k]
	k.nodes = [i]

	graph_impl = Graph()
	print("breadth first section")
	graph_impl.breath_first_search(root)
	print("depth first section")
	graph_impl.depth_first_search(root)

if __name__ == "__main__":
	main()
