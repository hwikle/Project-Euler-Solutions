# Filename: problem52.py
# Programmer: Hank Wikle
# Last modified 26 January 2018
# This program solves Problem 52 on Project Euler (Permuted Multiples)

def sameDigits(x, n, verbose=False):
	"""Determines whether x and n * x contain the same digits. Takes integers x and n. Returns a boolean."""

	if verbose:
		print('x: %d' % x)
		print('n: %d' % n)

	xDigits = list(str(x))
	xnDigits = list(str(n*x))

	xDigits.sort()
	xnDigits.sort()

	if verbose:
		print('xDigits:', xDigits)
		print('xnDigits:', xnDigits)

	return xDigits == xnDigits

if __name__ == '__main__':
	i = 1
	done = False
	nvals = [2, 3, 4, 5, 6]

	while not done:
		moveAlong = False
		for n in nvals:
			if not moveAlong and not sameDigits(i, n, True):
				moveAlong = True
				continue

		if not moveAlong:
			print('Solution found: %d' % i)
			done = True

		i += 1
