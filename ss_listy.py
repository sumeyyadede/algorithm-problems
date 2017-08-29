
class Listy(object):
	def __init__(self, l):
		self.l = l

	def element_at(self, i):
		if i < len(self.l):
			return self.l[i]
		return -1

def bs_listy(listy, x):
	start = 0
	end = 0
	c = 0
	while listy.element_at(end) != -1 and listy.element_at(end) <= x:
		start = end
		end = pow(2, c) - 1
		c += 1
	print(start, end)
	while start <= end:
		middle = (start + end) / 2
		if listy.element_at(middle) == - 1 or listy.element_at(middle) > x:
			end = middle - 1
		elif listy.element_at(middle) < x:
			start = middle + 1
		else:
			return middle
	return -1

def main():
	listy = Listy([i for i in xrange(200)])
	print(bs_listy(listy, 199))



if __name__ == "__main__":
	main()

