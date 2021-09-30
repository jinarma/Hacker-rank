""" All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits. """


s1 = 'Sorting123'
string_list = sorted(s1)
s2 = ''
for i in string_list:
	if ord(i) >= 48 and ord(i) <= 57:
		s2 += i
	elif ord(i) >

