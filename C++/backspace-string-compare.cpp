//Angel Alexander Baez Flores - A01425613
class Nodo {
public:
    char value;
    Nodo *next;
    Nodo(char data) {
        value = data;
        next = nullptr;
    }
};

class Pila {
private:
    Nodo *top;
public:
    Pila() {
        top = nullptr;
    }
    void push(char data) {
        Nodo *nuevo = new Nodo(data);
        if (top == nullptr) {
            top = nuevo;
        } else {
            nuevo->next = top;
            top = nuevo;
        }
    }
    char pop() {
        if (top == nullptr) {
            return -1;
        }
        Nodo *borrado = top;
        top = top->next;
        char value = borrado->value;
        delete borrado;
        return value;
    }
    bool isEmpty() {
        return top == nullptr;
    }
    void mostrar() {
        Nodo *actual = top;
        while (actual != nullptr) {
            cout << actual->value << " ";
            actual = actual->next;
        }
        cout << endl;
    }
    void limpiar() {
        while (!isEmpty()) {
            pop();
        }
    }
};

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return procesarCadena(s) == procesarCadena(t);
    }
private:
    string procesarCadena(const string& str) {
        Pila pila;
        for (char c : str) {
            if (c != '#') {
                pila.push(c);
            } else if (!pila.isEmpty()) {
                pila.pop();
            }
        }
        string resultado;
        while (!pila.isEmpty()) {
            resultado += pila.pop();
        }
        reverse(resultado.begin(), resultado.end());
        return resultado;
    }
};