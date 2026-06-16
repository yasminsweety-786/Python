import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students(name, age) VALUES(?, ?)",
    ("Ali", 21)
)

connection.commit()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()