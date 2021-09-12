""" take an int input then write as many nums as the input. If all the taken nums are +ve then check if any of them are palindromic ints. If both conditions are satisfied then print Ture else false """

count = int(input())
temp = input()
num_list = temp.split(' ')
for i in count:
	if i//2 <= 3:
		pass