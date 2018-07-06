using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_1
{
    public class Point
    {
        public int x, y;
        public Point(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }

    public class Point3D : Point
    {
        public int z;
        public Point3D(int x, int y, int z) : base(x, y)
        {
            this.z = z;
        }
    }

    public class Pair<TFirst, TSecond>
    {
        public TFirst First;
        public TSecond Second;
    }

    public class Color
    {
        public static readonly Color Black = new Color(0, 0, 0);
        public static readonly Color White = new Color(255, 255, 255);
        public static readonly Color Red = new Color(255, 0, 0);
        public static readonly Color Green = new Color(0, 255, 0);
        public static readonly Color Blue = new Color(0, 0, 255);
        private byte r, g, b;
        public Color(byte r, byte g, byte b)
        {
            this.r = r;
            this.g = g;
            this.b = b;
        }
    }

    class RefExample
    {
        static void Swap(ref int x, ref int y)
        {
            int temp = x;
            x = y;
            y = temp;
        }
        public static void SwapExample()
        {
            int i = 1, j = 2;
            Swap(ref i, ref j);
            Console.WriteLine($"{i} {j}");    // Outputs "2 1"
        }
    }

    class OutExample
    {
        static void Divide(int x, int y, out int result, out int remainder)
        {
            result = x / y;
            remainder = x % y;
        }
        public static void OutUsage()
        {
            Divide(10, 3, out int res, out int rem);
            Console.WriteLine("{0} {1}", res, rem);	// Outputs "3 1"
        }
    }


    class Entity
    {
        static int nextSerialNo;
        int serialNo;

        public Entity()
        {
            serialNo = nextSerialNo++;
        }
        public int GetSerialNo()
        {
            return serialNo;
        }
        public static int GetNextSerialNo()
        {
            return nextSerialNo;
        }
        public static void SetNextSerialNo(int value)
        {
            nextSerialNo = value;
        }
    }



    class Program
    {
        static void Main(string[] args)
        {
            Point p1 = new Point(0, 0);
            Point p2 = new Point(10, 20);

            Point a = new Point(10, 20);
            Point b = new Point3D(10, 20, 30);

            Pair<int, string> pair = new Pair<int, string>
            {
                First = 1,
                Second = "two"
            };

            Entity.SetNextSerialNo(1000);
            Entity e1 = new Entity();
            Entity e2 = new Entity();
            Console.WriteLine(e1.GetSerialNo());
            Console.WriteLine(e2.GetSerialNo());
            Console.WriteLine(Entity.GetNextSerialNo());
            Console.WriteLine("Hello World!");

            Expression e = new Operation(
                new VariableReference("x"),
                '*',
                new Operation(
                    new VariableReference("y"),
                    '+',
                    new Constant(2)
                )
            );

            Dictionary<string, object> vars = new Dictionary<string, object>();
            vars["x"] = 3;
            vars["y"] = 5;
            Console.WriteLine(e.Evaluate(vars));        // Outputs "21"
            //vars["x"] = 1.5;
            //vars["y"] = 9;
            //Console.WriteLine(e.Evaluate(vars));		// Outputs "16.5"
            Console.ReadKey();
        }
    }
}
