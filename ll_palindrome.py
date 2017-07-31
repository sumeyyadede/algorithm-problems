from ll import LinkedList

def is_palindrome_ll(ll):
	node = ll.head
	ht = dict()
	length = 0
	while node:
		for s in node.data:
			ht[node.data] = ht[node.data] + 1 if s in ht else 1
			node = node.next
			length += 1 
	is_odd = (length % 2 == 1)
	has_visited_odd = not is_odd
	for key in ht:
		if ht[key] % 2 == 1:
			if has_visited_odd:
				return False
			else:
				has_visited_odd = True
	return True

def main():
	ll = LinkedList()
	ll.insert("t")
	ll.insert("a")
	ll.insert("t")
	ll.insert("c")
	ll.insert("a")
	isp = is_palindrome_ll(ll)
	print(isp)

if __name__ == "__main__":
	main()
