def Merge(arr_a, arr_b, less_or_eq):
	result = []
	i = j = 0
	len_a, len_b = len(arr_a), len(arr_b)
	while i < len_a and j < len_b:
		if less_or_eq(arr_a[i], arr_b[j]):
			result.append(arr_a[i])
			i += 1
		else:
			result.append(arr_b[j])
			j += 1
	if i == len_a:
		while j < len_b:
			result.append(arr_b[j])
			j += 1
	else:
		while i < len_a:
			result.append(arr_a[i])
			i += 1
	return result


def MergeSort(arr, order):
	less_or_eq = order
	left, right = 0, len(arr) - 1
	if left < right:
		arr_left, arr_right = divide(arr)
		arr_left = MergeSort(arr_left, order)
		arr_right = MergeSort(arr_right, order)
		result = Merge(arr_left, arr_right, less_or_eq)
		return result
	else:
		return arr


def divide(arr):
	length = len(arr)
	if length % 2 == 0:
		middle = length / 2 - 0.5
	else:
		middle = length / 2
	lower_half = []
	upper_half = []
	for i in range(length):
		if i < middle:
			lower_half.append(arr[i])
		else:
			upper_half.append(arr[i])
	return (lower_half, upper_half)


def numeric_less_or_eq(a, b):
	return a <= b


def utf_8_lexicographic_less_or_eq(str_a, str_b):
	
	str_a, str_b = str_a.strip(), str_b.strip()
	len_a, len_b = len(str_a), len(str_b)
	for i in range(len_a):
		if i == len_b:
			return False
		char_a, char_b = str_a[i], str_b[i]
		code_a, code_b = char_a.encode("utf_8"), char_b.encode("utf-8")
		if code_a == code_b:
			i += 1
			continue
		return code_a < code_b
	return True


def numeric_MergeSort(arr):
	return MergeSort(arr, numeric_less_or_eq)
	
	
def string_MergeSort(arr):
	return MergeSort(arr, utf_8_lexicographic_less_or_eq)
