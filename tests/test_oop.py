import pytest
from src.utils.oop import Person, Student


class TestOOP:
    def test_person(self):
        p = Person("John", 25)
        assert p.name == "John"
        assert p.age == 25
        assert p.greeting() == "Hi John"
    
    def test_student(self):
        s = Student("Jane", 20, "S12345")
        assert s.name == "Jane"
        assert s.age == 20
        assert s.student_id == "S12345"
        assert s.greeting() == "Hi Jane. Your student id is S12345"
        
        # Test inheritance
        assert isinstance(s, Person)