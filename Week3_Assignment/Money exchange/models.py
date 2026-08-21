# models.py

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Currency:
    def __init__(self, code, name, rate):
        self.code = code
        self.name = name
        self.rate = rate

class Transaction:
    def __init__(self, customer_id, from_currency, to_currency, amount, date):
        self.customer_id = customer_id
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.date = date