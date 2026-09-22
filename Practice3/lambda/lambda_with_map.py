# Here is a list of numbers for map.
numbers = [1, 2, 3, 4, 5]


# Here is a lambda function that squares every number with map.
squared_numbers = list(map(lambda number: number ** 2, numbers))


# Here is a lambda function that doubles every number with map.
doubled_numbers = list(map(lambda number: number * 2, numbers))


if __name__ == "__main__":
    print(squared_numbers)
    print(doubled_numbers)
