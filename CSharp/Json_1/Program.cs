using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;

namespace Json_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string s = @"{'Nodes' : [{
  'Name': 'Transforms.ColumnCopier',
  'Inputs': {
    'Column': [
      {
        'Name': 'Label',
        'Source': 'F14'
      }
    ],
    'Data': '$Var_304109bb4da247f6ba9161dc320dd292'
  },
  'Outputs': {
    'OutputData': '$Var_0f0f9930c29142c7945df3fa083328e2',
    'Model': '$Var_934c5888fb1547248ca58215e32dd7b1'
  }
},{
  'Name': 'Transforms.ColumnConcatenator',
  'Inputs': {
    'Column': [
      {
        'Name': 'Features',
        'Source': [
          'F4',
          'F1012'
        ]
      }
    ],
    'Data': '$Var_0f0f9930c29142c7945df3fa083328e2'
  },
  'Outputs': {
    'OutputData': '$Var_c428010c44324afe965e2c1633993566',
    'Model': '$Var_40c7217a42f948edb2f32bc94e95f880'
  }
},{
  'Name': 'Trainers.AveragedPerceptronBinaryClassifier',
  'Inputs': {
    'LearningRate': 1.0,
    'DecreaseLearningRate': false,
    'L2RegularizerWeight': 0.0,
    'NumIterations': 1,
    'InitWtsDiameter': 0.0,
    'Shuffle': true,
    'LossFunction': {
      'Name': 'HingeLoss',
      'Settings': {
        'Margin': 1.0
      }
    },
    'Calibrator': {
      'Name': 'PlattCalibrator',
      'Settings': {}
    },
    'MaxCalibrationExamples': 1000000,
    'ResetWeightsAfterXExamples': null,
    'DoLazyUpdates': true,
    'RecencyGain': 0.0,
    'RecencyGainMulti': false,
    'Averaged': true,
    'AveragedTolerance': 0.01,
    'InitialWeights': null,
    'StreamingCacheSize': 1000000,
    'LabelColumn': 'Label',
    'TrainingData': '$Var_c428010c44324afe965e2c1633993566',
    'FeatureColumn': 'Features',
    'NormalizeFeatures': 'Auto',
    'Caching': 'Auto'
  },
  'Outputs': {
    'PredictorModel': '$Var_592cf854bc534322877f58c012a45693'
  }
},{
  'Name': 'Transforms.ManyHeterogeneousModelCombiner',
  'Inputs': {
    'TransformModels': [
      '$Var_934c5888fb1547248ca58215e32dd7b1',
      '$Var_40c7217a42f948edb2f32bc94e95f880'
    ],
    'PredictorModel': '$Var_592cf854bc534322877f58c012a45693'
  },
  'Outputs': {
    'PredictorModel': '$Var_d8ef8ac076ab4ff084f336cbadaeb62d'
  }
}]}";

            JObject o = JObject.Parse(s);
            Console.WriteLine(o);

            var label = o["Nodes"][0]["Inputs"]["Column"][0]["Source"];

            var features = (JArray)o["Nodes"][1]["Inputs"]["Column"][0]["Source"];
            var features1 = features[0];
            var features2 = features[1];

            Console.WriteLine(label);
            Console.WriteLine(features1);
            Console.WriteLine(features2);

            Assert.Equal("F14", label);
            Assert.Equal("F4", features1);
            Assert.Equal("F1012", features2);

            Console.ReadKey();
        }
    }
}
