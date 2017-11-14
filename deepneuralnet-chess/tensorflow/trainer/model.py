
"""Define a Wide + Deep model for classification on structured data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import multiprocessing

import tensorflow as tf


# Define the format of your input data including unused columns
COLS_HEADERS = "a1,b1,c1,d1,e1,f1,g1,h1,a2,b2,c2,d2,e2,f2,g2,h2,a3,b3,c3,d3,e3,f3,g3,h3,a4,b4,c4,d4,e4,f4,g4,h4,a5,b5,c5,d5,e5,f5,g5,h5,a6,b6,c6,d6,e6,f6,g6,h6,a7,b7,c7,d7,e7,f7,g7,h7,a8,b8,c8,d8,e8,f8,g8,h8,whos_move,fen,result"
CSV_COLUMNS = COLS_HEADERS.split(',')

CSV_COLUMN_DEFAULTS = [ ['0'] for col in CSV_COLUMNS ]
LABEL_COLUMN = 'result'
LABELS = ['1-0', '0-1', '1/2-1/2']

# ----------------------------------------------------------------------------------------
# Feature Columns:
# initialize the INPUT_COLUMNS
# ----------------------------------------------------------------------------------------
INPUT_COLUMNS = [ tf.feature_column.categorical_column_with_vocabulary_list(
    col, ['0','r','R','n','N','b','B','q','Q','k','K','p','P']) for i, col in enumerate(CSV_COLUMNS) if i < 64 ]

# ----------------------------------------------------------------------------------------
# Categorical Columns:
# Is who's move it is really important? Perhaps not.
# ----------------------------------------------------------------------------------------
# whos_move = tf.feature_column.categorical_column_with_vocabulary_list("whos_move", ["w", "b"])
# INPUT_COLUMNS.append(whos_move)

UNUSED_COLUMNS = set(CSV_COLUMNS) - {col.name for col in INPUT_COLUMNS} - \
    {LABEL_COLUMN}

def build_estimator(config, embedding_size=8, hidden_units=None):
  (a1,b1,c1,d1,e1,f1,g1,h1,a2,b2,c2,d2,e2,f2,g2,h2,a3,b3,c3,d3,e3,f3,g3,h3,a4,b4,c4,d4,e4,f4,g4,h4,
  a5,b5,c5,d5,e5,f5,g5,h5,a6,b6,c6,d6,e6,f6,g6,h6,a7,b7,c7,d7,e7,f7,g7,h7,a8,b8,c8,d8,e8,f8,g8,h8) = INPUT_COLUMNS

  wide_columns = [
      a1,b1,c1,d1,e1,f1,g1,h1,a2,b2,c2,d2,e2,f2,g2,h2,a3,b3,c3,d3,e3,f3,g3,h3,a4,b4,c4,d4,e4,f4,g4,h4,
      a5,b5,c5,d5,e5,f5,g5,h5,a6,b6,c6,d6,e6,f6,g6,h6,a7,b7,c7,d7,e7,f7,g7,h7,a8,b8,c8,d8,e8,f8,g8,h8
  ]

  deep_columns = [ tf.feature_column.indicator_column(col) for col in INPUT_COLUMNS ]

  return tf.contrib.learn.DNNLinearCombinedClassifier(
      config=config,
      linear_feature_columns=wide_columns,
      dnn_feature_columns=deep_columns,
      dnn_hidden_units=hidden_units or [100, 70, 50, 25],
      fix_global_step_increment_bug=True
  )


def parse_label_column(label_string_tensor):
  table = tf.contrib.lookup.index_table_from_tensor(tf.constant(LABELS))
  return table.lookup(label_string_tensor)

def csv_serving_input_fn():
  """Build the serving inputs."""
  csv_row = tf.placeholder(
      shape=[None],
      dtype=tf.string
  )
  features = parse_csv(csv_row)
  features.pop(LABEL_COLUMN)
  return tf.contrib.learn.InputFnOps(features, None, {'csv_row': csv_row})

# [START serving-function]
def example_serving_input_fn():
  """Build the serving inputs."""
  example_bytestring = tf.placeholder(
      shape=[None],
      dtype=tf.string,
  )
  feature_scalars = tf.parse_example(
      example_bytestring,
      tf.feature_column.make_parse_example_spec(INPUT_COLUMNS)
  )
  features = {
      key: tf.expand_dims(tensor, -1)
      for key, tensor in feature_scalars.iteritems()
  }
  return tf.contrib.learn.InputFnOps(
      features,
      None,  # labels
      {'example_proto': example_bytestring}
  )
# [END serving-function]

def json_serving_input_fn():
  """Build the serving inputs."""
  inputs = {}
  for feat in INPUT_COLUMNS:
    inputs[feat.name] = tf.placeholder(shape=[None], dtype=feat.dtype)

  features = {
      key: tf.expand_dims(tensor, -1)
      for key, tensor in inputs.iteritems()
  }
  return tf.contrib.learn.InputFnOps(features, None, inputs)


SERVING_FUNCTIONS = {
    'JSON': json_serving_input_fn,
    'EXAMPLE': example_serving_input_fn,
    'CSV': csv_serving_input_fn
}


def parse_csv(rows_string_tensor):
  """Takes the string input tensor and returns a dict of rank-2 tensors."""

  # Takes a rank-1 tensor and converts it into rank-2 tensor
  # Example if the data is ['csv,line,1', 'csv,line,2', ..] to
  # [['csv,line,1'], ['csv,line,2']] which after parsing will result in a
  # tuple of tensors: [['csv'], ['csv']], [['line'], ['line']], [[1], [2]]
  row_columns = tf.expand_dims(rows_string_tensor, -1)
  columns = tf.decode_csv(row_columns, record_defaults=CSV_COLUMN_DEFAULTS)
  features = dict(zip(CSV_COLUMNS, columns))

  # Remove unused columns
  for col in UNUSED_COLUMNS:
    features.pop(col)
  return features

def generate_input_fn(filenames,
                      num_epochs=None,
                      shuffle=True,
                      skip_header_lines=0,
                      batch_size=200):
  filename_queue = tf.train.input_producer(
      filenames, num_epochs=num_epochs, shuffle=shuffle)
  reader = tf.TextLineReader(skip_header_lines=skip_header_lines)

  _, rows = reader.read_up_to(filename_queue, num_records=batch_size)

  # Parse the CSV File
  features = parse_csv(rows)

  # This operation builds up a buffer of parsed tensors, so that parsing
  # input data doesn't block training
  # If requested it will also shuffle
  if shuffle:
    features = tf.train.shuffle_batch(
        features,
        batch_size,
        min_after_dequeue=2 * batch_size + 1,
        capacity=batch_size * 10,
        num_threads=multiprocessing.cpu_count(),
        enqueue_many=True,
        allow_smaller_final_batch=True
    )
  else:
    features = tf.train.batch(
        features,
        batch_size,
        capacity=batch_size * 10,
        num_threads=multiprocessing.cpu_count(),
        enqueue_many=True,
        allow_smaller_final_batch=True
    )

  return features, parse_label_column(features.pop(LABEL_COLUMN))
