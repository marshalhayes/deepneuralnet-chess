import tensorflow as tf
import pandas as pd

COLS_HEADERS = "a1,b1,c1,d1,e1,f1,g1,h1,a2,b2,c2,d2,e2,f2,g2,h2,a3,b3,c3,d3,e3,f3,g3,h3,a4,b4,c4,d4,e4,f4,g4,h4,a5,b5,c5,d5,e5,f5,g5,h5,a6,b6,c6,d6,e6,f6,g6,h6,a7,b7,c7,d7,e7,f7,g7,h7,a8,b8,c8,d8,e8,f8,g8,h8,whos_move,fen,result"
CSV_COLUMNS = COLS_HEADERS.split(',')

# ----------------------------------------------------------------------------------------
# Feature Columns:
# initialize the feature_columns to none
# ----------------------------------------------------------------------------------------
feature_columns = [ None for i in range(64) ]
for i, col in enumerate(CSV_COLUMNS):
    if i >= 64:
        break
    # each col value can be one of 13 possibilities. Whatever it is, hash it...
    feature_columns[i] = tf.feature_column.categorical_column_with_hash_bucket(col, hash_bucket_size=13)

# ----------------------------------------------------------------------------------------
# Categorical Columns:
# ----------------------------------------------------------------------------------------
whos_move = tf.feature_column.categorical_column_with_vocabulary_list("whos_move", ["w", "b"])

# !!! LABEL (CLASSIFICATION) !!!
# What does this actually do? {result} is never used anywhere
result = tf.feature_column.categorical_column_with_vocabulary_list("result", ["1-0", "0-1", "1/2-1/2"])

# ----------------------------------------------------------------------------------------
# Linear Model (Wide)
# ----------------------------------------------------------------------------------------
base_columns = feature_columns + [whos_move]
crossed_columns = []

# ----------------------------------------------------------------------------------------
# Neural Network (Deep)
# ----------------------------------------------------------------------------------------
deep_columns = [ tf.feature_column.indicator_column(col) for col in feature_columns ] + [tf.feature_column.indicator_column(whos_move)]

# ----------------------------------------------------------------------------------------
# input_fn()
# ----------------------------------------------------------------------------------------
def input_fn(data_file, num_epochs, shuffle):
  """Input builder function."""
  print("Reading input...")
  df_data = pd.read_csv(
      tf.gfile.Open(data_file),
      names=CSV_COLUMNS,
      verbose=True,
      skipinitialspace=True,
      engine="python",
      skiprows=1)
  # remove NaN elements
  df_data = df_data.dropna(how="any", axis=0)
  # labels = df_data["result"].astype("category").cat.codes
  labels = df_data["result"].astype("category").cat.codes.astype(int)
  print(labels)
  return tf.estimator.inputs.pandas_input_fn(
      x=df_data,
      y=labels,
      batch_size=100,
      num_epochs=num_epochs,
      shuffle=shuffle,
      num_threads=5)


# ----------------------------------------------------------------------------------------
# Combine the wide and deep models into one
# ----------------------------------------------------------------------------------------
model_dir = "output"
m = tf.estimator.DNNLinearCombinedClassifier(
    model_dir=model_dir,
    n_classes=3,
    linear_feature_columns=crossed_columns,
    dnn_feature_columns=deep_columns,
    dnn_hidden_units=[20,12])

# ----------------------------------------------------------------------------------------
# log the progress to the terminal
# ----------------------------------------------------------------------------------------
import logging
logging.getLogger().setLevel(logging.INFO)


# set num_epochs to None to get infinite stream of data.
m.train(
    input_fn=input_fn("../data/2017-09-15.pgn.csv", num_epochs=None, shuffle=True),
    steps=1000)
# set steps to None to run evaluation until all data consumed.
results = m.evaluate(
    input_fn=input_fn("../data/2017-03-1.pgn.csv", num_epochs=1, shuffle=False),
    steps=None)

# print("model directory = %s" % model_dir)
# for key in sorted(results):
#     print("%s: %s" % (key, results[key]))
