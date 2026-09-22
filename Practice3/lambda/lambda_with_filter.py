# Here is a list of numbers for filter.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# Here is a lambda function that keeps even numbers.
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))


# Here is a lambda function that keeps numbers greater than five.
large_numbers = list(filter(lambda number: number > 5, numbers))


if __name__ == "__main__":
    print(even_numbers)
    print(large_numbers)
