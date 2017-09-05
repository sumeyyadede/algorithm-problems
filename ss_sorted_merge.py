
def sorted_merge(a, b, l_a):
	l_b = len(b) - 1
	l_m = len(a) - 1
	l_a -= 1
	while l_m > -1:
		if l_a > -1 and a[l_a] > b[l_b]:
			a[l_m] = a[l_a]
			l_a -= 1
		elif l_b > -1:
			a[l_m] = b[l_b]
			l_b -= 1
		l_m -= 1
	return a

def main():
	b = [ i for i in xrange(4, 7)]
	a = [ i for i in xrange(3)]
	l_a = len(a)
	a += [None for _ in xrange(len(b))]
	print(a, b, l_a)
	print(sorted_merge(a, b, l_a))

if __name__ == "__main__":
	main()
