def combinations(x, y, z, n):
	new_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k is not n]
	print(new_list)

combinations(int(input()), int(input()), int(input()), int(input()))