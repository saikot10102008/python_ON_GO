# count the frequency of each element in a list

a = [1,22,333,33,333,33,22,1,1,1,1,22,33,33,33,333,333,333,1] # this is the list

d = {} # this is an empty dictionary that we will use to store counting as key-value pair
# key = element and value = frequency

for i in a:
    if i in d.keys():
        d[i] += 1 # if the key exists then increases the value by 1
    else:
        d[i] = 1 # creates a new key if it doesn't exist and sets its value to 1
    


