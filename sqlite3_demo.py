import sqlite3 as sql

con = sql.connect('sqlite3_demo')
cur = con.cursor()

# drop table if exist
cur.execute('DROP table IF EXISTS stocks')

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
values = [('2006-01-05','BUY','RHAT',100,35.14),
            ('2021-01-05','SELL','QLYS',50,120)]
sql = '''INSERT INTO stocks (date, trans, symbol, qty, price) 
            VALUES (?,?,?,?,?)'''
cur.executemany(sql,values)

# get the data
data = cur.execute('SELECT * FROM stocks ORDER BY price')

# print table columns
for col in data.description:
    print(col[0])

# print table values
for row in data.fetchall():
    print(row)


a = [1,6,2,7,3,8,4,9,5]
print(a)

a.sort()
print(a)

a.reverse()
print(a)