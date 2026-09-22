import math


# Here is a class that reads a string and prints it in uppercase.
class StringHandler:
    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


# Here is a base Shape class with area zero.
class Shape:
    def area(self):
        return 0


# Here is a Square class that calculates its area.
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Here is a Rectangle class that calculates its area.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Here is a Point class with coordinates and distance calculation.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        )


# Here is a bank account class with deposit and withdrawal methods.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


# Here is a function that filters prime numbers using filter and lambda.
def prime_numbers(numbers):
    def is_prime(number):
        if number < 2:
            return False

        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                return False

        return True

    return list(filter(lambda number: is_prime(number), numbers))


if __name__ == "__main__":
    handler = StringHandler()
    handler.text = "hello python"
    handler.printString()

    shape = Shape()
    square = Square(5)
    rectangle = Rectangle(4, 6)

    print("Shape area:", shape.area())
    print("Square area:", square.area())
    print("Rectangle area:", rectangle.area())

    first_point = Point(0, 0)
    second_point = Point(3, 4)

    first_point.show()
    first_point.move(1, 1)
    first_point.show()
    print("Distance:", second_point.dist(first_point))

    account = BankAccount("Bakdaulet", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(2000)
    account.show_balance()

    print("Primes:", prime_numbers([1, 2, 3, 4, 5, 7, 9, 11]))
