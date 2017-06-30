def one_way(string1, string2):
	l1 = len(string1)
	l2 = len(string2)
	if abs(l1 - l2) > 1:
		return False
	has_operated = False
	i = 0
	while i < min(l1, l2):
		if string1[i] != string2[i]:
			if not has_operated:
				if l1 > l2:
					string1 = string1[:i] + string1[i+1:]
				elif l1 < l2:
					string1 = string1[:i] + string2[i] + string1[i:]
				has_operated = True
			else:
				return False
		else:
			i = i + 1
	return True

def main():
	string1 = "pales"
	string2 = "pale"
	iow = one_way(string1, string2)
	print(iow)

if __name__ == "__main__":
	main()
