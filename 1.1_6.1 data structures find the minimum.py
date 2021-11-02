# Python program to find the minimum for
# each and every contiguous subarray of
# size k

# Method to find the minimum for each
# and every contiguous subarray of s
# of size k
def printMin(arr, n, k):
	subarray_min = 0

	for i in range(n - k + 1):
		subarray_min = arr[i]
		for j in range(1, k):
			if arr[i + j] < subarray_min:
				min = arr[i + j]
		print(str(subarray_min) + " ", end = "")

# Driver method
if __name__=="__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n = len(arr)
	k = 3
	printMin(arr, n, k)

# This code is contributed by Shiv Shankar
