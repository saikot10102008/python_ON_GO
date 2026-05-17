"""
Short, easy-to-read examples of common `dict` methods.

Each block shows one method, what it does in plain language, and a tiny
example that you can run or read quickly.
"""

# Start with a small, simple dictionary.
d = {'a': 1, 'b': 2}


# 1) get(key, default)
# - Returns the value for `key` if present.
# - If the key is missing, returns `default` (None if not given).
print('d before get ->', d)
print("d.get('a') ->", d.get('a'))         # 1
print("d.get('missing', 'no') ->", d.get('missing', 'no'))  # 'no'
print("d.get('missing', 'no') ->", d.get('missing'))  # if default is not given then 'None' will be displayed


# 2) setdefault(key, default)
# - If key exists, returns its value.
# - If missing, inserts key with default and returns that default.
print('\nsetdefault demo:')
print('before ->', d)
val = d.setdefault('c', 0)   # adds 'c': 0 because 'c' was missing
print('returned ->', val)
print('after ->', d)


# 3) keys(), values(), items()
# - They return views (live windows into the dict). Convert to list() for a snapshot.
print('\nviews vs lists:')
print('keys view ->', d.keys())
print('keys list ->', list(d.keys()))


# 4) update(other)
# - Merge another mapping into `d`. Existing keys are overwritten.
print('\nupdate demo:')
print(d)
d.update({'b': 20, 'd': 4})
print('after update ->', d)


# 5) pop(key[, default])
# - Removes and returns the value for key.
# - If key missing and default provided, returns default instead of raising.
print('\npop demo:')
print('pop existing b ->', d.pop('b'))
print("pop missing with default ->", d.pop('nope', 'def'))


# 6) popitem()
# - Removes and returns a 2-tuple (key, value) of the last inserted item.
# - Raises KeyError if the dict is empty.
print('\npopitem demo:')
pair = d.popitem()
print('returned pair ->', pair)   # e.g. ('d', 4)
print('dict now ->', d)


# 7) copy() (shallow)
# - Copies the top-level mapping. Nested mutable values would still be shared.
print('\ncopy demo:')
shallow = d.copy()
print('shallow copy ->', shallow)


# 8) fromkeys(iterable, value=None)
# - Creates a new dict with the given keys, each set to `value`.
print('\nfromkeys demo (simple):')
# fromkeys(keys, value) creates a new dict where every key maps to the same `value`.
# If `value` is mutable (like a list), that one object is shared by all keys.
print("dict.fromkeys(['x','y'], 0) ->", dict.fromkeys(['x', 'y'], 0))
print("dict.fromkeys(['p','q'], []) -> same list object used for both keys ->", dict.fromkeys(['p', 'q'], []))
print('If you need separate mutable objects, use a comprehension: {k: [] for k in keys}')


