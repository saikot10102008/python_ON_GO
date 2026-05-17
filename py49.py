"""
Shallow vs Deep Copy examples in Python

This file contains commented examples using lists and dictionaries
to demonstrate the difference between shallow and deep copies.

Key points (brief):
- Assignment (e.g., `b = a`) does NOT copy; both names refer to the same object.
- Shallow copy (e.g., `list.copy()`, slicing, `dict.copy()`, or `copy.copy`) copies
	the container but not the nested objects — nested objects are shared.
- Deep copy (`copy.deepcopy`) recursively copies nested objects so mutations
	to the copy do not affect the original.
"""

def separator(title):
		print('\n' + '=' * 8 + f' {title} ' + '=' * 8)


# 1) Assignment (no copy) — both names point to the same object
separator('Assignment (no copy)')
original = [1, 2, 3]
alias = original  # no copy, alias and original are the same object
alias[0] = 99
print('original after alias[0]=99 ->', original)  # original changed
print('alias is original ->', alias is original)


# 2) Shallow copy with a simple (flat) list
separator('Shallow copy: flat list')
flat = [1, 2, 3]
shallow_flat = flat.copy()  # or list(flat) or flat[:]
shallow_flat[0] = 10
print('flat ->', flat)
print('shallow_flat ->', shallow_flat)
print('flat is shallow_flat ->', flat is shallow_flat)


# 3) Shallow copy with nested list — nested objects are shared
separator('Shallow copy: nested list')
nested = [[1, 2], [3, 4]]
shallow_nested = nested.copy()  # top-level list copied, inner lists are shared

# Mutate an element inside a nested object
shallow_nested[0][0] = 'changed'
print('nested after shallow_nested[0][0] = "changed" ->', nested)
print('shallow_nested ->', shallow_nested)

# Reassign a top-level element in the shallow copy (does not affect original)
shallow_nested[0] = ['new']
print('after shallow_nested[0] = ["new"]:')
print('nested ->', nested)
print('shallow_nested ->', shallow_nested)


# 4) Shallow copy for dictionaries
separator('Shallow copy: dictionary')
orig_dict = {'a': 1, 'b': [2, 3]}
shallow_dict = orig_dict.copy()

# Mutating the nested list affects both
shallow_dict['b'].append(4)
print('orig_dict after shallow_dict["b"].append(4) ->', orig_dict)

# Reassigning a top-level key in shallow_dict won't change orig_dict
shallow_dict['a'] = 999
print('orig_dict after shallow_dict["a"] = 999 ->', orig_dict)
print('shallow_dict ->', shallow_dict)



# 5) Deep copy — conceptual explanation and manual example (no imports)
#
# A deep copy means creating new nested containers so that the copy
# does not share any mutable sub-objects with the original. Below is
# a manual way to build a deep-like copy for this specific structure
# without using `copy.deepcopy` or importing anything.
separator('Deep copy: nested structures (manual, no imports)')
complex_obj = {'x': [1, [2, 3]], 'y': {'z': 5}}

# Manual deep copy by explicitly creating new nested containers
manual_deep = {
	'x': [complex_obj['x'][0], list(complex_obj['x'][1])],
	'y': {'z': complex_obj['y']['z']}
}

# Mutate nested data in the manual deep copy
manual_deep['x'][1][0] = 'deep-changed'
manual_deep['y']['z'] = 'deep-z'

print('complex_obj ->', complex_obj)
print('manual_deep ->', manual_deep)


if __name__ == '__main__':
		# Running the module will execute the examples above.
		pass

