# CHAPTER 6 EXERCISE 1
'''
Student Grade Lookup (Dictionary) Exercise

A teacher wants a quick way to store and look up student grades.

Create a program that:
- Stores student names and grades in a dictionary
- Lets the user choose from multiple actions:
    add/update a grade
    search a student’s grade
    print all students and grades
    loop until they select 0 (zero)

- If the student is not found, print a message

Example data
"Anna": 5
"Mikko": 4
"Sara": 3

'''
# Dictionary to store student names and their grades
students_grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

def print_menu():
    """Displays the menu for user options."""
    print("\nChoose an option:")
    print("1: Add/Update a grade")
    print("2: Search a student's grade")
    print("3: Print all students and grades")
    print("0: Exit")

def add_update_grade():
    """Adds or updates a student's grade."""
    name = input("Enter the student's name: ").capitalize()
    grade = int(input(f"Enter {name}'s grade: "))
    students_grades[name] = grade
    print(f"{name}'s grade has been updated to {grade}.")

def search_grade():
    """Searches for a student's grade."""
    name = input("Enter the student's name: ").capitalize()
    if name in students_grades:
        print(f"{name}'s grade is: {students_grades[name]}")
    else:
        print(f"Student {name} not found.")

def print_all_grades():
    """Prints all students and their grades."""
    if not students_grades:
        print("No students to display.")
    else:
        print("\nAll Students and Grades:")
        for student, grade in students_grades.items():
            print(f"{student}: {grade}")

def main():
    """Main function that runs the program."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_update_grade()
        elif choice == "2":
            search_grade()
        elif choice == "3":
            print_all_grades()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Running the program
main()

# Hint! Use a dictionary and while loop for example!

