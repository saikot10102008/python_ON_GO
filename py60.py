# Simple non-OOP example showing `raise`
def sqrt_positive(n):
	if n < 0:
		raise ValueError("n must be >= 0")
	return n ** 0.5


if __name__ == "__main__":
	for x in [9, -4]:
		try:
			print(f"sqrt_positive({x}) =", sqrt_positive(x))
		except ValueError as e:
			print(f"Raised: {e}")

