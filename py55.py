# Exception handling in Python (very short)
# - use `try` / `except` to catch errors
# - `except ExceptionType as e:` accesses the error object
# - `else:` runs only if no exception was raised
# - `finally:` always runs (cleanup)
# - use `raise` to throw an exception
# - prefer specific exception types; avoid bare `except:`
# - create custom exceptions by subclassing `Exception`

# Minimal example:
# try:
#     risky_operation()
# except ValueError as e:
#     handle_value_error(e)
# else:
#     continue_when_ok()
# finally:
#     cleanup()

