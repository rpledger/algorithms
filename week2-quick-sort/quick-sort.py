comparision_count = 0

def read_samples(num, file):
	print "Reading inputs from file {}\n".format(file)
	A =[]
	for s in range(0,num):
		try:
			sample = int(file.readline())
			A.append(sample)
		except(ValueError):
			print "Sample ({}) not an interger".format(sample)
			file.close()
			exit()
	file.close()
	return A

def choose_pivot_first(A, l, r)
	p = 0
	if p != 0:
		A[l], A[p] = A[p], A[l]
	return A

def partition(A, l, r)
	p = A[l]
	i = l + 1
	for j in range (l+1, r):
		if A[j] < p:
			A[i], A[j] = A[j], A[i]
			i = i + 1
	return A

def quick_sort(A, l, r)
    comparision_count = comparision_count + r - l - 1
	if num = 1 return A
	A = choose_pivot_first(A, l, r)
	partition(A, l, r)
	quick_sort(A, l, p)
	quick_sort(A, p+1, r)


file = "../week1-merge-sort/test.txt"
A = read_samples(5, file)
A_sorted, calcs = QuickSort(A, 0, 4)