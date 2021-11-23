from FACTOR_ import factor
from tests import test_batch

print("")
print("Testing FACTOR...")
print("")

test_batch(
	[
		([1, 2, 1],),
		([1, 0, -1],),
		([1, -6, 11, -6],),
		([1, 6, 11, 6],),
		([1, 3, 2, 4, 12, 8],),
	],
	[
		"(X + 1)(X + 1)",
		"(X - 1)(X + 1)",
		"(X - 1)(X - 2)(X - 3)",
		"(X + 1)(X + 2)(X + 3)",
		"(X + 1)(X + 2)(X^3 + 4)",
	],
	factor
)

print("")