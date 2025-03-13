#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
    
struct Producto {
    string nombre;
    float precio;
    int stock;
};

vector<Producto> inventario;
float ganancias =0.0;

void registrarProducto(){
    int cantidad;
    cout << "Cuantos productos quieres registrar: ";
    cin >> cantidad;
    for (int a = 0; a < cantidad; a++){
        Producto nuevoproducto;
        cout << "Ingresa el nombre del producto: ";
        cin >> nuevoproducto.nombre;
        cout << "Ingresa el precio: ";
        cin >> nuevoproducto.precio;
        cout << "Ingresa la cantidad: ";
        cin >> nuevoproducto.stock;

        inventario.push_back(nuevoproducto);
        cout << "Producto agregado correctamente.\n ";

    }
};

void mostrarInventario(){
    cout<< "----- Inventario ----- \n";
    if(inventario.empty()){
        cout << "No hay productos. \n";
    }else{
        for(size_t i = 0; i < inventario.size();i++){
            cout << i+1 << ". " << inventario[i].nombre <<" - Precio $ "
            << inventario[i].precio << " - Stock: " 
            << inventario[i].stock << " unidades. \n";

        }
    }
};
void venderProducto(){
    if(inventario.empty()){
        cout << "No hay productos en el investario." << endl;
        return;
    }
    int opcion,cantidad;
    cout << "----- Venta -----" << endl;
    cout << "Seleccione el numero del producto que desea vender: ";
    cin >> opcion;
    opcion--;
    if(opcion < 0 || opcion >= inventario.size()){
        cout << "Opcion invalida. " << endl;
        return;
    }
    cout << "Ingresa la cantidad: ";
    cin >> cantidad;
    if(cantidad <= 0 ){
        cout << "Cantidad invalida. " << endl;
        return;
    }
    if(inventario[opcion].stock >= cantidad){
        float total= cantidad * inventario[opcion].precio;
        inventario[opcion].stock -= cantidad;
        ganancias += total;
        cout << "Venta realizada. Total: $" << total << endl;  
    }else {
        cout << "No hay sufiente stock. " << endl;
    }
    
};

void mostrarResumen(){
    cout << "----- Resumen -----" << endl;
    cout << "Ganancias totales $" << ganancias << endl;
    mostrarInventario();
};

void menu(){
    int opcion;
    
    do{ 
        cout <<"\n ----- TIENDA DE ABARROTES ----- \n"; 
        cout <<" 1.-Registra producto \n";
        cout <<" 2.-Mostrar inventario \n";
        cout <<" 3.-Vender producto \n";
        cout <<" 4.-Mostrar resumen \n";
        cout <<" 5.-Salir \n";
        cout <<"Selecione una opcion: ";
        cin >> opcion;

        switch(opcion){
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
            cout << "Terminaste la ejecucion. ";
            break;
        default:
            cout << "Opcion no valida. \n";
        }
    }while (opcion !=5 );

}


int main(){
    try{
        menu();
    } catch(const exception &e){
        cout << "Se presento un error: " << e.what() << "\n";
    }

    return 0; 
}
