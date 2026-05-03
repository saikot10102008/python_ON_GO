# count all the letters , digits and special symbols from a given string
# the give string "P@#yn26at^&i5ve"

str = "P@#yn26at^&i5ve"

digit = 0
letter = 0
special_character = 0

for i in str:
    if i.isdigit() :
        digit+=1
    elif i.isalpha() :
        letter+=1
    else:
        special_character+=1

print(f"letter: {letter}\ndigits: {digit}\nspecial character: {special_character}")