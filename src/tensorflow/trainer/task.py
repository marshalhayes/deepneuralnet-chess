import tensorflow as tf
import pandas as pd

# Categorical Columns
whos_move = tf.feature_column.categorical_column_with_vocabulary_list(
    "whos_move", ["w", "b"])
result = tf.feature_column.categorical_column_with_vocabulary_list(
    "result", ["1-0", "0-1", "1/2-1/2"])

# Continuous Columns
fen = tf.feature_column.categorical_column_with_hash_bucket(
    "fen", hash_bucket_size=1000)

a1 = tf.feature_column.categorical_column_with_hash_bucket(
    "a1", hash_bucket_size=13)
a2 = tf.feature_column.categorical_column_with_hash_bucket(
    "a2", hash_bucket_size=13)
a3 = tf.feature_column.categorical_column_with_hash_bucket(
    "a3", hash_bucket_size=13)
a4 = tf.feature_column.categorical_column_with_hash_bucket(
    "a4", hash_bucket_size=13)
a5 = tf.feature_column.categorical_column_with_hash_bucket(
    "a5", hash_bucket_size=13)
a6 = tf.feature_column.categorical_column_with_hash_bucket(
    "a6", hash_bucket_size=13)
a7 = tf.feature_column.categorical_column_with_hash_bucket(
    "a7", hash_bucket_size=13)
a8 = tf.feature_column.categorical_column_with_hash_bucket(
    "a8", hash_bucket_size=13)

b1 = tf.feature_column.categorical_column_with_hash_bucket(
    "b1", hash_bucket_size=13)
b2 = tf.feature_column.categorical_column_with_hash_bucket(
    "b2", hash_bucket_size=13)
b3 = tf.feature_column.categorical_column_with_hash_bucket(
    "b3", hash_bucket_size=13)
b4 = tf.feature_column.categorical_column_with_hash_bucket(
    "b4", hash_bucket_size=13)
b5 = tf.feature_column.categorical_column_with_hash_bucket(
    "b5", hash_bucket_size=13)
b6 = tf.feature_column.categorical_column_with_hash_bucket(
    "b6", hash_bucket_size=13)
b7 = tf.feature_column.categorical_column_with_hash_bucket(
    "b7", hash_bucket_size=13)
b8 = tf.feature_column.categorical_column_with_hash_bucket(
    "b8", hash_bucket_size=13)

c1 = tf.feature_column.categorical_column_with_hash_bucket(
    "c1", hash_bucket_size=13)
c2 = tf.feature_column.categorical_column_with_hash_bucket(
    "c2", hash_bucket_size=13)
c3 = tf.feature_column.categorical_column_with_hash_bucket(
    "c3", hash_bucket_size=13)
c4 = tf.feature_column.categorical_column_with_hash_bucket(
    "c4", hash_bucket_size=13)
c5 = tf.feature_column.categorical_column_with_hash_bucket(
    "c5", hash_bucket_size=13)
c6 = tf.feature_column.categorical_column_with_hash_bucket(
    "c6", hash_bucket_size=13)
c7 = tf.feature_column.categorical_column_with_hash_bucket(
    "c7", hash_bucket_size=13)
c8 = tf.feature_column.categorical_column_with_hash_bucket(
    "c8", hash_bucket_size=13)

d1 = tf.feature_column.categorical_column_with_hash_bucket(
    "d1", hash_bucket_size=13)
d2 = tf.feature_column.categorical_column_with_hash_bucket(
    "d2", hash_bucket_size=13)
d3 = tf.feature_column.categorical_column_with_hash_bucket(
    "d3", hash_bucket_size=13)
d4 = tf.feature_column.categorical_column_with_hash_bucket(
    "d4", hash_bucket_size=13)
d5 = tf.feature_column.categorical_column_with_hash_bucket(
    "d5", hash_bucket_size=13)
d6 = tf.feature_column.categorical_column_with_hash_bucket(
    "d6", hash_bucket_size=13)
d7 = tf.feature_column.categorical_column_with_hash_bucket(
    "d7", hash_bucket_size=13)
d8 = tf.feature_column.categorical_column_with_hash_bucket(
    "d8", hash_bucket_size=13)

e1 = tf.feature_column.categorical_column_with_hash_bucket(
    "e1", hash_bucket_size=13)
e2 = tf.feature_column.categorical_column_with_hash_bucket(
    "e2", hash_bucket_size=13)
e3 = tf.feature_column.categorical_column_with_hash_bucket(
    "e3", hash_bucket_size=13)
e4 = tf.feature_column.categorical_column_with_hash_bucket(
    "e4", hash_bucket_size=13)
e5 = tf.feature_column.categorical_column_with_hash_bucket(
    "e5", hash_bucket_size=13)
e6 = tf.feature_column.categorical_column_with_hash_bucket(
    "e6", hash_bucket_size=13)
e7 = tf.feature_column.categorical_column_with_hash_bucket(
    "e7", hash_bucket_size=13)
e8 = tf.feature_column.categorical_column_with_hash_bucket(
    "e8", hash_bucket_size=13)

f1 = tf.feature_column.categorical_column_with_hash_bucket(
    "f1", hash_bucket_size=13)
f2 = tf.feature_column.categorical_column_with_hash_bucket(
    "f2", hash_bucket_size=13)
f3 = tf.feature_column.categorical_column_with_hash_bucket(
    "f3", hash_bucket_size=13)
f4 = tf.feature_column.categorical_column_with_hash_bucket(
    "f4", hash_bucket_size=13)
f5 = tf.feature_column.categorical_column_with_hash_bucket(
    "f5", hash_bucket_size=13)
f6 = tf.feature_column.categorical_column_with_hash_bucket(
    "f6", hash_bucket_size=13)
f7 = tf.feature_column.categorical_column_with_hash_bucket(
    "f7", hash_bucket_size=13)
f8 = tf.feature_column.categorical_column_with_hash_bucket(
    "f8", hash_bucket_size=13)

g1 = tf.feature_column.categorical_column_with_hash_bucket(
    "g1", hash_bucket_size=13)
g2 = tf.feature_column.categorical_column_with_hash_bucket(
    "g2", hash_bucket_size=13)
g3 = tf.feature_column.categorical_column_with_hash_bucket(
    "g3", hash_bucket_size=13)
g4 = tf.feature_column.categorical_column_with_hash_bucket(
    "g4", hash_bucket_size=13)
g5 = tf.feature_column.categorical_column_with_hash_bucket(
    "g5", hash_bucket_size=13)
g6 = tf.feature_column.categorical_column_with_hash_bucket(
    "g6", hash_bucket_size=13)
g7 = tf.feature_column.categorical_column_with_hash_bucket(
    "g7", hash_bucket_size=13)
g8 = tf.feature_column.categorical_column_with_hash_bucket(
    "g8", hash_bucket_size=13)

h1 = tf.feature_column.categorical_column_with_hash_bucket(
    "h1", hash_bucket_size=13)
h2 = tf.feature_column.categorical_column_with_hash_bucket(
    "h2", hash_bucket_size=13)
h3 = tf.feature_column.categorical_column_with_hash_bucket(
    "h3", hash_bucket_size=13)
h4 = tf.feature_column.categorical_column_with_hash_bucket(
    "h4", hash_bucket_size=13)
h5 = tf.feature_column.categorical_column_with_hash_bucket(
    "h5", hash_bucket_size=13)
h6 = tf.feature_column.categorical_column_with_hash_bucket(
    "h6", hash_bucket_size=13)
h7 = tf.feature_column.categorical_column_with_hash_bucket(
    "h7", hash_bucket_size=13)
h8 = tf.feature_column.categorical_column_with_hash_bucket(
    "h8", hash_bucket_size=13)

# Linear Model (Wide)
base_columns = [
    a1,a2,a3,a4,a5,a6,a7,a8,
    b1,b2,b3,b4,b5,b6,b7,b8,
    c1,c2,c3,c4,c5,c6,c7,c8,
    d1,d2,d3,d4,d5,d6,d7,d8,
    e1,e2,e3,e4,e5,e6,e7,e8,
    f1,f2,f3,f4,f5,f6,f7,f8,
    g1,g2,g3,g4,g5,g6,g7,g8,
    h1,h2,h3,h4,h5,h6,h7,h8,
    whos_move
]
crossed_columns = [whos_move,a1,a2 ]

# Neural Network (Deep)
deep_columns = [
    tf.feature_column.indicator_column(a1),
    tf.feature_column.indicator_column(a2),
    tf.feature_column.indicator_column(a3),
    tf.feature_column.indicator_column(a4),
    tf.feature_column.indicator_column(a5),
    tf.feature_column.indicator_column(a6),
    tf.feature_column.indicator_column(a7),
    tf.feature_column.indicator_column(a8),

    tf.feature_column.indicator_column(b1),
    tf.feature_column.indicator_column(b2),
    tf.feature_column.indicator_column(b3),
    tf.feature_column.indicator_column(b4),
    tf.feature_column.indicator_column(b5),
    tf.feature_column.indicator_column(b6),
    tf.feature_column.indicator_column(b7),
    tf.feature_column.indicator_column(b8),

    tf.feature_column.indicator_column(c1),
    tf.feature_column.indicator_column(c2),
    tf.feature_column.indicator_column(c3),
    tf.feature_column.indicator_column(c4),
    tf.feature_column.indicator_column(c5),
    tf.feature_column.indicator_column(c6),
    tf.feature_column.indicator_column(c7),
    tf.feature_column.indicator_column(c8),

    tf.feature_column.indicator_column(d1),
    tf.feature_column.indicator_column(d2),
    tf.feature_column.indicator_column(d3),
    tf.feature_column.indicator_column(d4),
    tf.feature_column.indicator_column(d5),
    tf.feature_column.indicator_column(d6),
    tf.feature_column.indicator_column(d7),
    tf.feature_column.indicator_column(d8),

    tf.feature_column.indicator_column(e1),
    tf.feature_column.indicator_column(e2),
    tf.feature_column.indicator_column(e3),
    tf.feature_column.indicator_column(e4),
    tf.feature_column.indicator_column(e5),
    tf.feature_column.indicator_column(e6),
    tf.feature_column.indicator_column(e7),
    tf.feature_column.indicator_column(e8),

    tf.feature_column.indicator_column(f1),
    tf.feature_column.indicator_column(f2),
    tf.feature_column.indicator_column(f3),
    tf.feature_column.indicator_column(f4),
    tf.feature_column.indicator_column(f5),
    tf.feature_column.indicator_column(f6),
    tf.feature_column.indicator_column(f7),
    tf.feature_column.indicator_column(f8),

    tf.feature_column.indicator_column(g1),
    tf.feature_column.indicator_column(g2),
    tf.feature_column.indicator_column(g3),
    tf.feature_column.indicator_column(g4),
    tf.feature_column.indicator_column(g6),
    tf.feature_column.indicator_column(g7),
    tf.feature_column.indicator_column(g8),

    tf.feature_column.indicator_column(h1),
    tf.feature_column.indicator_column(h2),
    tf.feature_column.indicator_column(h3),
    tf.feature_column.indicator_column(h4),
    tf.feature_column.indicator_column(h5),
    tf.feature_column.indicator_column(h6),
    tf.feature_column.indicator_column(h7),
    tf.feature_column.indicator_column(h8),
    tf.feature_column.indicator_column(whos_move)
]

CSV_COLUMNS = ['a1','b1','c1','d1','e1','f1','g1','h1','a2','b2','c2','d2','e2','f2','g2','h2','a3','b3','c3','d3','e3','f3','g3','h3'
,'a4','b4','c4','d4','e4','f4','g4','h4','a5','b5','c5','d5','e5','f5','g5','h5','a6','b6','c6','d6','e6','f6','g6','h6','a7',
'b7','c7','d7','e7','f7','g7','h7','a8','b8','c8','d8','e8','f8','g8','h8','whos_move','fen','result']

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
  labels = df_data["result"].apply(lambda x: "1-0" in x).astype(int)
  return tf.estimator.inputs.pandas_input_fn(
      x=df_data,
      y=labels,
      batch_size=100,
      num_epochs=num_epochs,
      shuffle=shuffle,
      num_threads=5)

# def input_fn():
#     filename_queue = tf.train.string_input_producer(["train-data-10000.csv"], ["test-data-10000.csv"])
#     reader = tf.TextLineReader()
#     key, value = reader.read(filename_queue)
#
#     # Set default values
#     record_defaults = [ ["0"] for i in range(64) ]
#
#     col1, col2, col3, col4, col5, col6, col7,
#         col8, col9, col10, col11, col12, col13,
#         col14, col15, col16, col17, col18, col19,
#         col20, col21, col22, col23, col24, col25,
#         col26, col27, col28, col29, col30, col31,
#         col32, col32, col33, col34, col35, col36,
#         col37, col38, col39, col40, col41, col42,
#         col43, col44, col45, col46, col47, col48,
#         col49, col50, col51, col52, col53, col54,
#         col55, col56, col57, col58, col59, col60,
#         col61, col62, col63, col64, whos_move, result = tf.decode_csv(value, record_defaults=record_defaults)
#
#     features = tf.stack([col1, col2, col3, col4, col5, col6, col7,
#         col8, col9, col10, col11, col12, col13,
#         col14, col15, col16, col17, col18, col19,
#         col20, col21, col22, col23, col24, col25,
#         col26, col27, col28, col29, col30, col31,
#         col32, col32, col33, col34, col35, col36,
#         col37, col38, col39, col40, col41, col42,
#         col43, col44, col45, col46, col47, col48,
#         col49, col50, col51, col52, col53, col54,
#         col55, col56, col57, col58, col59, col60,
#         col61, col62, col63, col64, whos_move, result])
#
#     with tf.Session() as sess:
#       # Start populating the filename queue.
#       coord = tf.train.Coordinator()
#       threads = tf.train.start_queue_runners(coord=coord)
#
#       for i in range(1200):
#         # Retrieve a single instance:
#         example, label = sess.run([features, result])
#
#       coord.request_stop()
#       coord.join(threads)

# Combine the wide and deep models into one
model_dir = "output"
m = tf.estimator.DNNLinearCombinedClassifier(
    model_dir=model_dir,
    linear_feature_columns=crossed_columns,
    dnn_feature_columns=deep_columns,
    dnn_hidden_units=[10,6])

# set num_epochs to None to get infinite stream of data.
m.train(
    input_fn=input_fn("data/train-data-5000.csv", num_epochs=None, shuffle=True),
    steps=1000)
# set steps to None to run evaluation until all data consumed.
results = m.evaluate(
    input_fn=input_fn("data/test-data-5000.csv", num_epochs=4, shuffle=False),
    steps=None)
print("model directory = %s" % model_dir)

for key in sorted(results):
    print("%s: %s" % (key, results[key]))
