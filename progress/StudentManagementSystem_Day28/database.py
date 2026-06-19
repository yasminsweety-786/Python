import sqlite3


def create_connection():

    connection = sqlite3.connect("students.db")

    return connection



def create_table():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)


    connection.commit()

    connection.close()


create_table()