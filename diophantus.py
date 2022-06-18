def diophantus(a, b):
	
	c, d, e, f = 1, 0, 0, 1
	while a % b: a, b, c, d, e, f = b, a % b, e, f, c - e * (a // b), d - f * (a // b)
	return (b, e, f)

def result(a, b):
	
	(gcd, x, y) = diophantus(a, b)
	print(f"GCD of {a} and {b} is {gcd}")
	print(f"{a} * {x} + {b} * {y} = {a * x + b * y}")
	
if __name__ == "__main__":
    result(13, 25)
    result(3, 7)