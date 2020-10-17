arr = [9,8,7]

def minmaxE(arr):
	sum = 0
	n = len(arr)
	for i in range(n):
		sum += arr[i]
	print('Maximum sum possibe with n-1 elements is',sum-min(arr))
	print('minimum sum possibe with n-1 elements is',sum-max(arr))

print(minmaxE(arr))
	
	


