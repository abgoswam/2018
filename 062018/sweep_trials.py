###############################################################################
# FastTreesBinaryClassifier
from microsoftml_scikit import Pipeline, FileDataStream
from microsoftml_scikit.datasets import get_dataset
from microsoftml_scikit.ensemble import FastTreesBinaryClassifier
from microsoftml_scikit.feature_extraction.categorical import OneHotVectorizer

# data input (as a FileDataStream)
path = get_dataset('infert').as_filepath()
data = FileDataStream.read_csv(path)
# print(data.head())
#   age  case education  induced  parity  pooled.stratum  row_num  spontaneous  ...
# 0   26     1    0-5yrs        1       6               3        1            2  ...
# 1   42     1    0-5yrs        1       1               1        2            0  ...
# 2   39     1    0-5yrs        2       6               4        3            0  ...
# 3   34     1    0-5yrs        2       4               2        4            0  ...
# 4   35     1   6-11yrs        1       3              32        5            1  ...

# define the training pipeline
pipeline = Pipeline([
    OneHotVectorizer(columns={'edu': 'education'}),
    FastTreesBinaryClassifier(feature=['age', 'edu'], label='case')
])

# train, predict, and evaluate
# TODO: Replace with CV
predictions, metrics = pipeline.fit(data).test(data, 'case')

# print predictions
print(predictions.head())
#   PredictedLabel  Probability     Score
# 0               0     0.330738 -1.762120
# 1               0     0.337897 -1.681700
# 2               0     0.334428 -1.720559
# 3               0     0.331255 -1.756292
# 4               0     0.333299 -1.733252

# print evaluation metrics
print(metrics)
#        AUC  Accuracy  Positive precision  Positive recall  ...
# 0  0.502957  0.665323                   0                0  ...
