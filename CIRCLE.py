from math import *

def circle(type, inarr):
	x = 0
	y = 0
	r = 0
	if type == 1:
		r = inarr[0]
	elif type == 2:
		x = inarr[0]
		y = inarr[1]
		r = inarr[2]
	elif type == 3:
		x = -1 * inarr[0] / 2
		y = -1 * inarr[1] / 2
		r = sqrt((inarr[0]/2)**2 + (inarr[1]/2)**2 - inarr[2])
	output = [[x, y], r, [], []]
	disc = r**2 - y**2
	if disc == 0:
		output[2] = [x + sqrt(disc)]
	elif disc > 0:
		output[2] = [x - sqrt(disc), x + sqrt(disc)]
	disc = r**2 - y**2
	if disc == 0:
		output[3] = [y + sqrt(disc)]
	elif disc > 0:
		output[3] = [y - sqrt(disc), y + sqrt(disc)]
	return output

params = [[], ["r"], ["h", "k", "r"], ["a", "b", "c"]]
print("1: x^2 + y^2 = r^2")
print("2: (x-h)^2 + (y-k)^2 = r^2")
print("3: x^2 + ax + y^2 + bx + c = 0")
type = int(input("Select a type: "))
print("")
inarr = []
for letter in params[type]:
	inarr.append(float(input("Value of "+letter+": ")))
print("")
print("Coords rounded to 3 dec")
print("")
out = circle(type, inarr)
def coord_string(coords):
	return "("+str(round(coords[0], 3))+", "+str(round(coords[1], 3))+")"
print("Center: "+coord_string(out[0]))
print("Radius: "+str(out[1]))
if len(out[2]) == 2:
	print("X-ints: "+coord_string([out[2][0], 0])+" "+coord_string([out[2][1], 0]))
elif len(out[2]) == 1:
	print("X-int: "+coord_string([out[2][0], 0]))
else:
	print("No X-ints")
if len(out[3]) == 2:
	print("Y-ints: "+coord_string([0, out[3][0]])+" "+coord_string([0, out[3][1]]))
elif len(out[3]) == 1:
	print("Y-int: "+coord_string([0, out[3][0]]))
else:
	print("No Y-ints")