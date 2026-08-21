# main.py
from database import Database
from models import Customer, Currency, Transaction

if __name__ == '__main__':
    # setup db
    db = Database("exchange.db")
    db.setup()

    # Test objects
    c1 = Customer("Ayush Sharma", "ayush@email.com")
    c2 = Customer("John Doe", "john@email.com")
    
    curr1 = Currency("NZD", "New Zealand Dollar", 1.0)
    curr2 = Currency("USD", "US Dollar", 0.6)
    curr3 = Currency("INR", "Indian Rupee", 51.0)

    t1 = Transaction(1, "NZD", "INR", 150.0, "2026-08-21")
    t2 = Transaction(2, "USD", "NZD", 100.0, "2026-08-21")

    # save to database
    db.insert_customer(c1)
    db.insert_customer(c2)

    db.insert_currency(curr1)
    db.insert_currency(curr2)
    db.insert_currency(curr3)

    db.insert_transaction(t1)
    db.insert_transaction(t2)

    # print it out
    db.show_transactions()