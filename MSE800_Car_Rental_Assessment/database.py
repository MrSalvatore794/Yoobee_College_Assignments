import json
import os

class Database:
    def __init__(self):
        self.filename = "database.json"
        self.records = {
            "users": [],
            "cars": [],
            "bookings": []
        }
        self.load_data()

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.records, f, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.records = json.load(f)