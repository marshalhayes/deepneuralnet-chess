# neuralnet-pychess

**Installation**
According to your system, install the following packages:
  required:
    - [tensorflow](https://www.tensorflow.org/install/)
  optional:
    - [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
  
**Steps taken to produce this model**
1. install tensorflow
2. download lichess dataset 
3. install pgn-extract
    - pgn-extract is a terminal tool that can do a multitude of valuable things. I used it to get the FEN string value at each move. You can download the pgn-extract tool here [https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
    
**Manipulating the lichess dataset using pgn-extract**
By using the pgn-extract package, I was able to get the FEN string for each position after every individual move. Most of the FENs are unnecessary, but they may become useful later on.

Due to the large file size, the manipulated dataset is available from a Google Cloud Storage bucket here (link coming soon).

If you prefer to run the tool on your own dataset, run the pgn-extract script:

```
./pgn-extract -F --fencomments ../your_dataset.pgn >> outputfile.pgn
```
- "outputfile.pgn" consists of the entire values of "your_dataset.pgn" with the FEN position commented on every move...

On a semi-complete dataset from lichess, the manipulation took approximately an hour to complete. The resulting output file was over 50GB.


**Downloading lichess dataset**
Due to the massive dataset of 200,000,000+ Chess games, I have created a script that can auto-download the entire ~40GB (compressed) dataset...To download the dataset, run import.sh from data/

*In order to run the import script, you will need to download wget for your system.*

If you don't want the entire dataset, remove the unwanted urls from urllist.txt located in data/. You can also download specific datasets by simply visiting [database.lichess.org](https://database.lichess.org/) directly.
