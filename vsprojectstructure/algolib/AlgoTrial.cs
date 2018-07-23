using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using configlib;

namespace algolib
{
    public class AlgoTrial
    {
        public MySettings s;

        public AlgoTrial()
        {
            this.s = new MySettings();
        }
        public void ShowSettings()
        {
            this.s.ReadSettings();
        }
    }
}
