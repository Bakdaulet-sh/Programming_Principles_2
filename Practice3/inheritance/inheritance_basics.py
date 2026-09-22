# Here is a parent class.
class Animal:
    def eat(self):
        print("The animal is eating.")


# Here is a child class that inherits from Animal.
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


if __name__ == "__main__":
    dog = Dog()
    dog.eat()
    dog.bark()
