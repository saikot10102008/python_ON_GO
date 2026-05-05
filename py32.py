# Problem: take a number from the user and print its reverse.
# Solution: use a while loop to process the number digit by digit.
# Each loop takes the last digit with `% 10`, adds it to `rev`, and
# removes that digit from `num` with `// 10` until `num` becomes 0.


num = int(input("Give a number to reverse: "))

rev = 0

# `num > 0` means the loop keeps running while digits are still left.
while (num>0) :
    # Move the current last digit to the front of the reversed number.
    rev = (rev*10) + (num%10) # here , we took the last digit by (num%10) and added it to (rev*10) , (rev*10) is used so the that when we add a number from the last it remains in the front for it to revese and not change in value
    
    # Drop the last digit from the original number.
    num //= 10

print(rev)