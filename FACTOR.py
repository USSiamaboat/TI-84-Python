from math import *

def allFactors(n):
	n = int(abs(n))
	output = []
	for i in range(n):
		if n/(i+1) == round(n/(i+1)):
			output.append(i+1)
	return output

def shallowCopyArr(arr):
	output = []
	for item in arr:
		output.append(item)
	return output

def simpFrac(frac):
	num = frac[0]
	dem = frac[1]
	i = min(abs(num), abs(dem))
	while i >= 2:
		if abs(num) % i == 0 and abs(dem) % i == 0:
			num = num / i
			dem = dem / i
			break
		i = i - 1
	return [num, dem]

def possibleZeros(poly_coefs):
	fracs = []
	lead_coef = poly_coefs[0]
	const_coef = poly_coefs[len(poly_coefs)-1]
	lead_factors = allFactors(lead_coef)
	const_factors = allFactors(const_coef)
	for lead_factor in lead_factors:
		for const_factor in const_factors:
			fracs.append([const_factor, lead_factor])
	unique_fracs = []
	for frac in fracs:
		simped_frac = simpFrac(frac)
		if simped_frac not in unique_fracs:
			unique_fracs.append(simped_frac)
	output = []
	for frac in unique_fracs:
		output.append(frac)
		opp_frac = shallowCopyArr(frac)
		opp_frac[0] = opp_frac[0]*-1
		output.append(opp_frac)
	return output

def divide(dividend, x_int):
	middle = []
	result = []
	for i, coef in enumerate(dividend):
		if i == 0:
			middle.append(0)
		else:
			middle.append(result[i-1]*x_int)
		result.append(dividend[i]+middle[i])
	remainder = result[len(result)-1]
	result.pop()
	return [result, remainder]

def findZeros(polynomial_coefs, prev = []):
	potential_zeros = possibleZeros(polynomial_coefs)
	if len(potential_zeros) > 0:
		for zero in potential_zeros:
			if divide(polynomial_coefs, zero[0]/zero[1])[1] == 0:
				prev.append(zero)
				return findZeros(divide(polynomial_coefs, zero[0]/zero[1])[0], prev)
	return [prev, polynomial_coefs]

def frac_to_string(frac):
	if frac[0]/frac[1] != round(frac[0]/frac[1]):
		return "(" + str(frac[0]) + "/" + str(frac[1]) + ")"
	else:
		return str(int(frac[0]/frac[1]))

def poly_to_string(poly_coefs):
	output = "("
	if len(poly_coefs) > 1:
		for i in range(len(poly_coefs)):
			if poly_coefs[i] != 0:
				if i != 0:
					if poly_coefs[i] < 0:
						output += " - "
					else:
						output += " + "
				if abs(poly_coefs[i]) != 1 :
					output += str(int(abs(poly_coefs[i])))
				if i != len(poly_coefs) - 1:
					output += "X^" + str(len(poly_coefs)-i-1)
		return output + ")"
	else:
		return str(poly_coefs[0])

def factor(polynomial_coefs):
	zeros_raw = findZeros(polynomial_coefs, [])
	zeros = zeros_raw[0]
	remainder = poly_to_string(zeros_raw[1])
	output = ""

	if "(" not in remainder:
		if remainder == "-1":
			output += "-"
		elif remainder != "1":
			output += remainder

	for zero in zeros:
		output += "("
		if zero[1] != 1:
			temp = ""
			if zero[1] == round(zero[1]):
				temp = str(int(zero[1]))
			else:
				temp = str(zero[1])
			output += temp
		output += "X"
		if zero[0] != 0:
			if zero[0] > 0:
				output += " - "
			else:
				output += " + "
			temp = ""
			if zero[0] == round(zero[0]):
				temp = str(abs(int(zero[0])))
			else:
				temp = str(abs(zero[0]))
			output += temp
		output += ")"
	
	if "(" in remainder:
		output += remainder
	
	return output

if __name__ == "__main__":
	degree = int(input("Degree: "))
	poly = []
	for i in range(degree+1):
		temp = int(input("Coef of X^"+str(degree - i)+": "))
		poly.append(temp)
	print(factor(poly))
