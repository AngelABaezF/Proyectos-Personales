#include <iostream>
#include <iomanip>
#include <ctime>
#include <sstream>

int main() {
    // Ejemplo de cadena de fecha y hora
    std::string fecha_hora_str = "Jul 16 03:38:22";

    // Estructura tm para almacenar la fecha y hora
    std::tm fecha_hora = {};
    
    // Usamos un istringstream para leer la cadena de texto
    std::istringstream ss(fecha_hora_str);

    // Extraemos el mes, día, hora, minuto y segundo
    ss >> std::get_time(&fecha_hora, "%b %d %H:%M:%S");

    // Comprobar si la conversión fue exitosa
    if (ss.fail()) {
        std::cerr << "Error al convertir la cadena a tiempo" << std::endl;
        return 1;
    }

    // Ajustar el año y el mes (std::tm usa el año como años desde 1900 y meses de 0 a 11)
    fecha_hora.tm_year = 124; // Año 2024 - 1900
    fecha_hora.tm_mon -= 1;   // Ajustar el mes (de 0 a 11)

    // Convertir la estructura tm a tiempo en segundos desde Epoch
    std::time_t timestamp = std::mktime(&fecha_hora);

    // Comprobar si mktime devolvió un valor válido
    if (timestamp == -1) {
        std::cerr << "Error al convertir la estructura tm a tiempo" << std::endl;
        return 1;
    }

    // Mostrar el número entero correspondiente
    std::cout << "Timestamp: " << timestamp << std::endl;

    return 0;
}
