#include <iostream>
#include <vector>
using namespace std;

struct Student {
    int id;
    string name;
    float marks;
};

vector<Student> students;

void addStudent() {
    Student s;

    cout << "Enter Student ID: ";
    cin >> s.id;

    cout << "Enter Student Name: ";
    cin >> s.name;

    cout << "Enter Marks: ";
    cin >> s.marks;

    students.push_back(s);

    cout << "\nStudent added successfully!\n";
}

void displayStudents() {
    if (students.empty()) {
        cout << "\nNo students found.\n";
        return;
    }

    cout << "\n--- Student List ---\n";

    for (const Student &s : students) {
        cout << "ID: " << s.id << endl;
        cout << "Name: " << s.name << endl;
        cout << "Marks: " << s.marks << endl;
        cout << "-------------------\n";
    }
}

void searchStudent() {
    int id;

    cout << "Enter Student ID to search: ";
    cin >> id;

    for (const Student &s : students) {
        if (s.id == id) {
            cout << "\nStudent Found!\n";
            cout << "ID: " << s.id << endl;
            cout << "Name: " << s.name << endl;
            cout << "Marks: " << s.marks << endl;
            return;
        }
    }

    cout << "\nStudent not found.\n";
}

int main() {
    int choice;

    do {
        cout << "\n===== Student Management System =====\n";
        cout << "1. Add Student\n";
        cout << "2. Display Students\n";
        cout << "3. Search Student\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";

        cin >> choice;

        switch (choice) {
            case 1:
                addStudent();
                break;

            case 2:
                displayStudents();
                break;

            case 3:
                searchStudent();
                break;

            case 4:
                cout << "Thank you!\n";
                break;

            default:
                cout << "Invalid choice!\n";
        }

    } while (choice != 4);

    return 0;
}