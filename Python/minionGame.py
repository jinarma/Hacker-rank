def minion_game(string):
	# your code goes here
	vowels = ['A', 'E', 'I', 'O', 'U']
	counter = 0
	stuart, kevin = 0, 0

	# This is for stuart --------
	for i, ele in enumerate(string):
		counter = i+1
		for j, ele2 in enumerate(string):
			if ele2 not in vowels and len(string[j:j+counter]) == counter:
				stuart += 1
	
	# This is for kevin --------
	counter = 0
	for i, ele in enumerate(string):
		counter = i+1
		for j, ele2 in enumerate(string):
			if ele2 in vowels and len(string[j:j+counter]) == counter:
				kevin += 1

	if stuart > kevin:
		print(f'Stuart {stuart}')
	elif kevin > stuart:
		print(f'Kevin {kevin}')
	else:
		print('Draw')

if __name__ == '__main__':
	s = input()
	minion_game(s)
