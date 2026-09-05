class person:
    def __init__(self, Id, Name):
        self.Id = Id
        self.Name = Name

    def display(self):
        print(f"Id: {self.Id}, Name: {self.Name}")