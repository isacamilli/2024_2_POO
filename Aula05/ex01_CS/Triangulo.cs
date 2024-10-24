class Triangulo {

    private double b, h;
    public Triangulo() {
        this.b = 0;
        this.h = 0;
    }

    public void set_base(double v) {
        if (v > 0) b = v;
        else 
            throw new ArgumentOutOfRangeException ("A base do triangulo não pode ser negativa");
    }

    public void set_altura(double v) {
        if (v > 0) h = v;
        else 
            throw ArgumentOutOfRangeException ("A base do triangulo não pode ser negativa");
    }

    public double get_base() {
        return b;
    }

    public double get_altura() {
        return h;
    }

    public double calc_area() {
        double area = b * h / 2;
        return area;
    }
}    