import java.util.Scanner;

class Circulo {
    public double r, p = 3.14;

    public double calc_area() {
        double area = r * r * p;
        return area; 
    }

    public double calc_circ() {
        double circ = p * 2 * r;
        return circ;
    }
}

public class Ex1 {

    public static void main(String[] args) {
        Circulo x = new Circulo();
        System.out.print("Informe o valor do raio: ");
        Scanner num = new Scanner(System.in);
        x.r = num.nextDouble();
        double area = x.calc_area();
        double circ = x.calc_circ();
        System.out.println(String.format("O valor de área é: %.2f", area));
        System.out.println(String.format("O valor da circunferência é: %.2f",circ));
        num.close();
    }
}