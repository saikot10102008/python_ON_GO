# python's dictionary is similar to other language's hashmap
# dictionary keys cannot be changed but can be deleted and added after creation
# same value can exist for different keys but keys must be unique

# dictionary is a key-value pair data structure


dict = {"key":"value",0:100}
print(dict["key"],dict[0]) # values can be accessed using keys
print(dict)

# chnging values in dict
dict["key"] = "changed-value"
dict.update({0:10}) # this updates existing key linked value
dict.update({100:10000}) # this doesn't exist , so python creates a key:value pair itself
dict["key-2"] = "another-value" # this is also non-existent , so python creates it to make it existing
print(dict)

# to delete we can use del function

del dict["key-2"]

print("after running this: del dict[\"key-2\"]")
print(dict)