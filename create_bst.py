import random

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __repr__(self):
		return "({})".format(self.data)

def create_bst(arr):
	l = len(arr)
	if l == 0:
		return None
	m = int(l / 2)
	n = Node(arr[m])
	n.left = create_bst(arr[:m])
	n.right = create_bst(arr[m + 1:])
	return n

def create_bst_optimized(arr, start = None, end = None):
	if start == None:
		start = 0
		end = len(arr) - 1
	if start > end:
		return None
	m = int((start + end) / 2)
	n = Node(arr[m])
	n.left = create_bst_optimized(arr, start, m - 1)
	n.right = create_bst_optimized(arr, m + 1, end)
	return n

def preorder_traverse(n):
	if not n:
		return
	preorder_traverse(n.left)
	print(n, end=", ")
	preorder_traverse(n.right)

def main():
	arr = [random.randint(100, 10000) for i in range(100)]
	arr = sorted(arr)
	print(arr)
	n = create_bst_optimized(arr)
	preorder_traverse(n)

if __name__ == "__main__":
	main()

