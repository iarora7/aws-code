import psycopg2

# Test DB Connection

print("Hello World")


conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

print ("Opened database successfully")

cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print ("Table created successfully")

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
#
# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
#
# cur.execute("SELECT id, name, address, salary  from COMPANY")
# rows = cur.fetchall()
# for row in rows:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("ADDRESS = ", row[2])
#    print("SALARY = ", row[3], "\n")
#
# print("Operation done successfully")


cur.execute("Select * from Company")
rows = cur.fetchall()

for row in rows:
    print row, "\n"

conn.commit()
conn.close()
