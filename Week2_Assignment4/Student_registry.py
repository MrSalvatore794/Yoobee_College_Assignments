from typing import List  

class Student:
   
    def __init__(self, full_name: str, age: int, address: str, student_id: str):
        
        self.full_name: str = full_name
        self.age: int = age
        self.address: str = address
        self.student_id: str = student_id

    def display_info(self) -> None:
        print(f"ID: {self.student_id:<10} | Name: {self.full_name:<20} | Age: {self.age:<3} | Address: {self.address}")


class StudentRegistry:

    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def sort_by_age(self, reverse: bool = False) -> None:
        self.students.sort(key=lambda student: student.age, reverse=reverse)

    def display_all(self) -> None:
        if not self.students:
            print("No student records available.")
            return

        print("\n" + "=" * 70)
        print(f"{'STUDENT REGISTRY (SORTED BY AGE)':^70}")
        print("=" * 70)
        for student in self.students:
            student.display_info()
        print("=" * 70 + "\n")


def collect_student_data(registry: StudentRegistry) -> None:
    
    print("Student Information Collection System\n")
    print("Enter student details. Type 'done' when finished or collect up to any number.\n")
    count: int = 0

    while True:
        count += 1
        print(f"Entering Data for Student #{count}")

        student_id: str = input("Enter Student ID (or type 'done' to stop): ").strip()
        
        if student_id.lower() == 'done':
            break

        full_name: str = input("Enter Full Name: ").strip()
        while True:
            try:
                age: int = int(input("Enter Age: ").strip())
                if age < 0:
                    print("Age cannot be negative. Please enter a valid age.")
                    continue
                break
            except ValueError:
                print("Invalid input! Age must be a whole number (Integer). Try again.")

        address: str = input("Enter Address: ").strip()
        new_student: Student = Student(
            full_name=full_name,
            age=age,
            address=address,
            student_id=student_id
        )

        
        registry.add_student(new_student)
        print(f"Successfully added {full_name}!\n")


def main() -> None:
    
    registry: StudentRegistry = StudentRegistry()
    collect_student_data(registry)

    registry.sort_by_age()
    registry.display_all()


if __name__ == "__main__":
    main()