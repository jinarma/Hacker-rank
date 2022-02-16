# formula 2*(2*n-1)-1

def print_rangoli(size):

	width = 2*(2*size-1)-1
	a = 97
	iter_list = []
	for i in range(size):
		print(chr(a+size-i-1))
n = int(input())
print_rangoli(n)