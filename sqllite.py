import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_info = '''
    CREATE TABLE STUDENTS (
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25)
    )
'''
# cursor.execute(table_info)

cursor.execute("INSERT INTO STUDENTS VALUES('JOHN','10','A')")
cursor.execute("INSERT INTO STUDENTS VALUES('JANE','10','B')")
cursor.execute("INSERT INTO STUDENTS VALUES('JACK','11','A')")
cursor.execute("INSERT INTO STUDENTS VALUES('JILL','11','B')")

print('The data inserted are : ')

data = cursor.execute("SELECT * FROM STUDENTS")
for i in data:
    print(i)


connection.commit()
connection.close()