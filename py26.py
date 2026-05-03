# reversing a string

string = "SAIKOT"
print(string)
string = string[::-1]
print(string)

# reversing a string using a loop and by string concatenation
new_string = ""
for i in range(len(string)-1,-1,-1):
    new_string += string[i]

print(new_string)

