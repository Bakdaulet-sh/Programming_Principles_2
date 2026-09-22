from functions_01_07 import grams_to_ounces, filter_prime, reverse_words
from functions_08_14 import sphere_volume, unique_elements


# Here is an example that imports and uses functions from other files.
def run_import_examples():
    print("Ounces:", grams_to_ounces(100))
    print("Primes:", filter_prime([1, 2, 3, 4, 5, 6, 7]))
    print("Reversed:", reverse_words("We are ready"))
    print("Sphere volume:", sphere_volume(3))
    print("Unique:", unique_elements([1, 2, 2, 3, 1]))


if __name__ == "__main__":
    run_import_examples()
