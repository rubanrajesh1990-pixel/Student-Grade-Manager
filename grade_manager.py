
# Student Grade Manager
# Week 1 - Day 2 Assignment

students = []


# Function 1: Calculate student grade
def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Function 2: Add a student
def add_student():

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty!")
        return

    try:
        mark = float(input("Enter student mark (0-100): "))

    except ValueError:
        print("Error: Please enter a valid number!")
        return

    if mark < 0 or mark > 100:
        print("Error: Mark must be between 0 and 100!")
        return

    grade = get_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"Student {name} added successfully!")


# Function 3: Display student results
def show_results():

    if not students:
        print("\nNo students available. Please add students first.")
        return

    print("\n" + "=" * 45)
    print(f"{'Name':<20}{'Mark':<12}{'Grade':<10}")
    print("-" * 45)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:<12.1f}"
            f"{student['grade']:<10}"
        )

    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * 45)
    print(f"Average : {average:.1f}")
    print(f"Highest : {highest:g}")
    print(f"Lowest  : {lowest:g}")
    print("=" * 45)


# Main Application Menu
def main():

    while True:

        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


# Start application
if __name__ == "__main__":
    main()
