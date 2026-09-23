#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;

    cout << "a + b = " << (a + b) << endl;  // Addition
    cout << "a - b = " << (a - b) << endl;  // Subtraction
    cout << "a * b = " << (a * b) << endl;  // Multiplication
    cout << "a / b = " << (a / b) << endl;  // Division (integer division)
    cout << "a % b = " << (a % b) << endl;  // Modulus (remainder)

    // Increment & Decrement
    cout << "a++ = " << (a++) << endl;  // Post-increment (use then increase)
    cout << "Now a = " << a << endl;
    cout << "++b = " << (++b) << endl;  // Pre-increment (increase then use)

    return 0;
}
