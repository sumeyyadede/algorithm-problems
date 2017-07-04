def compress(string):
	result = str()
	count = 1
	prev_s = string[0]
	string = string + " "
	for s in string[1:]:
		if s == prev_s:
			count = count + 1
		else:
			result = result + prev_s + str(count)
			count = 1
			prev_s = s
	return result if len(result) < len(string) else string

def main():
	string = "aaaaaaabca"
	ip = compress(string)
	print(ip)

if __name__ == "__main__":
	main()
