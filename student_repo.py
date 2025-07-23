import sqlite3
from student import Student

class StudentRepository:
    """Data Access Layer - Handles database operations for Student entities"""
    
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        """Create students table if it doesn't exist"""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade REAL NOT NULL
            )
        ''')
        self.connection.commit()
    
    def add_student(self, student):
        """Add a student to the database"""
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO students (student_id, name, age, grade)
            VALUES (?, ?, ?, ?)
        ''', (student.student_id, student.name, student.age, student.grade))
        self.connection.commit()
    
    def get_students(self):
        """Fetch all students from the database"""
        cursor = self.connection.cursor()
        cursor.execute('SELECT student_id, name, age, grade FROM students')
        rows = cursor.fetchall()
        
        students = []
        for row in rows:
            student = Student(row[0], row[1], row[2], row[3])
            students.append(student)
        
        return students
    
    def delete_student(self, student_id):
        """Delete a student from the database"""
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.connection.commit()
        return cursor.rowcount > 0  # Return True if a row was deleted
    
    def close_connection(self):
        """Close the database connection"""
        self.connection.close()