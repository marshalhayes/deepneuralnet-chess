# DEEPNEURALNET-CHESS

# Getting Started 
**Installation**
According to your system, install the following packages:
  - required:
    - [tensorflow](https://www.tensorflow.org/install/)
    - [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
  - optional:
    - wget
       - wget comes prepackaged with many linux distributions. If you plan to download the lichess dataset yourself, you will need wget. Otherwise, you do not need it.

# Data Manipulation
**Steps taken to produce this model**
1. install tensorflow
2. download lichess dataset 
3. install pgn-extract
4. run pgn-extract on the dataset to 'extract' the FEN position
    ```
    pgn-extract --nocomments --notags --novars --nomovenumbers -F -#100000,100 ../orig/lichess_db_standard_rated_2015-01.pgn
    ```
    The above command removes the headers, comments, evaluations, and move numbers. Then it finds the FEN position for the final move of the game. It then writes 100,000 games per file...starting with the file name 1.pgn and goes in order (2.pgn, 3.pgn, ...). You can read more about pgn-extract [here](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/).
5. run [src/process.py](https://github.com/marshalhayes/deepneuralnet-chess/blob/master/src/process.py) on the new fen-commented dataset, extract the fen & result and vectorize each row for each game
6. use a portion of the generated csv as training data and the other portion as test data to tensorflow

**Downloading lichess dataset**
Due to the massive dataset of 200,000,000+ Chess games available from lichess, I have created a script that can auto-download the entire ~40GB (compressed) dataset...To download the dataset, run import.sh from data/

*In order to run the import script, you will need to download wget for your system.*

If you don't want the entire dataset, remove the unwanted urls from urllist.txt located in data/. You can also download specific datasets by simply visiting [database.lichess.org](https://database.lichess.org/) directly.

# References
None
