import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students(name, age) VALUES(?, ?)",
    ("Yasmin", 20)
)

connection.commit()

print("Data Inserted")

connection.close()