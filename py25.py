n = int(input("Check if a number is prime or not: "))
count = 0
for i in range(1,n+1,1):
    if n%i == 0:
        count+=1
if (count==2) :
    print("The number is prime")
else:
    print("The number isn't prime number")