using System;

namespace ex01_CS
{
    class Program
    {
        static void Main(string[] args)
        {
            Triangulo x = new Triangulo();
            Console.WriteLine ("Informe o valor da base do triângulo: ");
            x.set_base (double.Parse(Console.ReadLine()));
            Console.WriteLine ("Informe o valor da base do triângulo: ");
            x.set_altura (double.Parse(Console.ReadLine()));
            Console.WriteLine($"Base: {x.get_base()}");
            Console.WriteLine($"Base: {x.get_altura()}");
            Console.WriteLine($"Área: {x.calc_area()}");
        }
    }
}
