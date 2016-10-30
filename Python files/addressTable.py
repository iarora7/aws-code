import psycopg2

print("Hello World")


conn = psycopg2.connect(database="test1", user="postgres", password="Welcome@123", host="54.67.5.124", port="5432")

print ("Opened database successfully")

cur = conn.cursor()
# cur.execute('''CREATE TABLE HOUSES
#        (ID SERIAL PRIMARY KEY     NOT NULL,
#        ADDRESS           TEXT    NOT NULL);''')
# print ("Table created successfully")

# cur.execute("INSERT INTO HOUSES (ADDRESS) \
#       VALUES ('California')");

# cur.execute("INSERT INTO HOUSES (ADDRESS) \
#       VALUES ('Texas')");

# cur.execute("INSERT INTO HOUSES (ADDRESS) \
#       VALUES ('Teddy')");

# cur.execute("INSERT INTO HOUSES (ADDRESS) \
#       VALUES ('Cal State')");

cur.execute("SELECT id, address  from HOUSES")
rows = cur.fetchall()
for row in rows:
   print("Id = ", row[0])
   print("Address = ", row[1], "\n")

print("Operation done successfully")


# cur.execute("Select * from Company")
# rows = cur.fetchall()

# for row in rows:
#     print row, "\n"

conn.commit()
conn.close()