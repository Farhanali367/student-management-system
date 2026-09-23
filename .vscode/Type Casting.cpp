#include <iostream>
using namespace std;

int main() {
    int a = 10;
    double b = 3.5;

    double result = a + b;  // 'a' (int) is promoted to double

    cout << "Result = " << result << endl;  // 13.5
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int x = 5, y = 2;
    double div = (double)x / y;  // force int → double

    cout << "Division = " << div << endl;  // 2.5
    return 0;
}
