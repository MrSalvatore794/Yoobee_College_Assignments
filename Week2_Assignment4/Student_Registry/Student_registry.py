class Student:
    def __init__(self, student_id, name, age, address):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Address: {self.address}")


def main():
    students = []
    print("--- Student Registry System ---")

    while True:
        student_id = input("\nEnter Student ID (or type 'done' to stop): ").strip()
        if student_id.lower() == 'done':
            break

        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        address = input("Enter Address: ").strip()

        # Create and add student to list
        students.append(Student(student_id, name, age, address))

    # Sort students by age
    students.sort(key=lambda student: student.age)

    # Display results
    print("\n--- Student Registry (Sorted by Age) ---")
    if not students:
        print("No student records available.")
    else:
        for student in students:
            student.display()


if __name__ == "__main__":
    main()