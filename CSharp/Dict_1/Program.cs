using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dict_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Dictionary<string, int> dictionary = new Dictionary<string, int>();

            dictionary.Add("cat", 2);
            dictionary.Add("dog", 1);
            dictionary.Add("llama", 0);
            dictionary.Add("iguana", -1);

            Console.WriteLine(dictionary);

            Console.ReadKey();
        }
    }
}
