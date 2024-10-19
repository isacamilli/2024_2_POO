#include <iostream>
#include <iomanip>

using namespace std;
class cerchio {
    public:
    double r, p = 3.14;

    double calc_area(){
        double area = r * r * p;
        return area;
    }

    double calc_circun(){
        double circ = p * 2 * r;
        return circ;
    }
};

int main() {
    cerchio c;
    cout << "Informe o valor do raio: ";
    cin >> c.r;
    double area = c.calc_area();
    double circ = c.calc_circun();

    cout << fixed << setprecision(2);
    cout << "Área: " << area << endl;
    cout << "Circunferência: " << circ <<endl;

    return 0;
}