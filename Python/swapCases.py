def swap_case(string):
	temp_string = ''
	for i in string:
		if i.isalpha():
			if i == i.casefold():
				i = i.upper()
			else:
				i = i.lower()
		temp_string += i
	return temp_string
if __name__ == '__main__':
	print(swap_case(input()))