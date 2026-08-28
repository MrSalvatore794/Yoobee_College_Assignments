# database.py
import sqlite3

class Database:
    def __init__(self, db_name="exchange.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def setup(self):
        
        # dropping tables
        self.cursor.executescript('''
            DROP TABLE IF EXISTS Transactions;
            DROP TABLE IF EXISTS Customers;
            DROP TABLE IF EXISTS Currencies;
        ''')
        
        # making the tables
        self.cursor.executescript('''
            CREATE TABLE Customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            );

            CREATE TABLE Currencies (
                code TEXT PRIMARY KEY,
                name TEXT,
                rate REAL
            );

            CREATE TABLE Transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                from_currency TEXT,
                to_currency TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
                FOREIGN KEY(from_currency) REFERENCES Currencies(code),
                FOREIGN KEY(to_currency) REFERENCES Currencies(code)
            );
        ''')
        self.conn.commit()

    def insert_customer(self, cust):
        self.cursor.execute("INSERT INTO Customers (name, email) VALUES (?, ?)", 
                            (cust.name, cust.email))
        self.conn.commit()

    def insert_currency(self, curr):
        self.cursor.execute("INSERT INTO Currencies (code, name, rate) VALUES (?, ?, ?)", 
                            (curr.code, curr.name, curr.rate))
        self.conn.commit()

    def insert_transaction(self, trans):
        self.cursor.execute('''
            INSERT INTO Transactions (customer_id, from_currency, to_currency, amount, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (trans.customer_id, trans.from_currency, trans.to_currency, trans.amount, trans.date))
        self.conn.commit()

    def show_transactions(self):
        # joining the tables
        self.cursor.execute('''
            SELECT Customers.name, Transactions.amount, Transactions.from_currency, Transactions.to_currency, Transactions.date
            FROM Transactions
            JOIN Customers ON Transactions.customer_id = Customers.customer_id
        ''')
        print("--- Exchange Transactions ---")
        for row in self.cursor.fetchall():
            print(f"Customer: {row[0]} | Exchanged {row[1]} {row[2]} to {row[3]} on {row[4]}")