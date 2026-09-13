from rental import RentalBooking
from car import Car

class User:
    def __init__(self, username, password, role):
        
        # Differentiates between customer and admin roles.
        self.username = username
        self.password = password
        self.role = role 

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Customer")

    def request_booking(self, db, car_id, duration_days):

        # Implementing a booking feature that allows customers to specify rental dates and select a car.
        car_data = next((c for c in db.records["cars"] if c["ID"] == car_id), None)
        if not car_data:
            print("Car not found.")
            return
        if not car_data["available_now"]:
            print("Car is not available.")
            return
        if duration_days < car_data["min_rent_period"] or duration_days > car_data["max_rent_period"]:
            print(f"Duration must be between {car_data['min_rent_period']} and {car_data['max_rent_period']} days.")
            return
        
        booking = RentalBooking(car_id, self.username, duration_days)
        booking.calculate_fees() 
        db.records["bookings"].append(booking.to_dict())
        db.save_data()
        print(f"Booking {booking.booking_id} requested successfully! Total Fee: ${booking.total_fee}")

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Admin")
        
    def add_car(self, db, car):

        # Allows admins to add car records.
        db.records["cars"].append(car.to_dict())
        db.save_data()
        print("Car added successfully.")

    def update_car(self, db, car_id, updates):

        # Allows admins to update car records.
        for c in db.records["cars"]:
            if c["ID"] == car_id:
                c.update(updates)
                db.save_data()
                print("Car updated successfully.")
                return
        print("Car not found.")

    def delete_car(self, db, car_id):

        # Allows admins to delete car records.
        db.records["cars"] = [c for c in db.records["cars"] if c["ID"] != car_id]
        db.save_data()
        print("Car deleted successfully.")

    def approve_booking(self, db, booking_id, approve=True):
        # Allows admins to manage rental bookings, including approving or rejecting.
        for b in db.records["bookings"]:
            if b["booking_id"] == booking_id and b["status"] == "Pending":
                b["status"] = "Approved" if approve else "Rejected"
                if approve:
                    for c in db.records["cars"]:
                        if c["ID"] == b["car_id"]:
                            c["available_now"] = False
                db.save_data()
                print(f"Booking {booking_id} {b['status']}.")
                return
        print("Pending booking not found.")