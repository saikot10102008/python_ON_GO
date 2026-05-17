# pop and poitem method in dict
d = {"key": "value", 0: 10, 100: 10000, "key-2": "another-value"}

print(d)

# `pop(key)` removes the specified key and returns its value.
# If the key is not present, `pop` raises KeyError unless a default is provided.
a = d.pop("key")
print(a)   # prints the value that was removed
print(d)   # dictionary after removing the key

# `popitem()` removes and returns a 2-tuple (key, value).
# On Python 3.7+ `dict` preserves insertion order, so `popitem()`
# removes the *last inserted* item (the most recent key).
# It raises KeyError if the dictionary is empty.
b = d.popitem()
print(b)   # prints a 2-tuple (key, value) e.g. ('key-2', 'another-value')
print(d)   # dictionary after removing that item

# Note on 2-tuple:
# - A "2-tuple" is simply a tuple with exactly two elements, e.g. ('a', 1).
# - It's the same `tuple` type as any other tuple; the term only describes length.
# - You can unpack a 2-tuple directly: `k, v = b` will assign the key to `k` and
#   the value to `v`.
