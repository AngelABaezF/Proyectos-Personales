#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

bool isSymbol(const string &str) {
    for (char ch : str) {
        if (isdigit(ch)) {
            return false;
        }
    }
    return true;
}

bool list_of_symbols(const vector<string> &lst) {
    for (const string &item : lst) {
        if (!isSymbol(item)) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<string> list1 = {};
    vector<string> list2 = {"a", "b", "c", "d", "e"};
    vector<string> list3 = {"a", "b", "c", "d", "42", "e"};

    cout << boolalpha;
    cout << list_of_symbols(list1) << endl;
    cout << list_of_symbols(list2) << endl;
    cout << list_of_symbols(list3) << endl;

    return 0;
}