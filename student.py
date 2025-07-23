class Student:
    """Student model class representing a student entity"""
    
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def __repr__(self):
        return f"Student({self.student_id}, '{self.name}', {self.age}, {self.grade})"