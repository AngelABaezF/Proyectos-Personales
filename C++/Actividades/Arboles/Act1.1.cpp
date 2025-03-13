// Angel Alexander Baez Flores - A01425613
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <ctime>
#include <iomanip>

// Estructura para almacenar los registros de la bitácora
struct Registro {
    std::string mes;
    int dia;
    std::string hora;
    std::string ip;
    std::string razon;
    std::time_t timestamp;
};

// Función para convertir el nombre del mes a un número
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

// Función para convertir fecha y hora a timestamp
std::time_t convertirFechaATimestamp(const std::string& mes, int dia, const std::string& hora) {
    std::tm tm = {};
    tm.tm_year = 2024 - 1900; // Año actual menos 1900
    tm.tm_mon = convertirMesANumero(mes); // Mes en formato numérico
    tm.tm_mday = dia;

    // Parseo de la hora
    int horas, minutos, segundos;
    char sep;
    std::istringstream ss(hora);
    ss >> horas >> sep >> minutos >> sep >> segundos;

    tm.tm_hour = horas;
    tm.tm_min = minutos;
    tm.tm_sec = segundos;

    return std::mktime(&tm);
}

// Función para leer el archivo de bitácora y almacenar los datos en un vector
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
    archivoEntrada.close(); // Cierra el archivo después de leerlo
}

// Función para ordenar la bitácora por timestamp
void ordenarBitacora(std::vector<Registro>& bitacora) {
    std::sort(bitacora.begin(), bitacora.end(), [](const Registro& a, const Registro& b) {
        return a.timestamp < b.timestamp;
    });
}

// Función para realizar una búsqueda de registros con hora específica
std::vector<Registro> buscarRegistros(const std::vector<Registro>& bitacora) {
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

    std::cout << "Se encontraron " << resultados.size() << " registros en ese rango de fechas." << std::endl;
    return resultados;
}

// Función para mostrar registros en consola
void mostrarRegistros(const std::vector<Registro>& registros) {
    for (const auto& reg : registros) {
        std::cout << reg.mes << " " << reg.dia << " " << reg.hora << " " << reg.ip << " " << reg.razon << std::endl;
    }
}

// Función para guardar registros en un archivo
void guardarRegistrosEnArchivo(const std::vector<Registro>& registros, const std::string& archivo, const std::string& mesInicio, int diaInicio, const std::string& horaInicio, const std::string& mesFin, int diaFin, const std::string& horaFin) {
    std::ofstream archivoSalida(archivo); // Abre el archivo en modo escritura
    if (!archivoSalida) {
        std::cerr << "No se pudo abrir el archivo " << archivo << std::endl;
        return;
    }

    archivoSalida << "Resultados de la busqueda del " << mesInicio << " " << diaInicio << " " << horaInicio << " al " << mesFin << " " << diaFin << " " << horaFin << ":" << std::endl;
    for (const auto& reg : registros) {
        archivoSalida << reg.mes << " " << reg.dia << " " << reg.hora << " " << reg.ip << " " << reg.razon << std::endl;
    }

    archivoSalida.close();
}

int main() {
    std::vector<Registro> bitacora; // Vector para almacenar los registros de la bitácora
    std::string archivoEntrada = "bitacora.txt"; // Nombre del archivo de entrada
    std::string archivoSalida = "bitacora_ordenada.txt"; // Nombre del archivo de salida

    leerBitacora(bitacora, archivoEntrada);
    ordenarBitacora(bitacora);
    guardarRegistrosEnArchivo(bitacora, archivoSalida, "", 0, "", "", 0, "");

    int opcion;
    do {
        std::cout << "\n--- Menu ---" << std::endl;
        std::cout << "1. Realizar busqueda con hora especifica" << std::endl;
        std::cout << "2. Salir" << std::endl;
        std::cout << "Seleccione una opcion: ";
        std::cin >> opcion;

        if (opcion == 1) {
            auto registrosEncontrados = buscarRegistros(bitacora);
            if (!registrosEncontrados.empty()) {
                std::string verEnConsola;
                std::cout << "¿Desea ver los registros en consola? (si/no): ";
                std::cin >> verEnConsola;

                if (verEnConsola == "si") {
                    mostrarRegistros(registrosEncontrados);
                }

                std::string guardar;
                std::cout << "¿Desea guardar los registros en un archivo? (si/no): ";
                std::cin >> guardar;

                if (guardar == "si") {
                    std::string nombreArchivo;
                    std::cout << "Ingrese el nombre del archivo: ";
                    std::cin >> nombreArchivo;
                    guardarRegistrosEnArchivo(registrosEncontrados, nombreArchivo + ".txt", "", 0, "", "", 0, "");
                }
            }
        }
    } while (opcion != 2);

    std::cout << "Saliendo del programa..." << std::endl;
    return 0;
}
