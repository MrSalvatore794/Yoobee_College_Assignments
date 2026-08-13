class Student:
    def __init__(self, full_name, age, address, student_id):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.student_id = student_id

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.full_name} | Age: {self.age} | Address: {self.address}")


# Helper function to sort students by age (replaces lambda)
def get_student_age(student):
    return student.age


class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def sort_by_age(self):
        # Uses the get_student_age function as the sorting key
        self.students.sort(key=get_student_age)

    def display_all(self):
        if len(self.students) == 0:
            print("No student records available.")
            return

        print("\n==================================================")
        print("        STUDENT REGISTRY (SORTED BY AGE)          ")
        print("==================================================")
        for student in self.students:
            student.display_info()
        print("==================================================\n")


def collect_student_data(registry):
    print("Student Information Collection System\n")
    print("Enter student details. Type 'done' to stop.\n")
    
    count = 1
    while True:
        print(f"Entering Data for Student #{count}")
        student_id = input("Enter Student ID (or type 'done' to stop): ").strip()

        if student_id.lower() == 'done':
            break

        full_name = input("Enter Full Name: ").strip()
        
        # Simple try-except block for integer conversion
        try:
            age = int(input("Enter Age: ").strip())
        except ValueError:
            print("Invalid input! Setting age to 0.")
            age = 0

        address = input("Enter Address: ").strip()

        # Create new student object using positional arguments
        new_student = Student(full_name, age, address, student_id)
        registry.add_student(new_student)
        
        print(f"Successfully added {full_name}!\n")
        count += 1


def main():
    registry = StudentRegistry()
    collect_student_data(registry)
    registry.sort_by_age()
    registry.display_all()


if __name__ == "__main__":
    main()
