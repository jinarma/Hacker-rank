# width = 2*(2*n-1)-1
# end to end char length = 2*(size)-1

def print_rangoli(size):
	char_list = []
	a = 97
	for i in range(2*(size)-1):
		if i < size:
			# print(chr(a+size-i-1))
			char_list.append(chr(a+size-i-1))
		else:
			# print(chr(a+i-size+1))	
			char_list.append(chr(a-size+i+1))
	# print(char_list)
	secondary_char_list = []
	final_2D_list = []
	for i in range(size, 0, -1):
		secondary_char_list = []
		for j_tail in range(i-1, size):
			secondary_char_list.append(chr(a+j_tail))
		for j_head in range(i, size):
			secondary_char_list.insert(0, chr(a+j_head))
		# print(secondary_char_list)
		final_2D_list.append(secondary_char_list)
	for i in range(1, size):
		secondary_char_list = []
		for j_tail in range(i, size):
			secondary_char_list.append(chr(a+j_tail))
		for j_head in range(i+1, size):
			secondary_char_list.insert(0, chr(a+j_head))
		# print(secondary_char_list)
		final_2D_list.append(secondary_char_list)
	# print(final_2D_list)
	for ele in final_2D_list:
		string = '-'.join(ele)
		string = string.center(2*(2*size-1)-1, '-')
		print(string)
	
n = int(input())
print_rangoli(n)
