from ll import LinkedList
import math

def sum_lists(l1, l2):
	l3	 = LinkedList()
	node = l1.head
	temp = l2.head
	remainder = 0
	while node or temp:
		if node:
			x = node.data
			node = node.next
		else:
			x = 0
			
 		if temp:
			y = temp.data
			temp = temp.next
		else:
			y = 0
		z = x + y + remainder
		remainder = z / 10
		l3.insert_front(z % 10)
	if remainder == 1:
		l3.insert_front(1)
	return l3

def sum_lists2(l1,l2):
	l4 = LinkedList()
	node = l1.head
	temp = l2.head
	counter1 = 0
	counter2 = 0
	while node:
		node = node.next
		counter1 = counter1 + 1
	while temp:
		temp = temp.next
		counter2 = counter2 + 1
	node = l1.head
	temp = l2.head
	x = 0
	y = 0
	while node or temp:
		if node:
			counter1 = counter1 - 1
			x = x + (node.data)*pow(10,counter1)
			node = node.next
		if temp:
			counter2 = counter2 - 1
			y = y + (temp.data)*pow(10,counter2)
			temp = temp.next
	z = x + y
	n = z
	digit = 1
	while n >= 10:
		n = n / 10
		digit = digit + 1
	for t in xrange(digit):
		digit = digit - 1
		s = z / pow(10,digit)
		z = z - (s*pow(10,digit))
		l4.insert_front(s)
	return l4

def sum_lists_new(a1, a2):
	s = ll_to_int(a1) + ll_to_int(a2)	
	return int_to_ll(s)

def ll_to_int(a):
	node = a.head
	s = 0
	while node:
		s = (s*10) + node.data
		node = node.next
	return s

def int_to_ll(s):
	ll = LinkedList()
	while s != 0:
		ll.insert(s % 10) 
		s = s / 10
	return ll

def print_ll(t):
	while t:
		print(t.data)
		t = t.next
 	print("----")

def main():
	l1 = LinkedList()
	l1.insert(1)
	l1.insert(8)
	l1.insert(9)
	l1.insert(8)
	l1.insert(9)
	print_ll(l1.head)
	l2 = LinkedList()
	l2.insert(6)
	l2.insert(2)
	l2.insert(1)
	print_ll(l2.head)
	l3 = sum_lists(l1,l2)
	print_ll(l3.head)
	print("########")
	l1 = LinkedList()
	l1.insert_front(1)
	l1.insert_front(8)
	l1.insert_front(9)
	l1.insert_front(8)
	l1.insert_front(9)
	print_ll(l1.head)
	l2 = LinkedList()
	l2.insert_front(6)
	l2.insert_front(2)
	l2.insert_front(1)
	print_ll(l2.head)
	print("****")
	l4 = sum_lists2(l1,l2)
	print_ll(l4.head)
	print("****")
	l5 = sum_lists_new(l1,l2)
	print_ll(l5.head)

if __name__ == "__main__":
	main()
