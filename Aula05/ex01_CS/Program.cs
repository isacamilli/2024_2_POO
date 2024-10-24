using System;

namespace ex01_CS
{
    class Program
    {
        static void Main(string[] args)
        {
            Triangulo x = new Triangulo();
            Console.WriteLine ("Informe o valor da base do triângulo: ");
            x.set_base (Console.ReadLine());
            Console.WriteLine ("Informe o valor da base do triângulo: ")
            x.set_altura (Console.ReadLine());
            Console.WriteLine($"Base: {x.set_base}");
            Console.WriteLine($"Base: {x.set_altura}");
        }
    }
}
