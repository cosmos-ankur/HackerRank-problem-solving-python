#1st method
def maxnum(arr):
	n = len(arr)
	count = 0
	for i in range(n):
		if(arr[i]==max(arr)):
			count += 1
	return count

#2nd method
def max_num(arr):
	return arr.count(max(arr))

arr = [2,3,3,1]
print(maxnum(arr))
print(max_num(arr))