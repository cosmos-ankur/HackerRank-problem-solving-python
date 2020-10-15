
def diagonalDifference(arr):

    primdiag = secnddiag = 0
    for i in range(n):
        primdiag += arr[i][i]
        secnddiag += arr[i][n-i-1]
    return abs((primdiag-secnddiag))




	
	


	





mat = [[1,2,3],
[4,5,6],
[7,8,9]]
n = 3
print(diagonalDifference(mat))