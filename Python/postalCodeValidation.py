import re
# Do not delete 'r'.
regex_integer_in_range = r"[1-9][0-9][0-9][0-9][0-9][0-9]"
regex_alternating_repetitive_digit_pair = r""  # Do not delete 'r'.


P = input()
print(bool(re.match(regex_integer_in_range, P)))
for i in range(100000, 1000001):
	if bool(re.match(regex_integer_in_range, str(i))):
		continue
	print(i)
	break
""" print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
 """
