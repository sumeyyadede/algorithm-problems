
def is_unique(string):
	i = 0
	while i < len(string):
		j = i + 1
		while j < len(string):
			if string[i] == string[j]:
				return False
			j = j + 1
		i = i + 1
	return True

def is_unique_sorted(string):
	string = sorted(string)
	i = 0
	while i < len(string):
		j = i + 1
		while j < len(string):
			if string[i] == string[j]:
				return False
			j = j + 1
		i = i + 1
	return True
def is_unique_ht(string):
	ht = dict()
	for char in string:
		if char in ht:
			return False
		else:
			ht[char] = True
	return True 

def main():
	string = "Omer"
	iu = is_unique_ht(string)
	print(iu)

if __name__ == "__main__":
	main()
