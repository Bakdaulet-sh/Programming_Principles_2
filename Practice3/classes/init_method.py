# Here is a class that uses __init__ to initialize object data.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Here is a method that displays student information.
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":
    student = Student("Bakdaulet", 20)
    student.show_info()
