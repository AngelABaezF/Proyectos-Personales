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
class Fila{
private:
    Nodo *front;
    Nodo *back;
public:
    Fila(){
        front  = nullptr;
        back = nullptr;
    }
    void enqueue(int data){
        Nodo *nuevo = new Nodo(data);
        if (front==nullptr){
            front = nuevo;
            back = nuevo;
        }else{
            back -> next = nuevo;
            back = nuevo;
        }
    }
    int dequeue(){
		if (front == nullptr)
			return -1;
		Nodo *borrado = front;
		front = front->next;
        if (front==nullptr) back = nullptr;
        int value = borrado->value;
		delete borrado;
		return value;
	}
    void mostrar()
	{
		Nodo *actual = front;
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
	Fila *fila = new Fila();
	fila->enqueue(5);
    fila->dequeue();
    fila->mostrar();
    fila->enqueue(3);
    fila->enqueue(8);
    fila->mostrar();
    int value = fila->dequeue();
    if (value==-1){
        cout << "Error al extraer" <<endl;
    }else{
        cout << "dequeue " << value << endl;
    }
    fila->mostrar();
    fila->enqueue(9);
    fila->mostrar();

    return 0;
};