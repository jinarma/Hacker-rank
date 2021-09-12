if __name__ == '__main__':
	combination_list = []
	num_list = []
	name_list = []
	for count in range(int(input())):
		name = input()
		score = float(input())
		combination_list.append([name, score])
	minimum = combination_list[0][1]
	for i, j in combination_list:
		num_list.append(j)
		if j < minimum:
			minimum = j
	num_list.sort()
	for ele in num_list:
		if ele != num_list[0]:
			second_lowest = ele
			break
	for i, j in combination_list:
		if j == second_lowest:
			name_list.append(i)
	name_list.sort()
	for name in name_list:
		print(name)
