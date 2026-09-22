# Here is a class that provides printing functionality.
class Printable:
    def print_document(self):
        print("Document is printed.")


# Here is a class that provides logging functionality.
class Loggable:
    def log_action(self):
        print("Action was logged.")


# Here is a class that inherits from two parent classes.
class Report(Printable, Loggable):
    def show_report(self):
        print("Report is ready.")


if __name__ == "__main__":
    report = Report()
    report.show_report()
    report.print_document()
    report.log_action()
