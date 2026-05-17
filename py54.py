# write a python program to combine two dictionary by adding values for common keys
d1 = {10:100,20:200,30:300,40:400}
d2 = {40:400,50:500,60:600,30:300}
#let's combine d1 & d2 in d1

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i] # if a key in d2 exists in d1 then values are combined and saved in d1
    else:
        d1[i] = d2[i] # if the key from d2 doesn't exist in d1 then it creates a new one in d1 and assigns the value from d2 to d1

print(d1)