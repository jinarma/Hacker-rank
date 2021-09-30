def list_operations(size):
	ls = []
	for _ in range(size):
		command = input().split()
		if command[0].casefold() == 'insert':
			ls.insert(int(command[1]), int(command[2]))
		elif command[0].casefold() == 'print':
			print(ls)
		elif command[0].casefold() == 'remove':
			ls.remove(int(command[1]))
		elif command[0].casefold() == 'append':
			ls.append(int(command[1]))
		elif command[0].casefold() == 'sort':
			ls.sort()
		elif command[0].casefold() == 'pop':
			ls.pop()
		elif command[0].casefold() == 'reverse':
			ls.reverse()

if __name__ == '__main__':
	list_operations(int(input()))
