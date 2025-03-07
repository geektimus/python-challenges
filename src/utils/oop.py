class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi {self.name}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greeting(self):
        base_greeting = super().greeting()
        return f"{base_greeting}. Your student id is {self.student_id}"