# generate list of prime factors of natural number n
def prime_factors(n):
	factors = []
	d = 2
	while d*d <= n:
		while (n%d) == 0:
			factors.append(d)
			n /= d
		d += 1
	if n > 1:
		factors.append(n) 	
	return factors

# generate a list of divisors besides 1 and itself
def divisors(n):
	return [ d for d in range(2,n//2+1) if n % d == 0 ]


