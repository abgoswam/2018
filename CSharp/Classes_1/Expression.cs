using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_1
{
    public abstract class Expression
    {
        public abstract double Evaluate(Dictionary<string, object> vars);
    }
}
