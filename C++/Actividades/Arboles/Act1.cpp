//Angel Alexander Baez Flores - A01425613
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <ctime>
#include <iomanip>

//estructura
struct Registro {
    std::string mes;
    int dia;
    std::string hora;
    std::string ip;
    std::string razon;
    std::time_t timestamp;
};

//mes a un numero
//complejidad O(1) es una serie de comparaciones constantes
int convertirMesANumero(const std::string& mes) {
    if (mes == "Jan") return 0;
    if (mes == "Feb") return 1;
    if (mes == "Mar") return 2;
    if (mes == "Apr") return 3;
    if (mes == "May") return 4;
    if (mes == "Jun") return 5;
    if (mes == "Jul") return 6;
    if (mes == "Aug") return 7;
    if (mes == "Sep") return 8;
    if (mes == "Oct") return 9;
    if (mes == "Nov") return 10;
    if (mes == "Dec") return 11;
    return -1;
}

//fecha y hora string a timestamp
//complejidad O(1) ya que son operaciones constantes
std::time_t convertirFechaATimestamp(const std::string& mes, int dia, const std::string& hora) {
    std::tm tm = {};
    tm.tm_year = 2024 - 1900;
    tm.tm_mon = convertirMesANumero(mes);
    tm.tm_mday = dia;

    //parseo
    int horas, minutos, segundos;
    char sep;
    std::istringstream ss(hora);
    ss >> horas >> sep >> minutos >> sep >> segundos;

    tm.tm_hour = horas;
    tm.tm_min = minutos;
    tm.tm_sec = segundos;

    return std::mktime(&tm);
}

//lee el archivo y almacena en un vector
//complejidad O(n) ya que se procesa cada línea una vez
void leerBitacora(std::vector<Registro>& bitacora, const std::string& archivo) {
    std::ifstream archivoEntrada(archivo);
    if (!archivoEntrada) {
        std::cerr << "No se pudo abrir el archivo " << archivo << std::endl;
        return;
    }

    std::string linea;
    while (std::getline(archivoEntrada, linea)) {
        std::istringstream ss(linea);
        Registro reg;
        ss >> reg.mes >> reg.dia >> reg.hora >> reg.ip;
        std::getline(ss, reg.razon);
        reg.timestamp = convertirFechaATimestamp(reg.mes, reg.dia, reg.hora);
        bitacora.push_back(reg);
    }
    archivoEntrada.close();
}

//ordena la bitacora
//complejidad O(n log n) en el caso promedio y O(n^2) en el peor
void ordenarBitacora(std::vector<Registro>& bitacora) {
    std::sort(bitacora.begin(), bitacora.end(), [](const Registro& a, const Registro& b) {
        return a.timestamp < b.timestamp;
    });
}

//guarda archivo
//complejidad O(n) ya que escribe cada registro en el archivo una vez
void guardarRegistrosOrdenados(const std::vector<Registro>& bitacora, const std::string& archivoSalida) {
    std::ofstream archivo(archivoSalida);
    if (!archivo) {
        std::cerr << "No se pudo abrir el archivo " << archivoSalida << std::endl;
        return;
    }

    for (const auto& reg : bitacora) {
        archivo << reg.mes << " " << reg.dia << " " << reg.hora << " " << reg.ip << " " << reg.razon << std::endl;
    }

    archivo.close();
}

//busca registros
//complejidad O(n) para la búsqueda lineal de registros en el rango
void buscarRegistrosConHora(const std::vector<Registro>& bitacora) {
    std::string mesInicio, mesFin, horaInicio, horaFin;
    int diaInicio, diaFin;

    std::cout << "Ingrese la fecha de inicio (Mes Dia Hora hh:mm:ss): ";
    std::cin >> mesInicio >> diaInicio >> horaInicio;
    std::cout << "Ingrese la fecha de fin (Mes Dia Hora hh:mm:ss): ";
    std::cin >> mesFin >> diaFin >> horaFin;

    std::time_t inicio = convertirFechaATimestamp(mesInicio, diaInicio, horaInicio);
    std::time_t fin = convertirFechaATimestamp(mesFin, diaFin, horaFin);

    std::vector<Registro> resultados;
    for (const auto& reg : bitacora) {
        if (reg.timestamp >= inicio && reg.timestamp <= fin) {
            resultados.push_back(reg);
        }
    }

    std::cout << "Se encontraron " << resultados.size() << " registros en ese rango de fechas y horas.\n";

    std::string opcion;
    std::cout << "¿Desea ver los resultados en consola? (si/no): ";
    std::cin >> opcion;

    if (opcion == "si") {
        for (const auto& reg : resultados) {
            std::cout << reg.mes << " " << reg.dia << " " << reg.hora << " " << reg.ip << " " << reg.razon << std::endl;
        }
    }

    std::cout << "¿Desea guardar los resultados en un archivo? (si/no): ";
    std::cin >> opcion;

    if (opcion == "si") {
        std::string nombreArchivo;
        std::cout << "Ingrese el nombre del archivo (sin extension): ";
        std::cin >> nombreArchivo;
        std::ofstream archivoSalida(nombreArchivo + ".txt");

        archivoSalida << "Resultados desde " << mesInicio << " " << diaInicio << " " << horaInicio;
        archivoSalida << " hasta " << mesFin << " " << diaFin << " " << horaFin << ":\n";
        for (const auto& reg : resultados) {
            archivoSalida << reg.mes << " " << reg.dia << " " << reg.hora << " " << reg.ip << " " << reg.razon << std::endl;
        }
        archivoSalida.close();
    }
}

int main() {
    std::vector<Registro> bitacora;
    std::string archivoEntrada = "bitacora.txt";
    std::string archivoSalida = "bitacora_ordenada.txt";

    leerBitacora(bitacora, archivoEntrada);
    ordenarBitacora(bitacora);
    guardarRegistrosOrdenados(bitacora, archivoSalida);

    int opcion;
    do {
        std::cout << "Seleccione una opcion:\n";
        std::cout << "1. Buscar registros por rango de fechas y horas\n";
        std::cout << "2. Salir\n";
        std::cin >> opcion;

        switch (opcion) {
            case 1:
                buscarRegistrosConHora(bitacora);
                break;
            case 2:
                std::cout << "Saliendo del programa.\n";
                break;
            default:
                std::cout << "Opción no valida, por favor intente de nuevo.\n";
                break;
        }
    } while (opcion != 2);

    return 0;
}
