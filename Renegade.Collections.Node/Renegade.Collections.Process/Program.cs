using System;

namespace Renegade.Collections.Process
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Node<string> node = new Node<string>("blayne");
            Node<string> node3 = new Node<string>("blayne");

            Console.WriteLine(node.Data.Equals(node3.Data));

            Console.WriteLine(node.Equals(node3));

            Console.ReadKey();
        }
    }
}
