""" take an int input then write as many nums as the input. If all the taken nums are +ve then check if any of them are palindromic ints. If both conditions are satisfied then print True else false """

count = int(input())
temp = input()
num_list = temp.split(' ')
temp = ''.join(num_list)
num_list = list(temp)
for i in num_list:
	if int(i) < 0:
		print(False)
		exit()
if num_list == num_list[::-1]:
	print(True)
	exit()
print(False)
