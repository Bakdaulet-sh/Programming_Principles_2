# Here is a parent class with a method that can be overridden.
class Animal:
    def speak(self):
        print("The animal makes a sound.")


# Here is a child class that overrides the parent method.
class Cat(Animal):
    def speak(self):
        print("The cat says meow.")


if __name__ == "__main__":
    animal = Animal()
    cat = Cat()
    animal.speak()
    cat.speak()
