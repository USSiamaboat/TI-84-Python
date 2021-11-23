def test(in_arr, expected, func):
	actual = ""
	actual = func(*in_arr)
	if actual == expected:
		print("Pass")
	else:
		print("")
		print("Fail")
		print("Inputs: " + str([*in_arr]))
		print("Output: " +  actual)
		print("Expected: " + expected)
		print("")

def test_batch(in_arr_arr, expected_arr, func):
	for i, in_arr in enumerate(in_arr_arr):
		test(in_arr, expected_arr[i], func)
