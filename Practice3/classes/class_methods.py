# Here is a class with instance methods and a class method.
class Calculator:
    operation_count = 0

    # Here is an instance method that adds two numbers.
    def add(self, first_number, second_number):
        Calculator.operation_count += 1
        return first_number + second_number

    # Here is an instance method that multiplies two numbers.
    def multiply(self, first_number, second_number):
        Calculator.operation_count += 1
        return first_number * second_number

    # Here is a class method that shows the operation count.
    @classmethod
    def show_operation_count(cls):
        print(f"Operations: {cls.operation_count}")


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(4, 5))
    print(calculator.multiply(3, 6))
    Calculator.show_operation_count()
