
def zero_matrix(matrix,len1,len2):

	rowList = []
	for i in xrange(len1):
		rowList.append(0)

	colList = []
	for j in xrange(len2):
		colList.append(0)

	for i in xrange(len1):
		for j in xrange(len2):
			if matrix[i][j] == 0:
				rowList[i] = 1
				colList[j] = 1

	for i in xrange(len1):
		if (rowList[i] == 1):
			for z in xrange(len2):
				matrix[i][z] = 0

	for j in xrange(len2):
		if (colList[j] == 1):
			for z in xrange(len1):
				matrix[z][j] = 0

	return True

def main():

	len1 = 4
	len2 = 5

	matrix = [[0 for _ in xrange(len2)]for _ in xrange(len1)]

	for i in xrange(len1):
		for j in xrange(len2):
			matrix[i][j] = i + j

	matrix[3][2] = 0

	for i in xrange(len1):
		t = ""
		for j in xrange(len2):
			t = t + str(matrix[i][j]) + "\t"
		print(t)

	print("")

	zero_matrix(matrix,len1,len2)

	for i in xrange(len1):
		t = ""
		for j in xrange(len2):
			t = t + str(matrix[i][j]) + "\t"
		print(t)

if __name__ == "__main__":
	main()
