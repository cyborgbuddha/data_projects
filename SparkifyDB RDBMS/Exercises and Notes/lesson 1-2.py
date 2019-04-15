Table Name: transactions2 
column 0: transaction Id
column 1: Customer Name
column 2: Cashier Id
column 3: Year

Table Name: albums_sold
column 0: Album Id
column 1: Transaction Id
column 3: Album Name

Table Name: employees
column 0: Employee Id
column 1: Employee Name

Table Name: sales
column 0: Transaction Id
column 1: Amount Spent

-------------------------------

# TO-DO: Add all Create statements for all tables
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions2 (transaction_id int, customer_name varchar, cashier_id int, year int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (album_id int, transaction_id int, album_name varchar)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS employees (employee_id int, employee_name varchar)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS sales (transaction_id int, amount_spent int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

      
# TO-DO: Insert data into the tables    
    
    
    
try: 
    cur.execute("INSERT INTO transactions2  (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, "Amanda", 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions2  (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, "Toby", 1, 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions2  (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, "Max", 2, 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (1, 1, "Rubber Soul"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (2, 1, "Let It Be"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (3, 2, "My Generation"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (4, 3, "Meet the Beatles"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (5, 3, "Help!"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)", \
                 (1, "Sam"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)", \
                 (2, "Bob"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent) \
                 VALUES (%s, %s)", \
                 (1, 40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)    
    
try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent) \
                 VALUES (%s, %s)", \
                 (2, 19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 

try: 
    cur.execute("INSERT INTO sales (transaction_id, amount_spent) \
                 VALUES (%s, %s)", \
                 (3, 45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e) 

---------------------------------------

print("Table: transactions\n")
try: 
    cur.execute("SELECT * FROM transactions2;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: albums_sold\n")
try: 
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

print("\nTable: employees\n")
try: 
    cur.execute("SELECT * FROM employees;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
    
print("\nTable: sales\n")
try: 
    cur.execute("SELECT * FROM sales;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


--------------------------------


Let's say you need to do a query that gives:
transaction_id
 customer_name
 cashier name
 year 
 albums sold
 amount sold

 Table Name: transactions2 
column 0: transaction Id
column 1: Customer Name
column 2: Cashier Id
column 3: Year

Table Name: albums_sold
column 0: Album Id
column 1: Transaction Id
column 3: Album Name

Table Name: employees
column 0: Employee Id
column 1: Employee Name

Table Name: sales
column 0: Transaction Id
column 1: Amount Spent

TO-DO: Complete the statement below to perform a 3 way JOIN on the 4 tables you have created.
try: 
    cur.execute("SELECT transaction_id, customer_name, cashier_name, year, albums_sold, amount_sold")
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
try: 
    cur.execute("SELECT * \
    			FROM transactions2 \
    			JOIN albums_sold ON transactions2.transaction_id = albums_sold.transaction_id\
    			JOIN employees ON transactions2.cashier_id = employees.employee_id\
    			JOIN sales on transactions2.transaction_id = sales.transaction_id")
    				
    				
    				
    				
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)
​
row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


-----------------------------------------

# TO-DO: Create all tables
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id int, customer_name varchar, cashier_id int, year int, amount_spent int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)



#Insert data into all tables 
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1,"Amanda",1,2000,40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2,"Toby",1,2000,19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (3,"Max",2,2018,45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)   


----------------------------------

# Create the tables

try: 
    cur.execute("CREATE TABLE IF NOT EXISTS cashier_sales (transaction_id int, cashier_id int, cashier_name varchar, amount_spent int)")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)


#Insert into all tables 
    
try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_id, cashier_name, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (1,1,"Sam",40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_id, cashier_name, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (2,1,'Sam',19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO cashier_sales (transaction_id, cashier_id, cashier_name, amount_spent) \
                 VALUES (%s, %s, %s, %s)", \
                 (3,2,"Bob",45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)