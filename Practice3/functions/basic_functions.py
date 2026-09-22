# Here is a simple function.
def greet_user(name):
    print(f"Hello, {name}!")


# Here is a function that adds two numbers.
def add_numbers(first_number, second_number):
    return first_number + second_number


# Here is a function that checks whether a number is even.
def is_even(number):
    return number % 2 == 0


if __name__ == "__main__":
    greet_user("Bakdaulet")
    print(add_numbers(10, 20))
    print(is_even(8))
