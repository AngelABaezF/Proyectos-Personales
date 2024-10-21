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
	}
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
	void insertarInicio(int data)
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
	void insertarFinal(int data)
	{
		NodoLista *nuevo = new NodoLista(data);
		if (primero == nullptr)
		{
			primero = nuevo;
		}
		else
		{
			NodoLista *actual = primero;
			while (actual->next != nullptr)
				actual = actual->next;
			actual->next = nuevo;
		}
	}
	bool insertarDespues(int ref, int data)
	{
		if (primero == nullptr)
			return false;
		NodoLista *actual = primero;
		while (actual != nullptr && actual->value != ref)
		{
			actual = actual->next;
		}
		if (actual == nullptr)
			return false;
		NodoLista *nuevo = new NodoLista(data);
		nuevo->next = actual->next;
		actual->next = nuevo;
		return true;
	}
	bool insertarAntes(int ref, int data)
	{
		if (primero == nullptr)
			return false;
		if (primero->value == ref)
		{
			NodoLista *nuevo = new NodoLista(data);
			nuevo->next = primero;
			primero = nuevo;
			return true;
		}
		NodoLista *actual = primero;
		while (actual->next != nullptr && (actual->next)->value != ref)
		{
			actual = actual->next;
		}
		if (actual->next == nullptr)
			return false;
		NodoLista *nuevo = new NodoLista(data);
		nuevo->next = actual->next;
		actual->next = nuevo;
		return true;
	}
	bool eliminarPrimero()
	{
		if (primero == nullptr)
			return false;
		NodoLista *borrado = primero;
		primero = primero->next;
		delete borrado;
		return true;
	}
	bool eliminarUltimo()
	{
		if (primero == nullptr)
			return false;
		if (primero->next == nullptr)
		{
			delete primero;
			primero = nullptr;
			return true;
		}
		NodoLista *actual = primero;
		while ((actual->next)->next != nullptr)
		{
			actual = actual->next;
		}
		NodoLista *borrado = actual->next;
		actual->next = nullptr;
		delete borrado;
		return true;
	}
	bool eliminarElemento(int ref)
	{
		if (primero == nullptr)
			return false;
		if (primero->value == ref)
		{
			NodoLista *borrado = primero;
			primero = primero->next;
			delete borrado;
			return true;
		}
		NodoLista *actual = primero;
		while (actual->next != nullptr && (actual->next)->value != ref)
		{
			actual = actual->next;
		}
		if (actual->next == nullptr)
			return false;
		NodoLista *borrado = actual->next;
		actual->next = borrado->next;
		delete borrado;
		return true;
	}
	void mostrar()
	{
		NodoLista *actual = primero;
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
	Lista *lista = new Lista();
	lista->insertarInicio(13);
	lista->insertarInicio(9);
	lista->insertarInicio(3);
	lista->insertarFinal(77);
	lista->insertarFinal(123);
	lista->mostrar();
	if (!lista->insertarDespues(13, 10))
		cout << "Error en insertarDespues()" << endl;
	lista->mostrar();
	if (!lista->insertarAntes(3, 11))
		cout << "Error en insertarAntes()" << endl;
	if (!lista->insertarAntes(77, 81))
		cout << "Error en insertarAntes()" << endl;
	lista->mostrar();
	if (!lista->eliminarPrimero())
		cout << "Error en eliminarPrimero()" << endl;
	lista->mostrar();
	if (!lista->eliminarUltimo())
		cout << "Error en eliminarUltimo()" << endl;
	lista->mostrar();
	if (!lista->eliminarElemento(10))
		cout << "Error en eliminarElemento()" << endl;
	if (!lista->eliminarElemento(3))
		cout << "Error en eliminarElemento()" << endl;
	lista->mostrar();
	delete lista;
	return 0;
}