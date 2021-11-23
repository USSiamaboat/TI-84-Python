from POLYDIV_ import polydiv
from tests import test_batch

print("")
print("Testing POLYDIV...")
print("")

test_batch(
	[
		(1, 1, [1, 2, 1], 2),
		(1, -1, [1, 2, 6], 2),
		(1, 1, [2, 3, -1], 2),
		(1, -3, [1, -2, 0, -4], 3),
		(1, 2, [2, -3, 4, 5], 3),
	],
	[
		"1.0X^1 + 1.0 R: 0.0",
		"1.0X^1 + 3.0 R: 9.0",
		"2.0X^1 + 1.0 R: -2.0",
		"1.0X^2 + 1.0X^1 + 3.0 R: 5.0",
		"2.0X^2 - 7.0X^1 + 18.0 R: -31.0",
	],
	polydiv
)

print("")