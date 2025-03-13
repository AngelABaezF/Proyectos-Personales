//Ángel Alexander Báez Flores - A01425613
#include <iostream>
using namespace std;

class Nodo {
public:
    char value;
    Nodo* next;
    Nodo(char data) {
        value = data;
        next = nullptr;
    }
};

class Pila {
private:
    Nodo* top;
public:
    Pila() {
        top = nullptr;
    }
    void push(char data) {
        Nodo* nuevo = new Nodo(data);
        if (top == nullptr) {
            top = nuevo;
        } else {
            nuevo->next = top;
            top = nuevo;
        }
    }
    char pop() {
        if (top == nullptr)
            return -1;
        Nodo* borrado = top;
        top = top->next;
        char value = borrado->value;
        delete borrado;
        return value;
    }

    bool isEmpty() {
        return top == nullptr;
    }
};

class Solution {
public:
    bool isValid(string s) {
        Pila pila;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                pila.push(c);
            } else {
                if (pila.isEmpty()) return false;
                char top = pila.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return pila.isEmpty();
    }
};

int main() {
    Solution solution;
    
    string s1 = "()";
    string s2 = "()[]{}";
    string s3 = "(]";
    string s4 = "([])";
    
    cout << solution.isValid(s1) << endl;
    cout << solution.isValid(s2) << endl;
    cout << solution.isValid(s3) << endl;
    cout << solution.isValid(s4) << endl; 

    return 0;
}