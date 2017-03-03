import quick_sort

#comparision_count = 0

file = "QuickSort.txt"
num = int(raw_input("How many samples?: "))
method = int(raw_input("Pivot Method?:\n[0] = First Element\n[1] = Last Element\n[2] = Median of Three\n"))
A = quick_sort.read_samples(num, file)
#print "Input Array: {}".format(A)
A_sorted = quick_sort.quick_sort(A, 0, num, method)
#print "Array sorted: {}".format(A_sorted)
print "Number of Comparisions: {}".format(quick_sort.comparision_count)
