#include <iostream>
using namespace std;

int main() {
    int a = 5;

    cout << "Initial value of a = " << a << endl;

    // Pre-increment
    cout << "++a = " << ++a << " (a becomes 6, then printed)" << endl;

    // Post-increment
    cout << "a++ = " << a++ << " (print 6 first, then a becomes 7)" << endl;
    cout << "Now a = " << a << endl;

    // Pre-decrement
    cout << "--a = " << --a << " (a becomes 6, then printed)" << endl;

    // Post-decrement
    cout << "a-- = " << a-- << " (print 6 first, then a becomes 5)" << endl;
    cout << "Now a = " << a << endl;

    return 0;
}
