from __future__ import print_function

def rotate_matrix(matrix, len):

	if len == 0:
		return False

	for layer in xrange(len / 2):
		print("layer: " + str(layer))
		first = layer
		last = len-1-first

		for i in xrange(first, last):
			offset = i - first
			print("offset: " + str(offset))
			
			#keep the top
			temp = matrix[first][i]
			#left to top;
			matrix[first][i] = matrix[last-offset][first]
			#bottom to left
			matrix[last-offset][first] = matrix[last][last-offset]
			#right to bottom
			matrix[last][last-offset] = matrix[i][last]
			#temp to right
			matrix[i][last] = temp

	return True

def main():

	len = 4
	matrix = [[0 for _ in xrange(len)] for _ in xrange(len)]

	for i in xrange(len):
	 	for j in xrange(len):
	 		matrix[i][j] = i * len + j

	for i in xrange(len):
		t = ""
		for j in xrange(len):
			t = t + str(matrix[i][j]) + "\t"
		print(t)

	rotate_matrix(matrix, len)

	t = ""
	for i in xrange(len):
		t = t + "".join(str(matrix[i][j]) + "\t" for j in xrange(len)) + "\n"
	print(t)

	#print(str().join((str().join(str(matrix[i][j]) + "\t" for j in xrange(len)) + "\n") for i in xrange(len)))

if __name__ == "__main__":
	main()
