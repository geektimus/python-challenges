"""
Tests for the OOP implementations in the utils module.

This module tests the Person and Student classes, verifying their 
attributes, methods, and inheritance relationships.
"""

from src.utils.oop import Person, Student


class TestOOP:
    """Test cases for object-oriented programming utility classes."""
    def test_person(self):
        """Test Person class initialization and greeting method."""
        p = Person("John", 25)
        assert p.name == "John"
        assert p.age == 25
        assert p.greeting() == "Hi John"

    def test_student(self):
        """Test Student class initialization, greeting method, and inheritance from Person."""
        s = Student("Jane", 20, "S12345")
        assert s.name == "Jane"
        assert s.age == 20
        assert s.student_id == "S12345"
        assert s.greeting() == "Hi Jane. Your student id is S12345"

        # Test inheritance
        assert isinstance(s, Person)
