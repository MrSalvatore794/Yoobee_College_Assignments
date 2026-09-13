from database import Database
from user import Customer, Admin
from car import Car

class AppUI:
    def __init__(self):
        self.db = Database()
        self.current_user = None

    def start_application(self):
        print("Welcome to the Car Rental System")
        while True:
            if not self.current_user:
                self.auth_menu()
            else:
                self.display_menu()

    def auth_menu(self):
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            user = input("Username: ")
            pwd = input("Password: ")
            user_data = next((u for u in self.db.records["users"] if u["username"] == user and u["password"] == pwd), None)
            if user_data:
                if user_data["role"] == "Admin":
                    self.current_user = Admin(user, pwd)
                else:
                    self.current_user = Customer(user, pwd)
                print(f"Logged in as {user_data['role']}.")
            else:
                print("Invalid credentials.")
        elif choice == '2':
            user = input("Username: ")
            pwd = input("Password: ")
            role = input("Role (Customer/Admin): ")

            # User registration and login functionality
            if not any(u["username"] == user for u in self.db.records["users"]):
                self.db.records["users"].append({"username": user, "password": pwd, "role": role})
                self.db.save_data()
                print("Registered successfully.")
            else:
                print("Username exists.")
        elif choice == '3':
            exit()

    def display_menu(self):
        if self.current_user.role == "Admin":
            print("\nAdmin Menu:\n1. Add Car\n2. Update Car\n3. Delete Car\n4. Manage Bookings\n5. Logout")
            choice = input("Select an option: ")
            if choice == '1':
                c = Car(input("ID: "), input("Make: "), input("Model: "), int(input("Year: ")), 
                        float(input("Mileage: ")), True, int(input("Min rent period: ")), int(input("Max rent period: ")))
                self.current_user.add_car(self.db, c)
            elif choice == '2':
                car_id = input("Car ID to update: ")
                mileage = float(input("New mileage: "))
                self.current_user.update_car(self.db, car_id, {"mileage": mileage})
            elif choice == '3':
                car_id = input("Car ID to delete: ")
                self.current_user.delete_car(self.db, car_id)
            elif choice == '4':
                print("Pending Bookings:", [b for b in self.db.records["bookings"] if b["status"] == "Pending"])
                b_id = input("Enter Booking ID to approve/reject: ")
                action = input("Approve? (y/n): ")
                self.current_user.approve_booking(self.db, b_id, action.lower() == 'y')
            elif choice == '5':
                self.current_user = None
        else:
            print("\nCustomer Menu:\n1. View Available Cars\n2. Book a Car\n3. Logout")
            choice = input("Select an option: ")
            if choice == '1':

                # Enables customers to view available cars and their details
                cars = [c for c in self.db.records["cars"] if c["available_now"]]
                for c in cars:
                    print(c)
            elif choice == '2':
                car_id = input("Enter Car ID to book: ")
                days = int(input("Enter rental duration (days): "))
                self.current_user.request_booking(self.db, car_id, days)
            elif choice == '3':
                self.current_user = None

if __name__ == "__main__":
    app = AppUI()
    app.start_application()