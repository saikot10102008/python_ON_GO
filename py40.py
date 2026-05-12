a = [1, 2, 5, 6, 78, 3, 4, 5, 2, 9, 8, 99, 9]
print(a)
a.sort()
print(a)
a.reverse()
print(a)
intputo = input()

# can't use a.sort().reverse() cause a.sort() returns None. So reverse can't run on None;
# it needs a list to run on.
