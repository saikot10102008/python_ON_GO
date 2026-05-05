# Accept a number and check if it is a pallindromic number

# at first, I need to revrerse the number given, then compare the reversed number and given number, if they are 
# same then it is pallindromic

num = int(input("Give a number: "))

rev = 0 # rev stands for reverse

copy_of_num = num

while (num > 0) :
    rev = (rev*10) + (num%10)
    num //= 10

if (rev == copy_of_num) :
    print("The given number is pallindromic")
else:
    print("The given number is not pallindromic")