# dictionary traversing

d = {"key": "changed-value", 0: 10, 100: 10000, "key-2": "another-value"}
# we can directly iterate using for loop

for i in d: # this iterates through the keys
    print(i)


for i in d.keys(): # this iterates through the keys
    print(i)


for i in d.values(): # this iterates through the values
    print(i)

