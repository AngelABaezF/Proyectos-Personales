#include <iostream>
#include <functional>
#include <string>
#include <vector>
#include <numeric>
#include <omp.h>
using namespace std;

// Funciones como ciudadanos de primera clase
int cuadrado(int x){
    return x * x;
}

int aplicarFuncion(int (*f)(int), int x){
    return f(x);
}

// Inmutabilidad
void imprimirArray(const int arr[], int tam){
    for (int i = 0; i < tam; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Funciones Puras
int suma(int a, int b){
    return a + b;
}

// Transparencia Referencial
int multiplicar(int a, int b){
    return a * b;
}

// Composición de funciones
string prepararCafe(string agua){
    return agua + "+ Cafe";
}

string agregarLeche(string cafe){
    return cafe + "+ Leche";
}

string endulzar(string cafeLeche){
    return cafeLeche + "+ azucar";
}

string hacerCafe(){
    return endulzar(agregarLeche(prepararCafe("agua caliente")));
}

// Recursión
int factorial(int n){
    return (n == 0) ? 1 : n * factorial(n - 1);
}

// Tipos de datos algebraicos
class PedidoIndividual{
public:
    string nombre;
    PedidoIndividual(const string& nombre) : nombre(nombre){}
};

class PedidoCombo {
public:
    string plato1, plato2, bebida;
    PedidoCombo(const string& p1, const string& p2, const string& b) : plato1(p1), plato2(p2), bebida(b){}
};

void procesarPedido(const PedidoIndividual& pedido){
    cout << "Pedido individual: " << pedido.nombre << endl;
}

void procesarPedido(const PedidoCombo& pedido){
    cout << "Combo: " << pedido.plato1 << ", " << pedido.plato2 << ", " << pedido.bebida << endl;
}

// Paralelismo más sencillo
int suma_paralela(const vector<int>& nums){
    int resultado = 0;
#pragma omp parallel for reduction(+:resultado)
    for (size_t i = 0; i < nums.size(); ++i){
        resultado += nums[i];
    }
    return resultado;
}

int main(){
    // Funciones como Ciudadanos de Primera clase
    cout << aplicarFuncion(cuadrado, 4) << endl;
    
    // Inmutabilidad
    const int valores[] = {1, 2, 3, 4, 5};
    imprimirArray(valores, 5);
    
    // Funciones Puras
    cout << suma(4, 3) << endl;
    
    // Evaluación Perezosa
    auto calcular = []() -> int {
        cout << "Calculando..." << endl;
        return 10 * 2;
    };
    function<int()> resultado = calcular;
    cout << "Antes de llamar la función..." << endl;
    cout << "Resultado: " << resultado() << endl;

    // Transparencia Referencial
    cout << multiplicar(4, 5) << endl;

    // Recursión
    cout << factorial(5) << endl;

    // Composición de funciones
    cout << "Bebida lista: " << hacerCafe() << endl;

    PedidoIndividual pedido1("Hamburguesa");
    PedidoCombo pedido2("Hamburguesa", "Papas", "Refresco");

    procesarPedido(pedido1);
    procesarPedido(pedido2);
    
    // Paralelismo más sencillo
    vector<int> nums = {1, 2, 3, 4, 5};
    int resultado_final = suma_paralela(nums);
    cout << "La suma de los números es: " << resultado_final << endl;

    return 0;
}

// Este codigo pertenece a Ángel Alexander Báez Flores | A01425613