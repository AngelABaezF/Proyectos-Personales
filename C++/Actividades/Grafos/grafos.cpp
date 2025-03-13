#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>
#include <queue>
#include <stack>
using namespace std;
class Grafo{
private:
    int n;
    map<int, string> indices;
    map<string, int> nodos;
    vector<vector<int>> mat;

public:
    Grafo(){
        n = 0;
    }
    void fromFile(string filename){
        ifstream file(filename);
        if (!file)
            throw runtime_error("No se pudo abrir el archivo.");
        file >> n;
        cout << n;
        file.ignore();
        // Lista de nodos
        for (int k = 0; k < n; k++){
            string nodeName;
            file >> nodeName;
            file.ignore();
            nodos[nodeName] = k;
            indices[k] = nodeName;
        }
        // Llenar la matriz de adyacencia
        mat.resize(n, vector<int>(n, 0));
        while (!file.eof()){
            string name1, name2;
            file >> name1 >> name2;
            file.ignore();
            int index1 = nodos[name1];
            int index2 = nodos[name2];
            mat[index1][index2] = 1;
            mat[index2][index1] = 1;
        }
        file.close();
    }
    void mostrarNodos(){
        cout << "Nodos" << endl;
        for (auto item : nodos){
            cout << item.first << " " << item.second << endl;
        }
    }
    void mostrarMat(){
        cout << "Matriz de adyacencia" << endl;
        cout << setw(5) << " ";
        for (auto item1 : nodos)
            cout << setw(5) << item1.first;
        cout << endl;
        for (auto item1 : nodos){
            cout << setw(5) << item1.first;
            for (auto item2 : nodos){
                cout << setw(5)<< mat[item1.second][item2.second];
            }
            cout << endl;
        }
    }
    void BFS(string inicio){
        cout << "-- BFS" << endl;
        vector<bool> visitado(n, false);
        queue<pair<int, int>> fila;
        int index = nodos[inicio];
        fila.push({index, 0});
        visitado[index] = true;
        while (!fila.empty()){
            pair<int, int> current = fila.front();
            fila.pop();
            cout << string(current.second, ' ') << indices[current.first] << endl;
            for (int k = 0; k < n; k++){
                if (mat[current.first][k] > 0 && !visitado[k]){
                    fila.push({k, current.second + 4});
                    visitado[k] = true;
                }
            }
        }
    }
    void DFS(string inicio){
        cout << "-- DFS" << endl;
        vector<bool> visitado(n, false);
        stack<pair<int, int>> pila;
        int index = nodos[inicio];
        pila.push({index, 0});
        visitado[index] = true;
        while (!pila.empty()){
            pair<int, int> current = pila.top();
            pila.pop();
            cout << string(current.second, ' ') << indices[current.first] << endl;
            for (int k = 0; k < n; k++){
                if (mat[current.first][k] > 0 && !visitado[k]){
                    pila.push({k, current.second + 4});
                    visitado[k] = true;
                }
            }
        }
    }
};
int main(){
    cout << "Ejemplo de grafos" << endl;
    Grafo grafo;
    grafo.fromFile("ciudades.txt");
    grafo.mostrarNodos();
    grafo.mostrarMat();
    grafo.BFS("Lar");
    grafo.DFS("Lar");
    return 0;
}