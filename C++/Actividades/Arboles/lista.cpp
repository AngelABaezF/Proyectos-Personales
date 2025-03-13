#include <iostream>

using namespace std;

class NodoLista
{
public:
    int value;
    NodoLista *next;
    NodoLista(int data)
    {
        value = data;
        next = nullptr;
    };
};

class Lista
{
private:
    NodoLista *primero;

public:
    Lista()
    {
        primero = nullptr;
    }

    void insertarPrimero(int data)
    {
        NodoLista *nuevo = new NodoLista(data);
        if (primero == nullptr)
            primero = nuevo;
        else
        {
            nuevo->next = primero;
            primero = nuevo;
        }
    }

    void mostrar()
    {
        NodoLista *actual = primero;
        while (actual != nullptr)
        {
            cout << actual->value << "  ";
            actual = actual->next;
        }
    }
};

int main()
{
    Lista *lista = new Lista();
    lista->insertarPrimero(13);
    lista->insertarPrimero(8);
    lista->insertarPrimero(3);
    lista->insertarPrimero(1);
    lista->mostrar();
}