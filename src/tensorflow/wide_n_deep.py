import tensorflow as tf

CSV_HEADERS = ['a1','b1','c1','d1','e1','f1','g1','h1','a2','b2','c2','d2','e2','f2','g2','h2','a3','b3','c3','d3','e3','f3','g3','h3'
,'a4','b4','c4','d4','e4','f4','g4','h4','a5','b5','c5','d5','e5','f5','g5','h5','a6','b6','c6','d6','e6','f6','g6','h6','a7',
'b7','c7','d7','e7','f7','g7','h7','a8','b8','c8','d8','e8','f8','g8','h8','whos_move','fen','result']

# Categorical Columns
whos_move = tf.feature_column.categorical_column_with_vocabulary_list(
    "whos_move", ["w", "b"])
result = tf.feature_column.categorical_column_with_vocabulary_list(
    "result", ["1-0", "0-1", "1/2-1/2"])

# Continuous Columns
fen = tf.feature_column.categorical_column_with_hash_bucket(
    "fen", hash_bucket_size=1000)

# Remaining Columns - A
a1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
a8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "a8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - B
b1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
b8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "b8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - C
c1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
c8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "c8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - D
d1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
d8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "d8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - E
e1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
e8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "e8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - F
f1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
f8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "f8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - G
g1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
g8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "g8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
# Remaining Columns - H
h1 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h1", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h2 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h2", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h3 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h3", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h4 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h4", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h5 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h5", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h6 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h6", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h7 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h7", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
h8 = tf.feature_column.categorical_column_with_vocabulary_list(
    "h8", [0,"r","R","n","N","b","B","q","Q","k","K","p","P"])
