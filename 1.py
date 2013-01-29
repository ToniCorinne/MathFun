multiples = 0

for x in range(0,1000):
	y = x%3
	z = x%5
	if y == 0 or z ==0:
		multiples = multiples + x
print 'Multiples of 3 and 5 below 1000 summed = ', multiples