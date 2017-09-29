
def is_permutation(string1, string2):
	if len(string1) != len(string2):
		return False
	if string1 == string2:
		return False
	ht = dict()
	for char in string1:
		ht[char] = ht[char] + 1 if char in ht else 1
	for char in string2:
		if char in ht:
			ht[char] = ht[char] - 1
			if ht[char] < 0:
				return False
		else:
			return False
	return True

def is_permutation_sorted(string1, string2):
	if len(string1) != len(string2):
		return False
	if string1 == string2:
		return False
	str1 = sorted(string1)
	str2 = sorted(string2)
	if str1 == str2:
		return True
	return False


def main():
	string1 = "omeeerr "
	string2 = "eeerrmo "
	ip = is_permutation(string1, string2)
	print(ip)

if __name__ == "__main__":
	main()
