Biggie = 0
a = 0
b = 1

while b < 4000000:
	a, b = b, a + b
	print 'a',a
	print 'b', b
	if b%2 == 0:
		Biggie = Biggie + b

print "Sum of even-valued Fibonacci sequence =", Biggie