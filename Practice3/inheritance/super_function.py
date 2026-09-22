# Here is a parent class with a constructor.
class Person:
    def __init__(self, name):
        self.name = name


# Here is a child class that uses super() to call the parent constructor.
class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    # Here is a method that displays inherited and new data.
    def show_info(self):
        print(f"{self.name} studies at {self.university}.")


if __name__ == "__main__":
    student = Student("Bakdaulet", "KBTU")
    student.show_info()
