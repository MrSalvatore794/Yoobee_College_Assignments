import uuid

class RentalBooking:
    def __init__(self, car_id, customer_username, duration_days, status="Pending"):
        self.booking_id = str(uuid.uuid4())[:8]
        self.car_id = car_id
        self.customer_username = customer_username
        self.duration_days = duration_days
        self.total_fee = 0.0
        self.status = status
        
    def calculate_fees(self, daily_rate=50.0):
        # Calculates the rental fees based on the rental duration and a base rate
        self.total_fee = self.duration_days * daily_rate
        return self.total_fee

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "car_id": self.car_id,
            "customer_username": self.customer_username,
            "duration_days": self.duration_days,
            "total_fee": self.total_fee,
            "status": self.status
        }