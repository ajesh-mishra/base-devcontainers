from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError, validate

app = Flask(__name__)


def validate_length(n: int):
    if len(str(n)) != 10:
        raise ValidationError("Phone number should be have 10 digits.")
    
class StudentSchema(Schema):
    name = fields.String(required=True)
    phone = fields.Integer(required=True, validate=validate_length)

all_students: list[dict[str, str]] = [
    {"name": "student1", "phone": 7638309392},
    {"name": "student2", "phone": 7638309392},
]


@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/student", methods=["GET"])
def student():
    """
    curl http://localhost:5001/student
    """
    return jsonify(results=all_students), 200


@app.route("/student", methods=["POST"])
def add_student():
    """
    curl -X POST \
        -H "Content-Type: application/json" \
        -d '{"name":"student3","phone":7249272022}' \
        http://localhost:5001/student
    """
    data: dict[str, str] = request.json

    try:
        student: dict[str, str] = StudentSchema().load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    all_students.append(student)
    return f"{student["name"]} is added!", 201


@app.route("/student/<string:student_name>", methods=["PUT"])
def update_student(student_name):
    """
    curl -X PUT \
        -H "Content-Type: application/json" \
        -d '{"name":"student2","phone":9999999999}' \
        http://localhost:5001/student/student2
    """
    data: dict[str, str] = request.json

    try:
        student: dict[str, str] = StudentSchema().load(data)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    index: int = [index for index, student in enumerate(all_students) if student["name"] == student_name]

    if index:
        all_students[index[0]] = student
        return f"{student_name} updated successfully!", 202
    
    return f"{student_name} not found!", 404


@app.route("/student", methods=["DELETE"])
def delete_student():
    """
    curl -X DELETE \
        -H "Content-Type: application/json" \
        -d '{"student_name":"student3"}' \
        http://localhost:5001/student
    """
    student_name: str = request.json["student_name"]
    index: int = [index for index, student in enumerate(all_students) if student["name"] == student_name]

    if index:
        all_students.pop(index[0])
        return f"{student_name} is removed!", 204

    return f"{student_name} not found!", 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
