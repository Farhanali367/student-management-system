from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_marksheet():
    # Create a canvas
    c = canvas.Canvas("marksheet.pdf", pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height - 50, "Senior Secondary Examination - Marksheet")

    # Student Info (example)
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Name: John Doe")
    c.drawString(100, height - 120, "Roll No: 25301")
    c.drawString(100, height - 140, "Class: XII")
    c.drawString(100, height - 160, "Session: 2024-25")

    # Table headers
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    subjects = ["Subject", "Marks", "Grade"]
    x_positions = [100, 300, 400]
    for i, header in enumerate(subjects):
        c.drawString(x_positions[i], height - 200, header)

    # Marks data
    data = [
        ("English", 78),
        ("Physics", 70),
        ("Chemistry", 72),
        ("Mathematics", 69),
        ("Computer Science", 73),
    ]

    def get_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B+"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "D"

    y = height - 230
    total = 0
    for subject, marks in data:
        grade = get_grade(marks)
        c.setFont("Helvetica", 12)
        c.drawString(100, y, subject)
        c.drawString(300, y, str(marks))
        c.drawString(400, y, grade)
        total += marks
        y -= 25

    # Total & Result
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 20, f"Total Marks: {total}/500")
    percentage = total / 5
    c.drawString(100, y - 40, f"Percentage: {percentage:.2f}%")
    result = "PASS" if percentage >= 33 else "FAIL"
    c.drawString(100, y - 60, f"Result: {result}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawRightString(width - 100, 50, "Authorized Signatory")

    # Save PDF
    c.save()

create_marksheet()
