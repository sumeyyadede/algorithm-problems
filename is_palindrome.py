
def is_palindrome(string):
	length = len(string)
	string = string.lower()
	is_odd = (length % 2 == 1)
	ht = dict()
	for s in string:
		ht[s] = ht[s] + 1 if s in ht else 1
	has_visited_odd = not is_odd
	for key in ht:
		if ht[key] % 2 == 1:
			if has_visited_odd:
				return False
			else:
				has_visited_odd = True
	return True



def main():
	string = "TactCoa"
	isp = is_palindrome(string)
	print(isp)

if __name__ == "__main__":
	main()
