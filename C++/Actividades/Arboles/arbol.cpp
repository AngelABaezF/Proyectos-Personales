#include <iostream>
using namespace std;

class Nodo{
public:
    int value;
    Nodo *izq;
    Nodo *der;
    Nodo(int data){
        value = data;
        izq = nullptr;
        der = nullptr;
    }

    bool esHoja(){
        return der==nullptr && izq==nullptr;
    }

    bool unHijo(){
        if ((der==nullptr && izq !=nullptr) || (der!=nullptr && izq ==nullptr)) return true;
        else return false;
    }

    Nodo *unicoHijo(){
        if (der==nullptr) return izq;
        else return der;
    }
};

class Arbol{
private:
    Nodo *root;
public: 
    enum Rec {IN, PRE, POST};
    Arbol(){
        root = nullptr;
    }

    void insertar(Nodo* nodo, int data){
        if (data > nodo->value){
            if (nodo->der == nullptr)
                nodo->der = new Nodo(data);
            else
                insertar(nodo->der, data);
        }else if (data < nodo->value){
            if (nodo->izq == nullptr)
                nodo->izq = new Nodo(data);
            else
                insertar(nodo->izq, data);
        }
    }

    void insertar(int data){
        if (root==nullptr){
            root = new Nodo(data);
            return;
        }
        insertar(root, data);
    }

    void mostrarIn(Nodo* nodo, int spc){
        if (nodo->der != nullptr) mostrarIn(nodo->der,spc+4);
        cout << string(spc,' ') << nodo->value << endl;
        if (nodo->izq != nullptr) mostrarIn(nodo->izq, spc+4);
    }

    void mostrarPre(Nodo* nodo, int spc){
        cout << string(spc,' ') << nodo->value << endl;
        if (nodo->der != nullptr) mostrarPre(nodo->der,spc+4);        
        if (nodo->izq != nullptr) mostrarPre(nodo->izq, spc+4);
    }

    void mostrarPost(Nodo* nodo, int spc){        
        if (nodo->der != nullptr) mostrarPost(nodo->der,spc+4);        
        if (nodo->izq != nullptr) mostrarPost(nodo->izq, spc+4);
        cout << string(spc,' ') << nodo->value << endl;
    }

    void mostrar(Rec rec){
        if (root == nullptr){
            cout << "Árbol vacío" << endl;
            return;
        }
        cout << "- Árbol -" << endl;
        if (rec == Arbol::IN) mostrarIn(root,0);
        if (rec == Arbol::PRE) mostrarPre(root,0);
        if (rec == Arbol::POST) mostrarPost(root,0);
    }

    void reemplazar(Nodo* nodo){
        Nodo* actual = nodo->izq;
        while (actual->der!=nullptr && actual->der->der!=nullptr){
            actual = actual->der;
        }
        nodo->value = actual->der->value;
        Nodo* borrar = actual->der;
        actual->der = actual->der->izq;
        delete actual;
    }

    Nodo* borrar(Nodo* nodo, int data){
        if (nodo == nullptr) return nullptr;
        if (nodo ->value == data){
            if (nodo->esHoja()){
                delete nodo;
                return nullptr;
            } else if (nodo->unHijo()){
                Nodo* retorno  = nodo->unicoHijo();
                delete nodo;
                return retorno;
            } else reemplazar(nodo);
        }else if(data>nodo->value)
            nodo->der = borrar(nodo->der, data);
        else
            nodo->izq = borrar(nodo->izq, data);
        return nodo;
    }

    void borrar(int data){
        root = borrar(root, data);
    }
};

int main(){
    Arbol arbol;
/*
    arbol.insertar(500);
    arbol.insertar(350);
    arbol.insertar(700);
    arbol.insertar(600);
    arbol.insertar(800);
*/
    //arbol.mostrar(Arbol::PRE);
    //arbol.mostrar(Arbol::POST);

    arbol.borrar(700);

    arbol.insertar(200);
    arbol.insertar(250);
    arbol.insertar(225);
    arbol.insertar(275);
    arbol.insertar(400);

    arbol.mostrar(Arbol::IN);
    return 0;
}