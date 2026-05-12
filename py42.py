# check if a list is sorted or not

a = []

num = int(input("How many elements do you want in your list? :"))

for i in range(num):
    a.append(int(input("Give a number: ")))

for i in range(len(a) - 1):  # I can't use len(a) because in that case we will be trying to access index number len(a) which is invalid
    if a[i] < a[i + 1]:
        continue
    else:
        print("The list is not sorted!")
        break

else:
    print("The list is sorted!")
