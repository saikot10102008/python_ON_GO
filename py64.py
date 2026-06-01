"""
what happens when you omit () when calling a function

Simple examples and short comments showing the difference between
referencing a function (no parentheses) and calling it (with parentheses).
No advanced concepts used.
"""

# Define a function that returns a value
def greet():
    return 'hello'

# 1) Calling the function with () executes it and gives its return value
called = greet()          # greet() runs the function
print('called ->', called)  # called -> hello

# 2) Omitting () gives you the function object itself, not its result
referenced = greet        # greet is the function object (no call)
print('referenced ->', referenced)  # referenced -> <function greet at 0x...>

# You can call the referenced function later by adding () to it
print('call referenced ->', referenced())  # call referenced -> hello

# 3) Common mistake: expecting a value but getting the function
def add_one(n):
    return n + 1

# Wrong: forget parentheses -> you store the function, not its result
wrong = add_one         # wrong is a function
right = add_one(4)      # right is the result (5)
print('wrong ->', wrong)    # prints the function object
print('right ->', right)    # right -> 5

# 4) Use-case: store functions in a list and call them when needed
def a():
    return 'A'
def b():
    return 'B'

funcs = [a, b]          # list of function objects
results = [f() for f in funcs]  # call each function
print('results from funcs ->', results)  # ['A', 'B']

# Short note: functions are values you can pass around. Use () when
# you want to execute and get the returned value; omit () when you
# want to refer to the function itself (to assign, store, or pass it).

