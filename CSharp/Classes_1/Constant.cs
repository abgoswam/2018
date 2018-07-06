using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_1
{
    public class Constant : Expression
    {
        double value;

        public Constant(double value)
        {
            this.value = value;
        }

        public override double Evaluate(Dictionary<string, object> vars)
        {
            return value;
        }
    }
}
