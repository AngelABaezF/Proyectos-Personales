#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

struct Auto {
    string marca;
    string modelo;
    int anio;
    float precio;
    int stock;
};

vector<Auto> inventario;
float ganancias = 0.0;

void registrarAuto(){
    int cantidad;
    cout << "¿Cuantos autos quieres registrar?: ";
    cin >> cantidad;

    for (int i = 0; i < cantidad; i++){
        Auto nuevoAuto;
        cout << "\nIngresa la marca del auto: ";
        cin >> nuevoAuto.marca;
        cout << "Ingresa el modelo del auto: ";
        cin >> nuevoAuto.modelo;
        cout << "Ingresa el año del auto: ";
        cin >> nuevoAuto.anio;
        cout << "Ingresa el precio del auto: ";
        cin >> nuevoAuto.precio;
        cout << "Ingresa la cantidad en stock: ";
        cin >> nuevoAuto.stock;

        inventario.push_back(nuevoAuto);
        cout << "Auto agregado correctamente.\n";
    }
}

void mostrarInventario(){
    cout << "\n--- INVENTARIO DE AUTOS ---\n";
    if (inventario.empty()){
        cout << "No hay autos en el inventario.\n";
    } else {
        for (size_t i = 0; i <inventario.size(); i++){
            cout << i+1 << ". " << inventario[i].marca << " " << inventario[i].modelo
            << " (" << inventario[i].anio << ") - Precio $" << inventario[i].precio
            << " - Stock: " << inventario[i].stock << " unidades\n";
        }
    }
}

void menu(){
    int opcion;
    do {
        cout << "\n--- SISTEMA DE CONCESIONARIA ---\n";
        cout << "1. Registrar autos\n";
        cout << "2. Mostrar inventario\n";
        cout << "3. Veneder auto\n";
        cout << "4. Mostrar un resumen\n";
        cout << "5. Salir\n";
        cout << "Seleccione una opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                registrarAuto();
                break;
            case 2:
                mostrarInventario();
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
            cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Opcion no valida.\n";
        }
    } while (opcion != 5);
}

int main(){
    try {
        menu();
    } catch (const exception &e) {
        cout << "Se ha producido un error: " << e.what() << "\n";
    }
    return 0;
}