# Find the second greatest element in a list
a = []

num = int(input("How many elements do you want in your list? :"))

for i in range(num):
    a.append(int(input("Give a number: ")))

print(type(a[0]))

largest = a[0]
second_largest = a[0]

for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i

print(f"Largest {largest} and second largest {second_largest}")
