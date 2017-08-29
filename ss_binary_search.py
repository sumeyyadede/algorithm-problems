
def binary_search(arr, x):
	start = 0
	end = len(arr) - 1
	while start <= end:
		middle = (start + end) / 2
		if arr[middle] > x:
			end = middle - 1
		elif arr[middle] < x:
			start = middle + 1
		else:
			return middle
	return -1

def binary_search_twisted(arr, x):
	orig_start = 0
	prev = arr[0]
	i = 1
	l_arr = len(arr)
	while i < l_arr:
		if arr[i] < prev:
			break
		prev = arr[i]
		i += 1
	orig_start = i

	start = 0
	end = len(arr) - 1
	while start <= end:
		middle = (start + end) / 2
		if arr[(middle + orig_start) % l_arr] > x:
			end = middle - 1
		elif arr[(middle + orig_start) % l_arr] < x:
			start = middle + 1
		else:
			return (middle + orig_start) % l_arr
	return -1

def main():
	arr = [i for i in xrange(200, 250)] + [i for i in xrange(200)]
	print(arr)
	print(binary_search_twisted(arr, 210))

if __name__ == "__main__":
	main()

