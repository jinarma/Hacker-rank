if __name__ == '__main__':
	count = int(input())
	student_info = {}
	sum_of_list = 0
	for i in range(count):
		temp = input().split(' ')
		temp_s1 = temp[1:]
		student_info[temp[0]] = temp_s1		#important function
	student_name = input()
	for i in student_info[student_name]:
		sum_of_list += float(i)
	print('{:.2f}'.format(sum_of_list/3))
