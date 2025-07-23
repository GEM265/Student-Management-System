# Student-Management-System
**Objective:** The purpose of this assignment is to understand and implement the Layered Architecture pattern using Python. Students will design a simple application with three layers (Presentation, Business Logic, and Data Access) and apply separation of concerns principles.

**Instructions:** You are required to develop a Python-based application using the Layered Architecture pattern. Follow the given steps to structure your application properly.

**Task:**

Implement a **Student Management System (SMS)** that allows users to **add**, **view**, and **delete** student records using a layered architecture approach.

1. **Implement the model with the Student class - (student.py) :**
Student class with attributes (*student_id, name, age, grade*)

2. **Implement Data Access Layer (Repository Layer) with the functions below - (student_repo.py) :**
Handles data storage and retrieval using a database (SQLite).

create an SQLite database and connect

    . def create_table(self): Create students table.
  
    . def add_student(self, student): add the student to students table.
  
    . def get_students(self): fetch all students.
  
    . def delete_student(self, student_id): delete the student from students table.
  
3. **Implement Business Logic Layer (Service Layer) with the functions below - (student_service.py) :**
Contains the core logic for managing student records.

        . def add_student(self, student_id, name, age, grade):
            . check if age is valid (greater than 15)
            . check if grade is valid (greater than 70)
            . If all valid then create a new Student instance and call the repository layer’s add_student function with this instance.
       . def get_students(self): Fetch all students by calling repository layer’s get_students
       . def delete_student(self, student_id): Delete the student by calling repository layer’s delete_student
5. **Implement Presentation Layer (User Interface) - (main.py) :**
Provides a command line interface (CLI) for users to interact with the application. Implement an infinite loop that has an Exit choice.


<img width="257" height="143" alt="image" src="https://github.com/user-attachments/assets/2acb2d3e-1b72-4e33-bea3-2683d65a4bc4" />

