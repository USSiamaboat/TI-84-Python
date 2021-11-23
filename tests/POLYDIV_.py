from math import *

def polydiv(div_coef, div_const, dividend, degree):
	x_int = (-1*div_const)/div_coef

	middle = []
	result = []
	for i, coef in enumerate(dividend):
		if i == 0:
			middle.append(0)
		else:
			middle.append(result[i-1]*x_int)
		result.append(dividend[i]+middle[i])
	if div_coef > 1:
		for i, num in enumerate(result):
			result[i] = num / div_coef
	remainder = result[len(result)-1]
	result.pop()
	output = ""
	for i, coef in enumerate(result):
		if coef < 0:
			output += " - "
		elif i > 0:
			output += " + "
		output += str(float(abs(coef)))
		if degree - (i+1) > 0:
			output += "X^"+str(degree - (i+1))
	output += " R: " + str(remainder)
	return output

if __name__ == "__main__":
	div_coef = int(input("Divisor coef: "))
	div_const = int(input("Divisor: "+str(div_coef)+"x+"))
	degree = int(input("Degree:"))
	dividend = []
	for i in range(degree+1):
		temp = int(input("Coef of X^"+str(degree - i)+": "))
		dividend.append(temp)

	print(polydiv(div_coef, div_const, dividend, degree))