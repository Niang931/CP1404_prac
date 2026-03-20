
class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} with {self.student_id} = {self.gpa}"

    def __repr__(self):
        """For debugging and can print a list of objects"""
        # return f"{self.name} {self.gpa}"
        return str(vars(self))

    def run_tests(self):


student1 = Student('Naing','14892409', 9.0)
print(student1)