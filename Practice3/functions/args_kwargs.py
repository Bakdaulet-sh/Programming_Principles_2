# Here is a function that accepts many positional arguments.
def show_numbers(*numbers):
    for number in numbers:
        print(number)


# Here is a function that accepts many keyword arguments.
def show_profile(**profile):
    for key, value in profile.items():
        print(f"{key}: {value}")


# Here is a function using both forms.
def describe_person(*hobbies, **details):
    print("Hobbies:", hobbies)
    print("Details:", details)


if __name__ == "__main__":
    show_numbers(10, 20, 30)
    show_profile(name="Bakdaulet", age=20, city="Almaty")
    describe_person("games", "movies", name="Bakdaulet", age=20)
