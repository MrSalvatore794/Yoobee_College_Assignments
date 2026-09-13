class Car:
    def __init__(self, ID, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        # Database of available cars
        self.ID = ID 
        self.make = make 
        self.model = model 
        self.year = year 
        self.mileage = mileage 
        self.available_now = available_now 
        self.min_rent_period = min_rent_period 
        self.max_rent_period = max_rent_period 
    
    def to_dict(self):
        return {
            "ID": self.ID,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "available_now": self.available_now,
            "min_rent_period": self.min_rent_period,
            "max_rent_period": self.max_rent_period
        }