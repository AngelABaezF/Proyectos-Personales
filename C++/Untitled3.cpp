#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

class MyHash {
private:
    vector<pair<string, int>> table;

    // Tipo: Iterativo
    // Complejidad: O(n) donde n es la longitud de la clave.
    int hash(const string& key) {
        int hash = 0;
        for (char c : key) {
            hash = (hash * 31 + c) % table.size();
        }
        return hash;
    }

    // Tipo: Iterativo
    // Complejidad: O(sqrt(n)) donde n es el número que se está verificando si es primo.
    bool esPrimo(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        int lim = sqrt(n);
        for (int k = 3; k <= lim; k += 2) {
            if (n % k == 0) return false;
        }
        return true;
    }

public:
    // Tipo: Iterativo
    // Complejidad: O(n * m), donde n es el tamaño del vector de nombres y m es el número de intentos para encontrar una posición libre en la tabla.
    MyHash(const vector<string>& names) {
        int prime = (names.size() * 2) + 1;
        while (!esPrimo(prime)) {
            prime++;
        }
        cout << "Primo: " << prime << endl;
        table.resize(prime, {"", -1});
        int maxSaltos = 0;
        for (int k = 0; k < names.size(); k++) {
            int index = hash(names[k]);
            int saltos = 0;
            while (table[index].second != -1) {
                index = (index + 1) % table.size();
                saltos++;
            }
            table[index] = {names[k], k};
            if (saltos > maxSaltos) {
                maxSaltos = saltos;
            }
        }
        cout << "Numero maximo de saltos en la tabla: " << maxSaltos << endl;
    }

    // Tipo: Iterativo
    // Complejidad: O(n), donde n es el tamaño de la tabla hash.
    void showTable() {
        for (int k = 0; k < table.size(); k++) {
            cout << "(" << table[k].first << "," << table[k].second << ") ";
        }
        cout << endl;
    }

    // Tipo: Iterativo
    // Complejidad: O(m), donde m es el número de colisiones que ocurren.
    int find(const string& key) {
        int index = hash(key);
        int saltos = 0;
        while (table[index].second != -1) {
            if (table[index].first == key) return table[index].second;
            index = (index + 1) % table.size();
            saltos++;
        }
        return -1;
    }
};

int main() {
    vector<vector<string>> testCases = {
        {"Ana", "Vale", "Sergio", "Luis", "Mario", "Laura", "Jorge", "Sofia", "Carlos", "Isabel", "Pedro", "Juan", "Andres", "Julieta", "Carolina", "Fernanda", "Miguel", "Nicolas", "Camila", "Diego", "Tom", "Jerry", "Spike", "Tyke", "Butch", "Nibbles", "Tuffy", "Quacker", "Lightning", "Muscles", "Harry", "Ron", "Hermione", "Ginny", "Luna", "Neville", "Draco", "Cho", "Cedric", "Sirius"},
    };

    for (const auto& names : testCases) {
        cout << "Probando con " << names.size() << " nombres:" << endl;
        MyHash hash(names);
        hash.showTable();
        for (const auto& name : names) {
            cout << "Indice de " << name << ": " << hash.find(name) << endl;
        }
        cout << endl;
    }

    return 0;
}
