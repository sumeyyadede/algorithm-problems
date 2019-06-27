
def insertion_sorting(arr):
	for i in xrange(1, len(arr)):
		key = arr[i] 
		j = i - 1 
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key 

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

def quick_sorting(arr):
	high = []
	low = []
	pivot_list = []

	if len(arr) <= 1:
		return arr

	else:
		pivot = arr[0]

		for i in xrange(len(arr)):
			if arr[i] < pivot:
				low.append(arr[i])

			elif arr[i] > pivot:
				high.append(arr[i])

			else:
				pivot_list.append(arr[i])

			high = quick_sorting(high)
			low = quick_sorting(low)

	return low + pivot_list + high 

def merge_sorting(arr):

	result = []

	if len(arr) < 2:
		return arr

	mid = len(arr) / 2
	first_section = merge_sorting(arr[:mid])
	second_section = merge_sorting(arr[mid:]) 
	i = 0
	j = 0

	while i < len(first_section) and j < len(second_section):
		
		if first_section[i] < second_section[j]:
			result.append(first_section[i])
			i = i + 1

		else:
			result.append(second_section[j])
			j = j + 1

	result = result + first_section[i:]
	result = result + second_section[j:]

	return result

def main():	

	arr = [13,12,10,44,5,67,34,32,1,23]

	insertion_sorting(arr)
	for i in xrange(len(arr)):
		print(arr[i])

	# bubble_sorting(arr)
	# for i in xrange(len(arr)):
	# 	print(arr[i])

	# selecting_sorting(arr)
	# for i in xrange(len(arr)):
	# 	print(arr[i])

	# print(quick_sorting(arr))
	# print(quick_sorting(arr, 0, 9))

	# print(arr)	
	# print(merge_sorting(arr))


if __name__ == "__main__":
	main()


# def quick_sort_in_the_same_array(arr, start, end):
# 	if start < end:
# 		p_index = partition(arr, start, end)
# 		quick_sort_in_the_same_array(arr, start, p_index - 1)
# 		quick_sort_in_the_same_array(arr, p_index + 1, end)

	# if len(arr) <= 1:
	# 	return arr

	# else:
	# 	pivot = arr[len(arr) - 1]
	# 	wall = 0
		
	# 	for i  in xrange(len(arr) - 1):
	# 		if arr[i] <= pivot:
	# 			print(arr[i])
	# 			temp = arr[wall]
	# 			arr[wall] = arr[i]
	# 			arr[i] = temp
	# 			wall = wall + 1

	# 	temp = arr[wall]
	# 	arr[wall] = arr[i + 1]
	# 	arr[i + 1] = temp				

	# 	quick_sort_in_the_same_array(arr[:wall])
	# 	# quick_sort_in_the_same_array(arr[(wall + 1):])

	# 	return arr

# def partition(arr, start, end):
# 	pivot = arr[end]
# 	p_index = start
		
# 	for i  in xrange(start, end):
# 		if arr[i] <= pivot:
# 			print(arr[i])
# 			temp = arr[p_index]
# 			arr[p_index] = arr[i]
# 			arr[i] = temp
# 			p_index = p_index + 1		

# 	print(arr[i],i)
# 	temp = arr[p_index]
# 	arr[p_index] = arr[i]
# 	arr[i] = temp

# 	return p_index
