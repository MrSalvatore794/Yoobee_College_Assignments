# Money Exchange 

For this assignment, I made 3 tables for the database: Customers, Currencies, and Transactions. 

1. Customers table: This is needed to keep track of who is actually doing the exchange. I just put name, email, and a customer ID in here so we can identify them easily.

2. Currencies table: This one stores the currency codes (like NZD, USD, INR) and the exchange rates. It's much better to have a separate table for this because if a rate changes, I only have to update it in one spot instead of updating every single transaction.

3. Transactions table: This is the main one that bridges the other two. It records the actual exchange event (who did it, what currency to what currency, amount, and date). I used foreign keys to link to the customer and the currency codes. This keeps everything organized without repeating data everywhere.