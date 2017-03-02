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
	return 0

def quick_sort(A, l, r)
    comparision_count = comparision_count + r - l - 1
	if num = 1 return A
	p = choose_pivot_first(A, l, r)
	partition(A, l, r)
	quick_sort(A, l, p)
	quick_sort(A, p+1, r)


file = "../week1-merge-sort/test.txt"
A = read_samples(5, file)
A_sorted, calcs = QuickSort(A, 0, 4)