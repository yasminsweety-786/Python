from database import create_connection


def add_student(name, age, course):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "INSERT INTO students(name,age,course) VALUES(?,?,?)",
        (name, age, course)
    )


    connection.commit()

    connection.close()


def view_students():

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT * FROM students"
    )


    data = cursor.fetchall()


    for student in data:
        print(student)


    connection.close()



def delete_student(student_id):

    connection = create_connection()

    cursor = connection.cursor()


    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )


    connection.commit()

    connection.close()