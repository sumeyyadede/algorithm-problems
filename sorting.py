def bubble_sorting(arr):
	for i in xrange(len(arr)):
		for j in xrange(len(arr)-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

def selecting_sorting(arr):
	for i in xrange(len(arr)):
		mini = i
		for j in xrange(i+1, len(arr)):
			if arr[j] < arr[mini]:
				mini = j
		if mini != i:
			temp = arr[i]
			arr[i] = arr[mini]
			arr[mini] = temp

def merge_sorting(arr):
	pass
	
def main():
	arr = [13,12,10,44,5,67,34,32,1,23]
	bubble_sorting(arr)
	for i in xrange(len(arr)):
		print(arr[i])
	selecting_sorting(arr)
	for i in xrange(len(arr)):
		print(arr[i])

if __name__ == "__main__":
	main()
