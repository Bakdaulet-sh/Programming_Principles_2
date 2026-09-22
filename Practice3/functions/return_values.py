# Here is a function that returns the larger number.
def maximum(first_number, second_number):
    return first_number if first_number > second_number else second_number


# Here is a function that returns two values.
def calculate(number):
    return number ** 2, number ** 3


# Here is a function that returns a full name.
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


if __name__ == "__main__":
    print(maximum(12, 8))
    print(calculate(4))
    print(full_name("Bakdaulet", "Shamil"))
