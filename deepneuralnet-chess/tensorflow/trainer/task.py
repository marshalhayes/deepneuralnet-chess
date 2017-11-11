import tensorflow as tf
import numpy as np
import logging as log

COLS_HEADERS = "a8,b8,c8,d8,e8,f8,g8,h8,a7,b7,c7,d7,e7,f7,g7,h7,a6,b6,c6,d6,e6,f6,g6,h6,a5,b5,c5,d5,e5,f5,g5,h5,a4,b4,c4,d4,e4,f4,g4,h4,a3,b3,c3,d3,e3,f3,g3,h3,a2,b2,c2,d2,e2,f2,g2,h2,a1,b1,c1,d1,e1,f1,g1,h1,whos_move,fen,result"
CSV_COLUMNS = COLS_HEADERS.split(',')

TRAINING_DATA = "trainer/data/train-data-10000.csv"
TEST_DATA = "trainer/data/test-data-10000.csv"

def input_fn():
    # Preprocess your data here...

    # ...then return 1) a mapping of feature columns to Tensors with
    # the corresponding feature data, and 2) a Tensor containing labels
    return feature_cols, labels

# Load datasets
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TRAINING_DATA,
      target_dtype=np.int,
      features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=TEST_DATA,
      target_dtype=np.int,
      features_dtype=np.float32)

# Specify that all features have real-value data
feature_columns = [tf.feature_column.numeric_column("x", shape[4])]

 # Build 3 layer DNN with 10, 20, 10 units respectively
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                          hidden_units=[10, 20, 10],
                                          n_classes=3,
                                          model_dir="output")
# Define the training inputs
train_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(training_set.data)},
      y=np.array(training_set.target),
      num_epochs=None,
      shuffle=True)

# Train model
classifier.train(input_fn=train_input_fn, steps=2000)

# Define the test inputs
test_input_fn = tf.estimator.inputs.numpy_input_fn(
      x={"x": np.array(test_set.data)},
      y=np.array(test_set.target),
      num_epochs=1,
      shuffle=False)

# Evaluate accuracy
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
print("\nTest Accuracy: {0:f}\n".format(accuracy_score))
