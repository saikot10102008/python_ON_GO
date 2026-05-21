try:
    print("Code that can crash")
    # syntax error is not an exception
    print(0/0)
except Exception as e: # e is a variable that contains the error reasoning
    print(f"The error: {e}")
else:
    print("Code ran without any exception")
finally:
    print("Code didn't stop")