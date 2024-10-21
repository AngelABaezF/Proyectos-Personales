// Angel Alexander Baez Flores - A01425613
class Nodo {
public:
    int value;
    Nodo* next;
    Nodo(int data) {
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

    void push(int data) {
        Nodo* nuevo = new Nodo(data);
        if (top == nullptr) {
            top = nuevo;
        } else {
            nuevo->next = top;
            top = nuevo;
        }
    }

    int pop() {
        if (top == nullptr)
            return -1;
        Nodo* borrado = top;
        top = top->next;
        int value = borrado->value;
        delete borrado;
        return value;
    }

    int peek() {
        if (top == nullptr)
            return -1;
        return top->value;
    }

    bool isEmpty() {
        return top == nullptr;
    }
};

class Solution {
public:
    int longestValidParentheses(string s) {
        Pila pila;
        pila.push(-1);
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                pila.push(i);
            } else {
                pila.pop();

                if (pila.isEmpty()) {
                    pila.push(i);
                } else {
                    int currentLength = i - pila.peek();
                    maxLength = max(maxLength, currentLength);
                }
            }
        }
        return maxLength;
    }
};