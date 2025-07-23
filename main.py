from student_service import StudentService

class StudentManagementApp:
    """Presentation Layer - Command Line Interface for Student Management System"""
    
    def __init__(self):
        self.service = StudentService()
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*40)
        print("Student Management System")
        print("="*40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        print("="*40)
    
    def add_student_ui(self):
        """Handle adding a new student through UI"""
        try:
            print("\n--- Add New Student ---")
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = float(input("Enter Student Grade: "))
            
            result = self.service.add_student(student_id, name, age, grade)
            print(f"\n✓ {result}")
            
        except ValueError as e:
            print(f"\n✗ Error: {e}")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
    
    def view_students_ui(self):
        """Handle viewing all students through UI"""
        try:
            print("\n--- All Students ---")
            students = self.service.get_students()
            
            if not students:
                print("No students found in the database.")
            else:
                print(f"\nTotal Students: {len(students)}")
                print("-" * 60)
                for student in students:
                    print(student)
                print("-" * 60)
                    
        except Exception as e:
            print(f"\n✗ Error retrieving students: {e}")
    
    def delete_student_ui(self):
        """Handle deleting a student through UI"""
        try:
            print("\n--- Delete Student ---")
            student_id = int(input("Enter Student ID to delete: "))
            
            result = self.service.delete_student(student_id)
            print(f"\n✓ {result}")
            
        except ValueError:
            print("\n✗ Error: Please enter a valid student ID (number)")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Student Management System!")
        
        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice: ").strip()
                
                if choice == '1':
                    self.add_student_ui()
                elif choice == '2':
                    self.view_students_ui()
                elif choice == '3':
                    self.delete_student_ui()
                elif choice == '4':
                    print("\nThank you for using Student Management System!")
                    break
                else:
                    print("\n✗ Invalid choice! Please select 1-4.")
                    
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user.")
                break
            except Exception as e:
                print(f"\n✗ Unexpected error: {e}")
        
        # Clean up resources
        self.service.close_service()
        print("System closed successfully.")

# Entry point
if __name__ == "__main__":
    app = StudentManagementApp()
    app.run()