import itertools


# Here is a function that converts grams to ounces.
def grams_to_ounces(grams):
    return 28.3495231 * grams


# Here is a function that converts Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


# Here is a function that solves the chicken and rabbit puzzle.
def solve(numheads, numlegs):
    if numlegs % 2 != 0:
        return None

    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    if chickens < 0 or rabbits < 0:
        return None

    if 2 * chickens + 4 * rabbits != numlegs:
        return None

    return chickens, rabbits


# Here is a function that returns only prime numbers from a list.
def filter_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False

        return True

    return [number for number in numbers if is_prime(number)]


# Here is a function that prints every permutation of a string.
def print_permutations(text):
    for permutation in itertools.permutations(text):
        print("".join(permutation))


# Here is a function that reverses the order of words.
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


# Here is a function that checks whether two 3s are next to each other.
def has_33(numbers):
    return any(
        numbers[index] == 3 and numbers[index + 1] == 3
        for index in range(len(numbers) - 1)
    )


if __name__ == "__main__":
    print("Ounces:", grams_to_ounces(100))
    print("Celsius:", fahrenheit_to_celsius(68))
    print("Chickens and rabbits:", solve(35, 94))
    print("Primes:", filter_prime([1, 2, 3, 4, 5, 7, 9]))
    print("Reversed:", reverse_words("We are ready"))
    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
