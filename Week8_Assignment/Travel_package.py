# ==========================================
# 1. CLIENT
# ==========================================
class Travel_Package:
    def __init__(self, Destination, Hotel, Transport, Mealplan, Activites, Insurance):
        self.Destination = Destination
        self.Hotel = Hotel
        self.Transport = Transport
        self.Mealplan = Mealplan
        self.Activites = Activites
        self.Insurance = Insurance

    def show_details(self):
        print("Destination:", self.Destination)
        print("Hotel:", self.Hotel)
        print("Transport:", self.Transport)
        print("Meal Plan:", self.Mealplan)

# ==========================================
# 2. BUILDER / CONCRETE BUILDER
# ==========================================
class Travel_Booking:
    def __init__(self):
        self.Destination = None
        self.Hotel = None
        self.Transport = None
        self.Mealplan = None
        self.Activities = None
        self.Insurance = None

    def set_Destination(self, Destination):
        self.Destination = Destination
        return self
    def set_Hotel(self, Hotel):
        self.Hotel = Hotel
        return self
    def set_Transport(self, Transport):
        self.Transport = Transport
        return self
    def set_Mealplan(self, Mealplan):
            self.Mealplan = Mealplan
            return self
    def set_Activites(self, Activites):
            self.TraActivitesnsport = Activites
            return self
    def set_Insurance(self, Insurance):
            self.Insurance = Insurance
            return self
    def build(self):
        return Travel_Package(
            self.Destination,
            self.Hotel,
            self.Transport,
            self.Mealplan,
            self.Activities,
            self.Insurance
        )

# ==========================================
# 3. DIRECTOR 
# ==========================================
class Travel_Booking_Director:
    def build_basic_package(self, builder):
        builder.set_Destination("Paris")
        builder.set_Hotel("Hotel ABC")
        builder.set_Transport("Flight XYZ")
        builder.set_Mealplan("Breakfast Included")
        builder.set_Activites("City Tour")
        builder.set_Insurance("Basic")
        return builder.build()

builder= Travel_Booking()
director = Travel_Booking_Director()
travel_package = director.build_basic_package(builder)
travel_package.show_details()
