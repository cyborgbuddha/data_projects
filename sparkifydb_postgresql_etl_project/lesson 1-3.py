try: 
    cur.execute("CREATE TABLE IF NOT EXISTS customer_transactions (customer_id int, store_id int, spent numeric);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
#Insert into all tables 
try: 
    cur.execute("INSERT INTO customer_transactions (customer_id, store_id, spent) VALUES (%s,%s,%s)", (1,1,20.50))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
    cur.execute("INSERT INTO customer_transactions (customer_id, store_id, spent) VALUES (%s,%s,%s)", (2,1,35.21))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


-----------------------------------

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS customer (customer_id int, name varchar, rewards boolean);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO customer (customer_id, name, rewards) VALUES (%s,%s,%s);",(1,"Amanda",True))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO customer (customer_id, name, rewards) VALUES (%s,%s,%s);",(2,"Toby",False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS store (store_id int, state varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO store (store_id, state) VALUES (%s,%s);",(1,"CA"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
    cur.execute("INSERT INTO store (store_id, state) VALUES (%s,%s);",(2,"WA"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS items_purchased (customer_id int, item_number int, item_name varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO items_purchased (customer_id, item_number, item_name) VALUES (%s,%s,%s);",(1,1,"Rubber Soul"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO items_purchased (customer_id, item_number, item_name) VALUES (%s,%s,%s);",(2,3,"Let it Be"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

--------------------------
try: 
    cur.execute("SELECT * FROM customer_transactions\
                 JOIN customer ON customer_transactions.customer_id = customer.customer_id\
                 JOIN items_purchased ON customer_transactions.customer_id = items_purchased.customer_id\
                 JOIN store ON customer_transactions.store_id = store.store_id")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()