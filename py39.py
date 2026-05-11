import os

# dir() is a built-in function used to inspect objects.
# It returns a list of names (as strings) that exist inside that object.
# These names are usually attributes, variables, and methods you can use.
#
# dir(os) means: "show everything available in the os module".
# This helps you discover useful functions like listdir, getcwd, mkdir, remove.
print(dir(os))

# Important difference:
# dir(os) -> shows names defined in the os module (introspection/help).
# os.listdir(path) -> returns real files/folders from a directory (filesystem data).
# Example: print(os.listdir("."))

# help() opens Python's built-in documentation system.
# You can type a name inside it (for example: list, str, os) to read docs.
# In scripts, plain help() is interactive, so beginners usually use help(name).

# help(list) shows documentation for the list class:
# what a list is, its methods (append, pop, sort, etc.), and usage examples.
# It is useful when you forget method behavior or arguments.

# Example (uncomment to use):
# help(list)
