# sperate each digit of a number and print it on the new line
# // -> it is floor division -> if a number is 123 and we divide it by 10 using floor division we will get 12 , that means we get the number without the last digit
# % -> it is Modulo operator: it gives the remainder after division -> this gives us the last digit of a number if we do (number % 10)

n = int(input("Give a number: "))

while (n>0) :
    print(n%10) # this prints the last digit
    n //= 10 # this cuts off the last digit