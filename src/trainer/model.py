
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import multiprocessing

import tensorflow as tf

CSV_COLUMNS = ['position', 'result']
CSV_COLUMN_DEFAULTS = [[''], ['']]
LABEL_COLUMN = 'result'
LABELS = ['1-0', '0-1', '1/2-1/2']

INPUT_COLUMNS = [
    tf.feature_column.categorical_column_with_hash_bucket(
        'position', hash_bucket_size=100, dtype=tf.string),
    tf.feature_column.categorical_column_with_vocabulary_list(
        'result', ['1-0', '0-1', '1/2-1/2'])
]

UNUSED_COLUMNS = set(CSV_COLUMNS) - {col.name for col in INPUT_COLUMNS} - \
    {LABEL_COLUMN}

# Build a wide and deep model for predicting game result
def build__result_prediction(config, embedding_size=8, hidden_units=None):
    position, result = INPUT_COLUMNS

    wide_columns = [position]
    deep_columns = [
        tf.feature_column.embedding_column(
            position, dimension=embedding_size)
    ]

    return tf.contrib.learn.DNNLinearCombinedClassifier(
            config=config,
            linear_feature_columns=wide_columns,
            dnn_feature_columns=deep_columns,
            dnn_hidden_unity=hidden_units or [100, 70, 50, 25],
            fix_global_step_increment_bug=True
        )
def parse_label_column(label_string_tensor):
    '''
    Parses a string tensor into the label tensor
          Args:
            label_string_tensor: Tensor of dtype string. Result of parsing the
            CSV column specified by LABEL_COLUMN
          Returns:
            A Tensor of the same shape as label_string_tensor, should return
            an int64 Tensor representing the label index for classification tasks,
            and a float32 Tensor representing the value for a regression task.
    '''

    # Build a hash table inside the graph
    table = tf.contrib.lookup.index_table_from_tensor(tf.constant(LABELS))
    return table.lookup(label_string_tensor)

#########################################################################
# Tensorflow #
#########################################################################
def csv_serving_input_fn():
  """Build the serving inputs."""
  csv_row = tf.placeholder(
      shape=[None],
      dtype=tf.string
  )
  features = parse_csv(csv_row)
  features.pop(LABEL_COLUMN)
  return tf.contrib.learn.InputFnOps(features, None, {'csv_row': csv_row})

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
  """Generates an input function for training or evaluation.
  This uses the input pipeline based approach using file name queue
  to read data so that entire data is not loaded in memory.

  Args:
      filenames: [str] list of CSV files to read data from.
      num_epochs: int how many times through to read the data.
        If None will loop through data indefinitely
      shuffle: bool, whether or not to randomize the order of data.
        Controls randomization of both file order and line order within
        files.
      skip_header_lines: int set to non-zero in order to skip header lines
        in CSV files.
      batch_size: int First dimension size of the Tensors returned by
        input_fn
  Returns:
      A function () -> (features, indices) where features is a dictionary of
        Tensors, and indices is a single Tensor of label indices.
  """
  filename_queue = tf.train.string_input_producer(
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
