# deepneuralnet-chess
Given a chess position as input, predict the most likely result of the game.

This branch is an attempt to use the Google Cloud Machine Learning Engine to train a model. The major differences between this branch and master are as follows:
  1. tensorflow version 1.2 is required here, instead of tensorflow 1.4
  2. argparse is used in task.py to specify important data that may change often
  3. the model and task files are separate

This is the branch I will be focusing most of my efforts on.

**Installation**

```
pip install -r requirements.txt
```

**Training**

Coming soon

**Prediction**

Coming soon

**Results**

Given approximately 10,000,000 games as training data, the model has evaluation accuracy 45% on step 1. After 2,000 steps the model has accuracy 73.4%.

*Step 1*
```
Saving dict for global step 1: accuracy = 0.457,
accuracy/baseline_label_mean = 0.53075,
accuracy/threshold_0.500000_mean = 0.457,
auc = 0.54672,
auc_precision_recall = 0.537762,
global_step = 1,
labels/actual_label_mean = 0.53075, labels/prediction_mean = 0.942805,
loss = 1.367, precision/positive_threshold_0.500000_mean = 0.49425, recall/positive_threshold_0.500000_mean = 1.0
```

*Step 2000*

```
Saving dict for global step 2000: accuracy = 0.7345,
accuracy/baseline_label_mean = 0.53075,
accuracy/threshold_0.500000_mean = 0.7345,
auc = 0.8568, auc_precision_recall = 0.854109,
global_step = 2000,
labels/actual_label_mean = 0.53075, labels/prediction_mean = 0.549272,
loss = 0.46474, precision/positive_threshold_0.500000_mean = 0.722294, recall/positive_threshold_0.500000_mean = 0.847243
```
