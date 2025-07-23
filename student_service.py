from student import Student
from student_repo import StudentRepository

class StudentService:
    """Business Logic Layer - Contains core logic for managing student records"""
    
    def __init__(self):
        self.repository = StudentRepository()
    
    def add_student(self, student_id, name, age, grade):
        """Add a new student with validation"""
        # Validate age (must be greater than 15)
        if age <= 15:
            raise ValueError("Age must be greater than 15")
        
        # Validate grade (must be greater than 70)
        if grade <= 70:
            raise ValueError("Grade must be greater than 70")
        
        # Create a new Student instance
        student = Student(student_id, name, age, grade)
        
        # Add student using repository layer
        self.repository.add_student(student)
        
        return f"Student {name} added successfully!"
    
    def get_students(self):
        """Fetch all students"""
        return self.repository.get_students()
    
    def delete_student(self, student_id):
        """Delete a student by ID"""
        success = self.repository.delete_student(student_id)
        if success:
            return f"Student with ID {student_id} deleted successfully!"
        else:
            return f"Student with ID {student_id} not found!"
    
    def close_service(self):
        """Close the service and database connection"""
        self.repository.close_connection()