def one_way(string1, string2):
	l1 = len(string1)
	l2 = len(string2)
	if abs(l1 - l2) > 1:
		return False
	has_operated = False
	if abs(l1 - l2) == 1:
		if l1 > l2:
			i = 0
			while i < l2:
				if string1[i] != string2[i]:
					if not has_operated:
						string1 = string1[:i] + string1[i+1:]
						has_operated = True
					else:
						return False
				else:
					i = i + 1
		else:
			i = 0
			while i < l1:
				if string1[i] != string2[i]:
					if not has_operated:
						string1 = string1[:i] + string2[i] + string1[i:]
						has_operated = True
					else:
						return False
				else:
					i = i + 1
	else:
		i = 0
		while i < l1:
			if string1[i] != string2[i]:
				if not has_operated:
					has_operated = True
				else:
					return False
			i = i + 1
	return True

def main():
	string1 = "palxs"
	string2 = "pale"
	iow = one_way(string1, string2)
	print(iow)

if __name__ == "__main__":
	main()
