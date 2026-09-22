# Here is a class with a class variable shared by all objects.
class Student:
    university = "KBTU"

    # Here is the constructor that creates an instance variable.
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    first_student = Student("Bakdaulet")
    second_student = Student("Ali")
    print(first_student.name, first_student.university)
    print(second_student.name, second_student.university)
