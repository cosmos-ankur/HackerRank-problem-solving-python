
arr = [0, 100, 35, 0, 94, 40, 42, 87, 59, 0]

def pos(arr):
	n = len(arr)
	pos = neg = zer = 0
	for i in range(n):
		if arr[i] > 0:
			pos += 1
		elif arr[i] < 0:
			neg += 1
		else :
			zer += 1
	print(pos/n)
	print(neg/n)
	print(zer/n)
			

print(pos(arr))
