from studentOperations import *


while True:


    print("\nStudent Management System")

    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        name = input("Name: ")

        age = int(input("Age: "))

        course = input("Course: ")


        add_student(
            name,
            age,
            course
        )


        print("Student Added")


    elif choice == "2":

        view_students()


    elif choice == "3":

        id = int(input("Student ID: "))

        delete_student(id)


        print("Deleted")


    elif choice == "4":

        break


    else:

        print("Invalid Choice")