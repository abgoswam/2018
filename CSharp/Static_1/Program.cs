using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Static_1
{
    class Demo
    {
        public static void Main()
        {
            System.Console.WriteLine("DemoClass");

            OuterClass oc = new OuterClass();
            OuterClass.NestedClass reference = oc.CreateObjectOfNestedClass();
        }
    }

    class OuterClass
    {
        public class NestedClass
        {

        }
        public NestedClass CreateObjectOfNestedClass()
        {
            NestedClass obj = new NestedClass();
            return obj;
        }
    }
}
