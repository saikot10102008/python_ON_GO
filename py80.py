dict = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4
}


print(dict.items())

for i , x in dict.items():
    print(f"{i:5} = {x:03.2f}")
    