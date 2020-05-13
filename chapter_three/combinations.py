def check_if_number_might_have_duplicates(num) -> "duplicated_flag":
	duplicated_flag = False
	if len(set(num))+2 <= len(num):
		duplicated_flag = True
	return duplicated_flag


def check_if_number_is_raising(first_digit, second_digit) -> "is_raising":
	is_raising = False
	if first_digit <= second_digit:
		is_raising = True
	return is_raising


def check_for_first_duplication(first_digit, second_digit, duplicated_digit) -> "duplicated_digit":
	if first_digit == second_digit:
		duplicated_digit = first_digit
	return duplicated_digit


def check_for_second_duplication(first_digit, second_digit, duplicated_digit) -> "second_duplication":
	second_duplication = False
	if first_digit == second_digit != duplicated_digit:
		second_duplication = True
	return second_duplication


def check_password_criteria(num) -> "possible_password":
	duplicated_digit = False
	second_duplication = False
	possible_password = False
	for i in range(len(num)):
		j = i+1
		first_digit = num[i:j]
		second_digit = num[j:j+1]
		is_raising = check_if_number_is_raising(first_digit, second_digit)
		if is_raising:
			if not duplicated_digit:
				duplicated_digit = check_for_first_duplication(first_digit, second_digit, duplicated_digit)
			elif not second_duplication:
				second_duplication = check_for_second_duplication(first_digit, second_digit, duplicated_digit)
		else:
			if not second_digit and second_duplication:
				possible_password = True
			break

	return possible_password

def number_of_possible_passwords(borders):
	possible_passwords = []
	for num in range(*borders):
		num_str = str(num)
		duplicate_flag = check_if_number_might_have_duplicates(num_str)
		if duplicate_flag:
			possible_password = check_password_criteria(num_str)
			if possible_password:
				possible_passwords.append(num)

	number_possible_passwords = len(possible_passwords)
	return number_possible_passwords


borders = (372**2, 809**2)
num = number_of_possible_passwords(borders)




