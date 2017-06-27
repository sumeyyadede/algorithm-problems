
def urlify(string, length):
	i = 0
	spaces = 0
	while i < length:
		if string[i] == " ":
			spaces = spaces + 1
		i = i + 1
	i = length - 1
	prev_i = length - 1
	while i >= 0:
		if string[i] == " ":
			while i < prev_i:
				string[prev_i + 2 * spaces] = string[prev_i]
				prev_i = prev_i - 1
			string[prev_i + 2 * spaces] = "0"
			string[prev_i + 2 * spaces - 1] = "2"
			string[prev_i + 2 * spaces - 2] = "%"
			spaces = spaces - 1
			prev_i = i - 1
		i = i - 1
	return "".join(a for a in string)

def main():
	string = "Mr John Smith"
	length = 13
	input_string = [a for a in string] + [" " for _ in xrange(4)]
	url = urlify(input_string, length)
	print(url)

if __name__ == "__main__":
	main()
