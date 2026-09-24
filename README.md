# 🎓 Student Management System

A full-stack **Student Management System** built with a modern web dashboard and REST API backend. The project allows users to manage student records, marks, and results through a simple and responsive interface.

## 🌐 Live Demo

**Live Website:**  
https://farhanali367.github.io/student-management-system/

## ✨ Features

- ➕ Add new students
- 📋 View all student records
- 🔍 Search students by ID, name, or course
- ✏️ Edit student information
- 🗑️ Delete student records
- 📊 View student marks
- ✅ Automatic PASS / FAIL result
- 📈 Dashboard statistics
- 🔗 REST API integration
- 🌍 Live frontend and backend deployment

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Programming / Tools
- C++
- Git
- GitHub
- GitHub Pages
- Render
- VS Code

## 📁 Project Structure

```text
student-management-system/
│
├── backened/
│   ├── main.py
│   ├── database.py
│   ├── requirements.txt
│   ├── index.html
│   └── students.db
│
├── src/
│   └── main.cpp
│
├── index.html
├── README.md
└── .gitignore
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Get all students |
| POST | `/students` | Add a new student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |

## 🚀 Run the Backend Locally

### 1. Clone the repository

```bash
git clone https://github.com/Farhanali367/student-management-system.git
cd student-management-system
```

### 2. Open the backend folder

```bash
cd backened
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI server

```bash
python -m uvicorn main:app --reload
```

### 6. Open API documentation

```text
http://127.0.0.1:8000/docs
```

## 🌍 Deployment

### Frontend
Deployed on **GitHub Pages**

### Backend
Deployed on **Render**

The frontend communicates with the live FastAPI backend through REST API requests.

## 📊 Project Highlights

- Full-stack web application
- CRUD operations for student records
- REST API architecture
- SQLite database
- Search functionality
- Student result calculation
- GitHub version control
- Cloud deployment
- Responsive dashboard interface

## 🎯 Learning Outcomes

Through this project, I practiced:

- C++ programming
- Python development
- FastAPI
- REST APIs
- SQLAlchemy
- SQLite database management
- HTML, CSS and JavaScript
- CRUD operations
- Git and GitHub
- Web deployment

## 👨‍💻 Author

**Mohd Farhan**  
BTech CSE Student

**GitHub:**  
https://github.com/Farhanali367

---

⭐ **If you find this project useful, consider giving it a star!**
