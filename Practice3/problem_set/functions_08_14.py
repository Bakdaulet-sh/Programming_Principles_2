import random


# Here is a function that checks whether 0, 0, and 7 appear in order.
def spy_game(numbers):
    sequence = [0, 0, 7]
    position = 0

    for number in numbers:
        if number == sequence[position]:
            position += 1

            if position == len(sequence):
                return True

    return False


# Here is a function that calculates the volume of a sphere.
def sphere_volume(radius):
    return (4 / 3) * 3.141592653589793 * radius ** 3


# Here is a function that removes duplicate elements without using set.
def unique_elements(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


# Here is a function that checks whether a string is a palindrome.
def is_palindrome(text):
    cleaned_text = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    return cleaned_text == cleaned_text[::-1]


# Here is a function that prints a histogram using asterisks.
def histogram(numbers):
    for number in numbers:
        print("*" * number)


# Here is a function that implements the number guessing game.
def guess_number_game():
    secret_number = random.randint(1, 20)

    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(
                f"Good job, {name}! "
                f"You guessed my number in {attempts} guesses."
            )
            break


if __name__ == "__main__":
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(spy_game([1, 0, 2, 4, 0, 5, 7]))
    print(spy_game([1, 7, 2, 0, 4, 5, 0]))

    print("Sphere volume:", sphere_volume(3))
    print("Unique:", unique_elements([1, 2, 2, 3, 1, 4]))
    print("Palindrome:", is_palindrome("Madam"))

    histogram([4, 9, 7])
