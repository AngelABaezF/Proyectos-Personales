#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

// Estructura para almacenar información de los productos
struct Producto {
    string nombre;
    float precio;
    int stock;
};

vector<Producto> inventario; // Lista de productos
float ganancias = 0.0;       // Variable para almacenar las ganancias

// Función para registrar productos en el inventario
void registrarProducto() {
    int cantidad;
    cout << "¿Cuántos productos quieres registrar?: ";
    cin >> cantidad;

    for (int i = 0; i < cantidad; i++) {
        Producto nuevoProducto;
        cout << "\nIngrese el nombre del producto: ";
        cin >> nuevoProducto.nombre;
        cout << "Ingrese el precio del producto: ";
        cin >> nuevoProducto.precio;
        cout << "Ingrese la cantidad en stock: ";
        cin >> nuevoProducto.stock;

        inventario.push_back(nuevoProducto);
        cout << "Producto agregado correctamente.\n";
    }
}

// Función para mostrar el inventario actual
void mostrarInventario() {
    cout << "\n--- INVENTARIO ACTUAL ---\n";
    if (inventario.empty()) {
        cout << "No hay productos en inventario.\n";
    } else {
        for (size_t i = 0; i < inventario.size(); i++) {
            cout << i + 1 << ". " << inventario[i].nombre
                 << " - Precio: $" << inventario[i].precio
                 << " - Stock: " << inventario[i].stock << endl;
        }
    }
}

// Función para vender productos
void venderProducto() {
    if (inventario.empty()) {
        cout << "No hay productos en inventario.\n";
        return;
    }

    int opcion, cantidad;
    mostrarInventario();

    cout << "\nSeleccione el número del producto que desea vender: ";
    cin >> opcion;
    opcion--; // Ajustar al índice del vector

    if (opcion < 0 || opcion >= inventario.size()) {
        cout << "Opción inválida.\n";
        return;
    }

    cout << "Ingrese la cantidad que desea vender: ";
    cin >> cantidad;

    if (cantidad <= 0) {
        cout << "Cantidad no válida.\n";
        return;
    }

    if (inventario[opcion].stock >= cantidad) {
        float total = cantidad * inventario[opcion].precio;
        inventario[opcion].stock -= cantidad;
        ganancias += total;
        cout << "Venta realizada. Total: $" << total << endl;
    } else {
        cout << "No hay suficiente stock disponible.\n";
    }
}

// Función para mostrar el resumen de la tienda
void mostrarResumen() {
    cout << "\n--- RESUMEN DE LA TIENDA ---\n";
    cout << "Ganancias totales: $" << ganancias << endl;
    mostrarInventario();
}

// Función para manejar el menú de opciones
void menu() {
    int opcion;
    do {
        cout << "\n--- SISTEMA DE TIENDA ---\n";
        cout << "1. Registrar productos\n";
        cout << "2. Mostrar inventario\n";
        cout << "3. Vender producto\n";
        cout << "4. Mostrar resumen\n";
        cout << "5. Salir\n";
        cout << "Seleccione una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                registrarProducto();
                break;
            case 2:
                mostrarInventario();
                break;
            case 3:
                venderProducto();
                break;
            case 4:
                mostrarResumen();
                break;
            case 5:
                cout << "Saliendo del programa...\n";
                break;
            default:
                cout << "Opción no válida.\n";
        }
    } while (opcion != 5);
}

// Función principal
int main() {
    try {
        menu();
    } catch (const exception &e) {
        cout << "Se ha producido un error: " << e.what() << endl;
    }

    return 0;
}