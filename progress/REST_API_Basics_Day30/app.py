from flask import Flask, jsonify, request

app = Flask(__name__)


students = [
    {
        "id": 1,
        "name": "Yasmin",
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Ali",
        "course": "Flask"
    }
]


# Home API
@app.route("/")
def home():
    return "REST API Day 30"


# GET all students
@app.route("/students", methods=["GET"])
def get_students():

    return jsonify(students)


# GET single student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({
        "message": "Student not found"
    })


# POST new student
@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    new_student = {
        "id": len(students)+1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student)


if __name__ == "__main__":
    app.run(debug=True)