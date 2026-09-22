# Here is a list of students represented by dictionaries.
students = [
    {"name": "Alice", "age": 21},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 23},
]


# Here is a lambda function that sorts students by age.
students_by_age = sorted(students, key=lambda student: student["age"])


# Here is a lambda function that sorts students by name.
students_by_name = sorted(students, key=lambda student: student["name"])


if __name__ == "__main__":
    print(students_by_age)
    print(students_by_name)
