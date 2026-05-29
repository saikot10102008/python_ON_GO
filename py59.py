# Exception handling in Python — very short summary
# - Use `try:` to run code that may raise exceptions
# - Use `except ExceptionType as e:` to handle specific errors
# - Use a bare `except:` only sparingly (catches everything)
# - `else:` runs if no exception was raised
# - `finally:` runs always (use for cleanup)
# - Use `raise` to raise an exception; subclass `Exception` for custom errors
# Keep handlers specific and minimal for clarity
 
# Simple runnable example: safe division demonstrating try/except/else/finally
def safe_divide(a, b):
	try:
		a = float(a)
		b = float(b)
		result = a / b
	except ZeroDivisionError:
		print("Error: division by zero")
		return None
	except ValueError:
		print("Error: non-numeric input")
		return None
	except Exception as e:
		print(f"The Exception: {e}")
	else:
		return result
	finally:
		# cleanup placeholder (runs whether exception occurred or not)
		pass

if __name__ == "__main__":
	print("10 / 2 =", safe_divide(10, 2))
	print("10 / 0 =", safe_divide(10, 0))
	print("'x' / 1 =", safe_divide('x', 1))

