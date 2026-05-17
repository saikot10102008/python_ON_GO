# write a python script to merge two python dictionaries

# # way-1
# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}
# d3 = {}

# d3.update(d1)
# d3.update(d2)
# print(d3)

# way-2
# merge d1 and d2 into d1
d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i] # this will create new key-value pair in d1 if key doesn't exist and updates if the key already exists
    

print(d1)