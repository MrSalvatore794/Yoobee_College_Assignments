class Pizza:
    def cooking(self):
        print("Preparing Pizza")

class Burger:
    def cooking(self):
        print("Preparing Burger")

class Pasta:
    def cooking(self):
        print("Preparing Pasta")

class PizzaClub:
    @staticmethod
    def Select_Food(Menu):
        if Menu=="Pizza":
            return Pizza()
        elif Menu=="Burger":
            return Burger()
        elif Menu=="Pasta":
            return Pasta()
        else:
            raise ValueError("Not available")

Menu=PizzaClub.Select_Food("Pizza")
Menu.cooking()
