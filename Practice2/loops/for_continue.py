# For Loop Continue

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    if fruit == "banana":
        continue

    print(fruit)
