def isOnlyDigits(num):
	#devuelve true unicamente si el imput es de solo numeros.
	if num == '':
		return False

	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False

		return True