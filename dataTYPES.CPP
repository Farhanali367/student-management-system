#include <iostream>
using namespace std;

int main() {
    // Integer types
    int a = 10;            // 4 bytes
    short b = 20;          // 2 bytes
    long c = 100000L;      // 4 or 8 bytes (platform dependent)
    long long d = 10000000000LL; // 8 bytes

    // Floating point types
    float e = 3.14f;       // 4 bytes
    double f = 3.14159265; // 8 bytes
    long double g = 3.141592653589793L; // 12 or 16 bytes

    // Character and boolean
    char h = 'X';          // 1 byte
    bool i = true;         // 1 byte (true/false)

    // String (from <string>)
    string j = "Hello, C++";

    // Printing values
    cout << "int: " << a << endl;
    cout << "short: " << b << endl;
    cout << "long: " << c << endl;
    cout << "long long: " << d << endl;
    cout << "float: " << e << endl;
    cout << "double: " << f << endl;
    cout << "long double: " << g << endl;
    cout << "char: " << h << endl;
    cout << "bool: " << i << endl;
    cout << "string: " << j << endl;

    return 0;
}
