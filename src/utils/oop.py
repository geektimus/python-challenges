"""
Object-oriented programming examples and patterns.

This module demonstrates basic OOP concepts like classes, inheritance, and method overriding.
"""

class Person:
    """
    A basic class representing a person.
    
    Attributes:
        name (str): The person's name
        age (int): The person's age
    """
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            age (int): The person's age
        """
        self.name = name
        self.age = age

    def greeting(self):
        """
        Generate a greeting message for this person.
        
        Returns:
            str: A personalized greeting message
        """
        return f"Hi {self.name}"


class Student(Person):
    """
    A class representing a student, inheriting from Person.
    
    Attributes:
        name (str): The student's name (inherited)
        age (int): The student's age (inherited)
        student_id (str): The student's unique identifier
    """
    def __init__(self, name, age, student_id):
        """
        Initialize a Student object.
        
        Args:
            name (str): The student's name
            age (int): The student's age
            student_id (str): The student's unique identifier
        """
        super().__init__(name, age)
        self.student_id = student_id

    def greeting(self):
        """
        Generate a greeting message for this student, including their ID.
        
        This method overrides the greeting method from the Person class.
        
        Returns:
            str: A personalized greeting message including the student ID
        """
        base_greeting = super().greeting()
        return f"{base_greeting}. Your student id is {self.student_id}"