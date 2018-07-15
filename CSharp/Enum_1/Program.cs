using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Enum_1
{
    class Program
    {
        public enum ColumnPurpose
        {
            Ignore = 0,
            Name = 1,
            Label = 2,
            NumericFeature = 3,
            CategoricalFeature = 4,
            TextFeature = 5,
            Weight = 6,
            GroupId = 7,
            ImagePath = 8
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("{0}:{1}", ColumnPurpose.Ignore, ColumnPurpose.Ignore.ToString());
            Console.ReadKey();
        }
    }
}
