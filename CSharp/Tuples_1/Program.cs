using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tuples_1
{
    class Program
    {
        private static (string first, string middle, string last) LookupName(long id) // tuple return type
        {
            string first = "abhishek";
            string m = null;
            string l = "goswami";

            // retrieve first, middle and last from data storage
            return (first:first, middle:f, last:l); // tuple literal
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            var (first, middle, last) = LookupName(0);
            Console.WriteLine("{0}:{1}:{2}", first, middle, last);
        }
    }
}
