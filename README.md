# deepneuralnet-chess

# Getting Started 
**Installation**
According to your system, install the following packages:
  - required:
    - [tensorflow](https://www.tensorflow.org/install/)
    - [gcloud sdk](https://cloud.google.com/sdk/)
    - [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
  - optional:
    - wget
       - wget comes prepackaged with many linux distributions. If you plan to download the lichess dataset yourself, you will need wget. Otherwise, you do not need it.

# Data Manipulation
**Steps taken to produce this model**
1. install tensorflow
2. download lichess dataset 
3. install pgn-extract
    - pgn-extract is a terminal tool that can do a multitude of valuable things. I used it to get the FEN string value at the final move of each game. You can download the pgn-extract tool [here](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
3b. parse the now fen-commented dataset and extract the fen and the result, and then export that to a csv
4. use the generated csv as training data to tensorflow
    
**Manipulating the lichess dataset using pgn-extract**
By using the pgn-extract package, I was able to get the FEN string for the final position of each game.

Due to the large file size, the manipulated dataset is available from a Google Cloud Storage bucket here (link coming soon).

If you prefer to run the tool on your own dataset, run the pgn-extract script:

```
./pgn-extract -F ../your_dataset.pgn -o output.pgn
```
- "output.pgn" consists of the entire values of "your_dataset.pgn" with the FEN position commented on the final position. You can read more about the pgn-extract tool [here](ftp://ftp.cs.kent.ac.uk/pub/djb/pgn-extract/help.html), but we will not be using it anymore in this project.

On a semi-complete dataset from lichess, the manipulation took approximately an hour to complete on a Google Compute Engine VM. The resulting output file was over 50GB.


**Downloading lichess dataset**
Due to the massive dataset of 200,000,000+ Chess games, I have created a script that can auto-download the entire ~40GB (compressed) dataset...To download the dataset, run import.sh from data/

*In order to run the import script, you will need to download wget for your system.*

If you don't want the entire dataset, remove the unwanted urls from urllist.txt located in data/. You can also download specific datasets by simply visiting [database.lichess.org](https://database.lichess.org/) directly.
