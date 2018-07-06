using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_1
{
    public class Operation : Expression
    {
        Expression left;
        char op;
        Expression right;
        public Operation(Expression left, char op, Expression right)
        {
            this.left = left;
            this.op = op;
            this.right = right;
        }
        public override double Evaluate(Dictionary<string, object> vars)
        {
            double x = left.Evaluate(vars);
            double y = right.Evaluate(vars);
            switch (op)
            {
                case '+': return x + y;
                case '-': return x - y;
                case '*': return x * y;
                case '/': return x / y;
            }
            throw new Exception("Unknown operator");
        }
    }
}
