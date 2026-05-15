# a = {} -> this is not an empty set, this is an empty dictionary

a = {1,2,3}
b = {3,4,5}

c = a.union(b) # this doesn't change a and b
d = a|b # this is also union operation
e = a
e |= b

print(f"{a}\n{b}\n{c}\n{d}\n{e}")
