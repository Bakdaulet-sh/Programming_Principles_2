# Here is a lambda function that adds two numbers.
add_numbers = lambda first_number, second_number: first_number + second_number


# Here is a lambda function that squares a number.
square_number = lambda number: number ** 2


# Here is a lambda function that checks for an even number.
is_even = lambda number: number % 2 == 0


# Here is a lambda function that converts text to uppercase.
to_upper = lambda text: text.upper()


if __name__ == "__main__":
    print(add_numbers(5, 7))
    print(square_number(6))
    print(is_even(10))
    print(to_upper("python"))
