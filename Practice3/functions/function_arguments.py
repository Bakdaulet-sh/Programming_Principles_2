# Here is a function with positional arguments.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


# Here is a function with a default argument.
def power(number, exponent=2):
    return number ** exponent


# Here is a function with many positional arguments.
def calculate_sum(*numbers):
    return sum(numbers)


if __name__ == "__main__":
    introduce("Bakdaulet", 20)
    print(power(5))
    print(power(5, 3))
    print(calculate_sum(1, 2, 3, 4))
