# sets

# A set is an unordered collection of unique values.
# It automatically removes duplicates.

my_set = {1, 2, 3, 3, 4, 4, 5}
print(f"Initial set: {my_set}")

# Duplicate values are removed automatically.
print(f"Length after removing duplicates: {len(my_set)}")

# Sets do not keep items in a fixed order.
# Because of that, you should not depend on index positions.

# Add a new element to the set.
my_set.add(6)
print(f"After add(6): {my_set}")

# Remove an element from the set.
my_set.remove(2)
print(f"After remove(2): {my_set}")

# discard() is safer than remove() because it does not raise an error
# if the item is not present.
my_set.discard(100)
print(f"After discard(100): {my_set}")

# Membership test: check whether a value exists in the set.
print(f"Is 3 in set? {3 in my_set}")

# Common set operations
even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7}

# Union combines both sets.
print(f"Union: {even_numbers | odd_numbers}")

# Intersection keeps only common values.
print(f"Intersection: {even_numbers & odd_numbers}")

# Difference keeps values that are in the first set but not the second.
print(f"Difference: {even_numbers - odd_numbers}")

# Sets are useful when you want fast duplicate removal
# and quick membership checking.
