#include <iostream>
using namespace std;
class Nodo{
public:
	int value;
	Nodo *next;
	Nodo(int data){
		value = data;
		next = nullptr;
	}
};
class Pila{
private:
    Nodo *top;
public:
    Pila(){
        top  = nullptr;
    }
    void push(int data){
        Nodo *nuevo = new Nodo(data);
        if (top==nullptr) top = nuevo;
        else{
            nuevo -> next = top;
            top = nuevo;
        }
    }
    int pop(){
		if (top == nullptr)
			return -1;
		Nodo *borrado = top;
		top = top->next;
        int value = borrado->value;
		delete borrado;
		return value;
	}
    void mostrar()
	{
		Nodo *actual = top;
		while (actual != nullptr)
		{
			cout << actual->value << " ";
			actual = actual->next;
		}
		cout << endl;
	}
};
int main()
{
	Pila *pila = new Pila();
	pila->push(5);
    pila->push(3);
    pila->push(8);
    pila->mostrar();
    int value = pila->pop();
    if (value==-1){
        cout << "Error al extraer" <<endl;
    }else{
        cout << "pop " << value << endl;
    }
    pila->mostrar();
    pila->push(9);
    pila->mostrar();

    return 0;
};