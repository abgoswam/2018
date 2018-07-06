using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Properties_1
{
    public class Student
    {
        public string FirstName { get; }
        public string LastName { get; }

        public Student(string firstName, string lastName)
        {
            if (string.IsNullOrEmpty(lastName))
            {
                throw new ArgumentException(message: "Cannot be blank", paramName: nameof(lastName));
            }

            FirstName = firstName;
            LastName = lastName;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.ReadKey();
        }
    }
}
