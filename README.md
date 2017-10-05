# neuralnet-pychess

**Installation**
According to your system, install the following packages:
  - [tensorflow](https://www.tensorflow.org/install/) 
  
**Downloading lichess dataset**
Due to the massive dataset of 200,000,000+ Chess games, I have created a script that can auto-download the entire ~40GB (compressed) dataset...To download the dataset, run import.sh from data/

*In order to run the import script, you will need to download wget for your system.*

If you don't want the entire dataset, remove the unwanted urls from urllist.txt located in data/. You can also download specific datasets by simply visiting [database.lichess.org](https://database.lichess.org/) directly.

**Steps taken to produce this model**
1. install tensorflow
2. download lichess dataset 
3. install pgn-extract
    - pgn-extract is a terminal tool that can do a multitude of valuable things. I used it to get the FEN string value at each move. You can download the pgn-extract tool here [https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/)
