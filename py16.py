# string and string slicing experimentation


string_var = "STRING"

a = string_var[-1]
b = string_var[5]

print(a,b) # comma ( , ) adds a space btween a and b variable

print(string_var[0:5:1]) # STRIN
print(string_var[:5:1]) # STRIN
print(string_var[0::1]) # STRING
print(string_var[0:5:]) # STRIN
print(string_var[0:6:]) # STRING
print(string_var[0:999999999999999999999999999999999999999999999999999999999:]) # STRING
print(string_var[0:5]) # STRIN
print(string_var[::1]) # STRING
print(string_var[::2]) # SRN
print(string_var[::]) # STRING

print (" Type of this data type: ",type(string_var))
print(" we can use comma to concatenate anything but we cannot we + unless until both are string")
print("string-1"+" string-2") # comma provides a space but + doesn't




