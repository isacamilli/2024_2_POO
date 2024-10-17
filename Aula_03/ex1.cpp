#include <iostream>

using namespace std;

class Triangulo {
    public: //controlar a visibilidade dos membros
    double b = 0, h = 0;
    double calc_area() {
        double area = b * h / 2;
        return area;
    }
};

int main() {
    Triangulo x; //em java -> Trangulo x = new Triangulo()
    cout << x.b <<  ' ' << x.h << endl; 
    cout << "Informe o valor da base: ";
    cin >> x.b;
    cout << "Informe o valor da altura: ";
    cin >> x.h;

    double area = x.calc_area();
    cout << "A área do triângulo informado é: " << x.calc_area() << endl;

    return 0;
}
