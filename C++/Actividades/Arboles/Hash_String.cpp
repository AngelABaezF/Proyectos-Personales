#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

class MyHash {
private:
    vector<pair<string, int>> table;
    /* 
		Tipo: Iterativo
    	Complejidad: O(n) n es la longitud de la clave
    */
    int hash(const string& key) {
        int hash = 0;
        for (char c : key) {
            hash = (hash * 31 + c) % table.size();
        }
        return hash;
    }
	/*
    	Tipo: Iterativo
    	Complejidad: O(sqrt(n)) n es el número que se está verificando si es primo
    */
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
	/*
    	Tipo: Iterativo
    	Complejidad: O(n * m) n es el tamaño del vector y m es el número de saltos para encontrar una posición libre
    */
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
	/*
    	Tipo: Iterativo
    	Complejidad: O(n) n es el tamaño de la tabla
    */
    void showTable() {
        for (int k = 0; k < table.size(); k++) {
            cout << "(" << table[k].first << "," << table[k].second << ") ";
        }
        cout << endl;
    }
	/*
    	Tipo: Iterativo
    	Complejidad: O(m) m es el número de colisiones que ocurren
    */
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
    	//
        {"Ana", "Vale", "Sergio", "Luis", "Mario", "Laura", "Jorge", "Sofia", "Carlos", "Isabel"},
        // 100 nombres
		/*{
		    "Ana", "Vale", "Sergio", "Luis", "Mario", "Laura", "Jorge", "Sofia", "Carlos", "Isabel",
		    "Juan", "Pedro", "Lucia", "Fernando", "Mariana", "Gabriel", "Camila", "Andrea", "Daniel", "Paula",
		    "Diego", "Miguel", "Angela", "Francisco", "Natalia", "Rodrigo", "Elena", "Victor", "Gabriela", "Manuel",
		    "Raul", "Pablo", "Cristina", "Alvaro", "Marta", "David", "Claudia", "Hector", "Alejandro", "Ines",
		    "Javier", "Emilia", "Roberto", "Victoria", "Alfredo", "Patricia", "Gustavo", "Raquel", "Felipe", "Teresa",
		    "Rafael", "Lorena", "Eduardo", "Beatriz", "Ricardo", "Monica", "Hugo", "Olga", "Federico", "Margarita",
		    "Alonso", "Rosa", "Martin", "Carmen", "Jaime", "Silvia", "Julio", "Veronica", "Nicolas", "Esther",
		    "Santiago", "Sara", "Agustin", "Pilar", "Arturo", "Yolanda", "Bruno", "Alicia", "Armando", "Graciela",
		    "Mauricio", "Isidora", "Gilberto", "Fabiola", "Enrique", "Regina", "Ignacio", "Leticia", "Oscar", "Catalina",
		    "Guillermo", "Susana", "Emilio", "Virginia", "Marcos", "Florencia", "Joaquin", "Belén", "Cristian", "Alejandra"
		},*/
		// 1000 nombres
		/*{
		    "Ana", "Vale", "Sergio", "Luis", "Mario", "Laura", "Jorge", "Sofia", "Carlos", "Isabel",
		    "Juan", "Pedro", "Lucia", "Fernando", "Mariana", "Gabriel", "Camila", "Andrea", "Daniel", "Paula",
		    "Diego", "Miguel", "Angela", "Francisco", "Natalia", "Rodrigo", "Elena", "Victor", "Gabriela", "Manuel",
		    "Raul", "Pablo", "Cristina", "Alvaro", "Marta", "David", "Claudia", "Hector", "Alejandro", "Ines",
		    "Javier", "Emilia", "Roberto", "Victoria", "Alfredo", "Patricia", "Gustavo", "Raquel", "Felipe", "Teresa",
		    "Rafael", "Lorena", "Eduardo", "Beatriz", "Ricardo", "Monica", "Hugo", "Olga", "Federico", "Margarita",
		    "Alonso", "Rosa", "Martin", "Carmen", "Jaime", "Silvia", "Julio", "Veronica", "Nicolas", "Esther",
		    "Santiago", "Sara", "Agustin", "Pilar", "Arturo", "Yolanda", "Bruno", "Alicia", "Armando", "Graciela",
		    "Mauricio", "Isidora", "Gilberto", "Fabiola", "Enrique", "Regina", "Ignacio", "Leticia", "Oscar", "Catalina",
		    "Guillermo", "Susana", "Emilio", "Virginia", "Marcos", "Florencia", "Joaquin", "Belén", "Cristian", "Alejandra",
		    "Antonio", "Rocio", "Jose", "Miriam", "Adrian", "Elisa", "Sebastian", "Julia", "Ernesto", "Isabel",
		    "Luis", "Elena", "Ricardo", "Amparo", "Andres", "Susana", "Jorge", "Lorena", "Vicente", "Eva",
		    "Raul", "Esther", "Pablo", "Mercedes", "Gerardo", "Natalia", "Felipe", "Rosa", "Rodrigo", "Teresa",
		    "Salvador", "Patricia", "Samuel", "Carolina", "Vicente", "Lucia", "Benito", "Estela", "Gonzalo", "Angela",
		    "Ramon", "Claudia", "Emilio", "Magdalena", "Eduardo", "Alejandra", "Ruben", "Valeria", "Julian", "Laura",
		    "Hugo", "Margarita", "Joaquin", "Pilar", "Esteban", "Cristina", "Francisco", "Alba", "Leandro", "Raquel",
		    "Julio", "Paula", "Sergio", "Veronica", "Adolfo", "Silvia", "Lorenzo", "Marta", "Arturo", "Noelia",
		    "Carlos", "Luisa", "Gregorio", "Nuria", "Jesus", "Milagros", "Miguel", "Gloria", "Felipe", "Eva",
		    "Ignacio", "Marta", "Nicolas", "Nieves", "Lucas", "Alicia", "Mauricio", "Carolina", "Federico", "Carmen",
		    "Alejandro", "Dolores", "Vicente", "Ruth", "Mariano", "Beatriz", "Bruno", "Soledad", "Gilberto", "Julia",
		    "Ramiro", "Elvira", "Felipe", "Miriam", "Rafael", "Belen", "Enrique", "Olga", "Antonio", "Ana",
		    "Manuel", "Celia", "Oscar", "Sara", "Marcos", "Alba", "Mario", "Adriana", "Gustavo", "Adela",
		    "David", "Aurora", "Arturo", "Victoria", "Fernando", "Blanca", "Gerardo", "Valentina", "Cesar", "Ines",
		    "Emilio", "Marta", "Nicolas", "Susana", "Guillermo", "Gloria", "Eduardo", "Angela", "Pablo", "Clara",
		    "Javier", "Amalia", "Ignacio", "Raquel", "Ricardo", "Teresa", "Diego", "Isabel", "Francisco", "Magdalena",
		    "Rodrigo", "Sara", "Ruben", "Margarita", "Julio", "Cristina", "Raul", "Silvia", "Santiago", "Pilar",
		    "Adrian", "Sofia", "Ramon", "Maria", "Alfredo", "Luisa", "Juan", "Eva", "Martin", "Carmen",
		    "Felipe", "Gabriela", "Alvaro", "Lorena", "Cesar", "Carolina", "Andres", "Monica", "Oscar", "Marina",
		    "Bruno", "Veronica", "Hugo", "Nieves", "Sebastian", "Leticia", "Joaquin", "Patricia", "Enrique", "Paula",
		    "Lucas", "Beatriz", "Samuel", "Valeria", "Gonzalo", "Isabel", "Gregorio", "Lucia", "Esteban", "Amparo",
		    "Ramiro", "Yolanda", "Alberto", "Nuria", "Julian", "Emilia", "Arturo", "Carla", "Mariano", "Mariana",
		    "Gerardo", "Claudia", "Vicente", "Gloria", "Salvador", "Ana", "Ricardo", "Eva", "Ignacio", "Dolores",
		    "Jesus", "Marta", "Francisco", "Raquel", "Raul", "Carolina", "Victor", "Rosa", "Rafael", "Olga",
		    "Javier", "Nieves", "Diego", "Carmen", "Antonio", "Isabel", "Alejandro", "Marina", "Manuel", "Patricia",
		    "Ruben", "Pilar", "Lucas", "Silvia", "Felipe", "Lorena", "Emilio", "Elena", "Alfredo", "Margarita",
		    "Ramiro", "Blanca", "Santiago", "Aurora", "Hector", "Victoria", "Nicolas", "Amalia", "Guillermo", "Cristina",
		    "Eduardo", "Amparo", "Julian", "Susana", "Alvaro", "Gloria", "Fernando", "Maria", "Pablo", "Teresa",
		    "Luis", "Lucia", "Sebastian", "Miriam", "Joaquin", "Clara", "Gerardo", "Sara", "Julio", "Ines",
		    "Martin", "Magdalena", "Arturo", "Angela", "Enrique", "Raquel", "Rafael", "Gabriela", "David", "Alicia",
		    "Diego", "Ana", "Juan", "Lorena", "Adrian", "Monica", "Oscar", "Carmen", "Ignacio", "Beatriz",
		    "Victor", "Dolores", "Rodrigo", "Eva", "Felipe", "Patricia", "Javier", "Silvia", "Ramon", "Raquel",
		    "Miguel", "Lucia", "Emilio", "Pilar", "Hugo", "Cristina", "Carlos", "Isabel", "Eduardo", "Amalia",
		    "Alfredo", "Elena", "Bruno", "Blanca", "Ricardo", "Sara", "Lucas", "Gabriela", "Sergio", "Claudia",
		    "Ruben", "Gloria", "Guillermo", "Marta", "Sebastian", "Paula", "Alejandro", "Isabel", "Rafael", "Monica",
		    "Santiago", "Carolina", "Arturo", "Lorena", "Ramiro", "Nuria", "Luis", "Elvira", "Manuel", "Valeria",
		    "Joaquin", "Adriana", "Victor", "Miriam", "Julian", "Alicia", "Enrique", "Angela", "Lucas", "Nieves",
		    "Ignacio", "Susana", "Fernando", "Patricia", "David", "Ana", "Javier", "Clara", "Diego", "Beatriz",
		    "Pablo", "Dolores", "Hugo", "Lucia", "Ricardo", "Blanca", "Antonio", "Eva", "Gerardo", "Rosa",
		    "Miguel", "Gabriela", "Rodrigo", "Elena", "Felipe", "Victoria", "Julio", "Cristina", "Emilio", "Aurora",
		    "Alvaro", "Amparo", "Francisco", "Ines", "Ruben", "Sara", "Julio", "Teresa", "Fernando", "Alejandra",
		    "Javier", "Carmen", "David", "Monica", "Lucas", "Dolores", "Pablo", "Gabriela", "Gerardo", "Blanca",
		    "Raul", "Miriam", "Sergio", "Elena", "Felipe", "Gloria", "Alfredo", "Susana", "Ricardo", "Valeria",
		    "Carlos", "Alicia", "Miguel", "Patricia", "Santiago", "Maria", "Oscar", "Lorena", "Victor", "Nieves",
		    "Julio", "Ines", "Rafael", "Silvia", "Ruben", "Teresa", "Emilio", "Elvira", "Luis", "Carmen",
		    "Francisco", "Isabel", "Ramon", "Cristina", "Ignacio", "Amparo", "Eduardo", "Lorena", "Alvaro", "Gloria",
		    "Fernando", "Raquel", "Gerardo", "Blanca", "Luis", "Eva", "Arturo", "Marta", "Martin", "Sara",
		    "Alberto", "Nuria", "Bruno", "Susana", "Jesus", "Patricia", "Samuel", "Isabel", "Vicente", "Monica",
		    "Hugo", "Valeria", "Joaquin", "Amalia", "Andres", "Gabriela", "Pablo", "Miriam", "Julian", "Teresa",
		    "Alejandro", "Blanca", "Nicolas", "Carmen", "Ruben", "Eva", "Raul", "Maria", "David", "Ana",
		    "Ricardo", "Lorena", "Sebastian", "Dolores", "Victor", "Silvia", "Lucas", "Marta", "Ramon", "Clara",
		    "Alfredo", "Nieves", "Enrique", "Miriam", "Joaquin", "Amparo", "Adrian", "Patricia", "Carlos", "Gabriela",
		    "Fernando", "Isabel", "Javier", "Lorena", "Ignacio", "Elena", "Miguel", "Aurora", "Diego", "Susana",
		    "Martin", "Rosa", "Julio", "Carmen", "Pablo", "Blanca", "Francisco", "Marta", "Gerardo", "Teresa",
		    "Alvaro", "Silvia", "Raul", "Cristina", "Santiago", "Dolores", "Ruben", "Amalia", "Oscar", "Gabriela",
		    "Felipe", "Isabel", "Bruno", "Aurora", "Joaquin", "Ana", "Julian", "Patricia", "David", "Eva",
		    "Alfredo", "Lucia", "Luis", "Susana", "Ricardo", "Clara", "Rafael", "Monica", "Emilio", "Raquel",
		    "Carlos", "Miriam", "Miguel", "Nieves", "Hugo", "Elvira", "Javier", "Victoria", "Gerardo", "Amparo",
		    "Lucas", "Blanca", "Diego", "Teresa", "Sergio", "Marta", "Francisco", "Ana", "Ruben", "Lorena",
		    "Pablo", "Cristina", "Fernando", "Miriam", "Luis", "Eva", "Rodrigo", "Patricia", "Enrique", "Isabel",
		    "Antonio", "Marta", "Julio", "Aurora", "Ignacio", "Gabriela", "Martin", "Clara", "Ramon", "Dolores",
		    "Raul", "Nieves", "Eduardo", "Carmen", "Alvaro", "Blanca", "Santiago", "Susana", "Arturo", "Monica",
		    "Alberto", "Maria", "Felipe", "Cristina", "Joaquin", "Elena", "Miguel", "Teresa", "Lucas", "Valeria",
		    "Francisco", "Patricia", "Julian", "Amalia", "Bruno", "Gabriela", "Oscar", "Miriam", "Javier", "Rosa",
		    "Ignacio", "Aurora", "Fernando", "Susana", "Gerardo", "Eva", "Hugo", "Blanca", "Antonio", "Teresa",
		    "Ricardo", "Lorena", "David", "Clara", "Emilio", "Patricia", "Luis", "Isabel", "Alejandro", "Monica",
		    "Sergio", "Ramon", "Raul", "Amalia", "Pablo", "Dolores", "Julio", "Marta", "Rafael", "Maria",
		    "Lucas", "Nieves", "Felipe", "Cristina", "Ruben", "Aurora", "Santiago", "Lorena", "Martin", "Elena",
		    "Arturo", "Carmen", "Javier", "Susana", "Miguel", "Dolores", "Joaquin", "Patricia", "Gerardo", "Blanca",
		    "Enrique", "Amparo", "Julian", "Ana", "Victor", "Amalia", "Alvaro", "Nieves", "Hugo", "Carmen",
		    "David", "Lucia", "Ignacio", "Aurora", "Fernando", "Cristina", "Francisco", "Isabel", "Pablo", "Eva",
		    "Luis", "Marta", "Lucas", "Patricia", "Julio", "Monica", "Ruben", "Gabriela", "Ramon", "Clara",
		    "Raul", "Dolores", "Eduardo", "Susana", "Alberto", "Elena", "Santiago", "Blanca", "Felipe", "Maria",
		    "Ricardo", "Teresa", "Javier", "Miriam", "Emilio", "Lorena", "Hector", "Amalia", "Carlos", "Eva",
		    "Joaquin", "Cristina", "David", "Isabel", "Gerardo", "Aurora", "Lucas", "Marta", "Enrique", "Carmen",
		    "Luis", "Clara", "Pablo", "Teresa", "Raul", "Elena", "Felipe", "Blanca", "Antonio", "Susana",
		    "Ignacio", "Patricia", "Alejandro", "Dolores", "Fernando", "Monica", "Rafael", "Gabriela", "Santiago", "Rosa"
		},*/


    };

    for (const auto& names : testCases) {
        cout << "Probando con " << names.size() << " nombres:" << endl;
        MyHash hash(names);
        hash.showTable();
        /*for (const auto& name : names) {
            cout << "Indice de " << name << ": " << hash.find(name) << endl;
        }*/
        cout << endl;
    }

    return 0;
}
