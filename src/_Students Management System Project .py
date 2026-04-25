# Generated from: _Students Management System Project .ipynb
# Converted at: 2026-04-25T04:38:14.092Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

student_grades = {}

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with {grade}")
    save_data()

# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks updated to {grade}")
        save_data()
    else:
        print(f"{name} not found!")

# Delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted")
        save_data()
    else:
        print(f"{name} not found!")

# Display all students
def display_all():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No data found")

# Search student
def search_student(name):
    if name in student_grades:
        print(f"{name} scored {student_grades[name]}")
    else:
        print("Student not found")

# Class statistics
def show_stats():
    if student_grades:
        grades = list(student_grades.values())
        avg = sum(grades) / len(grades)
        print(f"Average Marks: {avg:.2f}")
        print(f"Highest Marks: {max(grades)}")
        print(f"Lowest Marks: {min(grades)}")
    else:
        print("No data available")

def main():
    load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Show Statistics")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Enter a valid number!")
            continue

        if choice == 1:
            name = input("Enter name: ")
            try:
                grade = int(input("Enter grade: "))
                add_student(name, grade)
            except:
                print("Invalid grade!")

        elif choice == 2:
            name = input("Enter name: ")
            try:
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
            except:
                print("Invalid grade!")

        elif choice == 3:
            name = input("Enter name: ")
            delete_student(name)

        elif choice == 4:
            display_all()

        elif choice == 5:
            name = input("Enter name: ")
            search_student(name)

        elif choice == 6:
            show_stats()

        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

main()