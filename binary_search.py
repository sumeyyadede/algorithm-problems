
# def binary_search(arr, item):
	
# 	low = 0
# 	high = len(arr) - 1

# 	while low <= high:

# 		mid = (low + high) / 2
		
# 		if arr[mid] == item:
# 			return mid

# 		if arr[mid] > item:
# 			high = mid - 1

# 		else:
# 			low = mid + 1

# 	return None

def binary_search_recursion(arr, item):

	low = 0
	high = len(arr) 

	if len(arr) == 0:
		return None
		
	else:
		mid = (low + high) / 2

		if arr[mid] == item:
			return arr[mid]

		elif arr[mid] > item:		
			high = mid - 1
			return binary_search_recursion(arr[:high], item)

		elif arr[mid] < item:
			low = mid + 1
			return binary_search_recursion(arr[low:], item)


def main():
	
	arr = [None]*100
	for i in xrange(len(arr)):
		arr[i] = i + 5

	print(binary_search_recursion(arr, 1))

if __name__ == "__main__":
	main()
