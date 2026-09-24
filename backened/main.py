from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_connection, create_table

app = FastAPI(title="Student Management System API")

# Allow frontend to connect with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database table
create_table()


class Student(BaseModel):
    id: int
    name: str
    course: str
    email: str
    marks: float


# Home
@app.get("/")
def home():
    return {
        "message": "Student Management System API is running"
    }


# Get all students
@app.get("/students")
def get_students():
    connection = get_connection()

    students = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return [dict(student) for student in students]


# Add student
@app.post("/students")
def add_student(student: Student):
    connection = get_connection()

    existing_student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student.id,)
    ).fetchone()

    if existing_student:
        connection.close()
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    connection.execute(
        """
        INSERT INTO students
        (id, name, course, email, marks)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            student.id,
            student.name,
            student.course,
            student.email,
            student.marks
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Student added successfully",
        "student": student
    }


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    connection = get_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return dict(student)


# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    connection = get_connection()

    existing_student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if not existing_student:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.execute(
        """
        UPDATE students
        SET name = ?,
            course = ?,
            email = ?,
            marks = ?
        WHERE id = ?
        """,
        (
            student.name,
            student.course,
            student.email,
            student.marks,
            student_id
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Student updated successfully"
    }


# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()

    result = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()

    if result.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }