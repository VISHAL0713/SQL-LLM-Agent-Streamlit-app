import sqlite3

#### connect to sqllit3
connection = sqlite3.connect("student.db")

#### create a cursor object
cursor = connection.cursor()

#### create th table
table_info = """

CREATE table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

### insert some records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Devops','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','Data Science','B',70)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','Devops','A',35)''')
cursor.execute('''Insert Into STUDENT values('Vishal','Automation','A',30)''')
cursor.execute('''Insert Into STUDENT values('Vicky','Data Science','A',25)''')
cursor.execute('''Insert Into STUDENT values('Rahul','Automation','B',60)''')
cursor.execute('''Insert Into STUDENT values('Brian','Data Science','B',73)''')

### display all the records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
    
### close the connection
connection.commit()
connection.close()