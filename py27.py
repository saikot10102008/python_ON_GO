# let's check if a string is pallindrome

str = input("Let's see if a string is pallindrome or not: ")

strr = ""
for i in range(len(str)-1,-1,-1):
    strr += str

if strr == str:
    print("Your string is pallindrome")
else:
    print("Your string is not pallindrome")