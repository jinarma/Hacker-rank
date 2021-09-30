""" not using if condition """
import re
unwanted_characters = "['!', '@', '#', '$', '%', '&', ' ']"
def matrix(code, rows, columns):
	string = ''
	for j in range(rows):
		for i in range(columns):
			string = string + code[i][j]
	temp_string = re.sub(unwanted_characters, ' ', string)
	#print(string)
	temp_list = temp_string.split()
	temp_string = ' '.join(temp_list)
	print(temp_string)
	

matrix_size = input().split()
columns, rows = int(matrix_size[0]), int(matrix_size[1])
matrix_code = []
for i in range(columns):
	matrix_code.append(list(input()))
matrix(matrix_code, rows, columns)
