class Person:
    def setup_person(self, person_id, name):
        self.id = person_id
        self.name = name

class Student(Person):
    def setup_student(self, student_id, name):
        self.setup_person(student_id, name)  # Inherits from Person
        self.courses = []

    def enroll_course(self, course):
        if len(course.students) < course.capacity:
            self.courses.append(course.title)
            course.students.append(self.name)
            print(f"\n=> SUCCESS: {self.name} has been enrolled in {course.title}.")
        else:
            print(f"\n=> WAITLIST: Sorry, {course.title} is at full capacity.")

class Staff(Person):
    def setup_staff(self, staff_id, name, tax_num):
        self.setup_person(staff_id, name)
        self.tax_num = tax_num

class Academic(Staff):
    def setup_academic(self, staff_id, name, tax_num, publications):
        self.setup_staff(staff_id, name, tax_num) # Inherits from Staff
        self.publications = publications

    def assign_grade(self, student_name, course_title, grade):
        print(f"\n=> GRADE ASSIGNED: Lecturer {self.name} gave {student_name} a {grade} in {course_title}.")

class Course:
    def setup_course(self, course_id, title, capacity):
        self.course_id = course_id
        self.title = title
        self.capacity = capacity
        self.students = []

def run_cli():
    # test data
    course1 = Course()
    course1.setup_course("MSE800", "Software Engineering", 2)
    
    student1 = Student()
    student1.setup_student("S101", "Ayush")
    
    lecturer1 = Academic()
    lecturer1.setup_academic("L001", "Dr. Smith", "TAX999", "Tech Journals")

    while True:
        print("\n--- College Management CLI ---")
        print("1. Enroll Student in Course")
        print("2. Assign Grade to Student")
        print("3. View Course Details")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            student1.enroll_course(course1)
        elif choice == "2":
            lecturer1.assign_grade(student1.name, course1.title, "A")
        elif choice == "3":
            print(f"\n--- {course1.title} Details ---")
            print(f"Capacity: {len(course1.students)} / {course1.capacity}")
            print(f"Enrolled Students: {', '.join(course1.students) if course1.students else 'None yet'}")
        elif choice == "4":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run 
run_cli()