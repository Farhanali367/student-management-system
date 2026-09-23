#include <iostream>
#include <typeinfo> // for typeid
using namespace std;

int main() {
    int a = 42;
    double b = 3.14;
    char c = 'A';
    bool d = true;
    string e = "Hello";

    cout << "Type of a: " << typeid(a).name() << endl;
    cout << "Type of b: " << typeid(b).name() << endl;
    cout << "Type of c: " << typeid(c).name() << endl;
    cout << "Type of d: " << typeid(d).name() << endl;
    cout << "Type of e: " << typeid(e).name() << endl;

    return 0;
}
