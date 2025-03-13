#include <iostream>
#include <functional>

using namespace std;

int sign(int n){
    if (n < 0){
        return -1;
    }else if (n > 0){
        return 1;
    }else{
        return 0;
    }
}

char bmi(double weight, double height){
    double bmi_value = weight / (height * height);

    if (bmi_value < 20){
        return 'U';
    } else if (bmi_value >= 20 && bmi_value < 20){
        
    }
}

int main(){
    //Funcion Lambda
    function <double(double)> fahrenheit_to_celsius = [](double f) {
        return (5.0 / 9.0) * (f - 32);
    };
    double fahrenheit;
    cout << "Ingrese la temperatura en grados Fahrenheit:" << endl;
    cin >> fahrenheit;

    double celsius = fahrenheit_to_celsius(fahrenheit);
    cout << "La temperatura en grados Celsius es: " << celsius << "\n";

    //Recursividad
    int num; 
    cout << "Ingrese un número: ";
    cin >> num;

    cout << "El signo de " << num << " es: " << sign(num) << endl;

    //BMI
    cout << "Ingresa el peso en Kilogramos: ";
    cin >> weight;
    cout << "Ingresa la altura en metros: ";
    cin >> height;

    char classification = bmi(weight, height);

    switch (classification)
    {
    case 'U': cout << "underweight" << endl; break;
    case 'N': cout << "normal" << endl; break;
    case '1': cout << "obese1" << endl; break;
    case '2': cout << "obese2" << endl; break;
    case '3': cout << "obese3" << endl; break;
    default:
        break;
    }

    return 0;
}