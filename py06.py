# set data type


# set -> A set is a collection of unique items with no order.


# Creating a set (uses curly braces {})


unique_number = {1, 2, 3, 3, 3, 4, 5, 5}
print(unique_number)  # Output: {1, 2, 3, 4, 5}


"""
What happened here?

We tried to add: 1, 2, 3, 3, 3, 4, 5, 5

Set removes duplicates automatically

Result: {1, 2, 3, 4, 5} (no duplicates!)
"""


"""
Key Properties of Sets:
No duplicates - Automatically removes same values

No order - Items don't have positions like lists

Can't access by index - unique_number[0] will give ERROR

Mutable - Can add/remove items (except frozenset)
"""


# frozenset -> A frozenset is an immutable (unchangeable) version of a set in Python that cannot be modified after creation.
# Creating a frozenset (immutable set)
immutable_set = frozenset([1, 2, 3, 3, 4, 4])
print(immutable_set)  # Output: frozenset({1, 2, 3, 4})


# syntax of frozenset : frozenset(iterable)
# Where iterable can be: list, tuple, string, set, etc.
# From a list:
# fs1 = frozenset([1, 2, 3, 4, 5])
# print(fs1)  # frozenset({1, 2, 3, 4, 5})
