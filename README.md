# deepneuralnet-chess
Given a chess position as input, predict the most likely result of the game.

**The dataset**
There are many chess databases with enormous amounts of data that would be great for this project. I chose one of my 
favorite places to play chess, [lichess.org](http://lichess.org). 

lichess is an open source chess server. They compile datasets monthly from their entire user base. The most recent count 
of the entire dataset was 241,127,059 games (approximately 47.4 GB compressed). For this project, I will use only the datasets from 2017.

**Processing the data**
The dataset contains information that is unnecessary, even completely useless, for my project. 
  1. clock times
  2. move numbers
  3. comments
  4. evaluations
  5. variations
  6. header data (tags)
  
To delete this unncessary data, I am using a tool called [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) from the University of Kent in the United Kingdom.

I am also using this tool to find the *final* position of each game. 

The documentation for pgn-extract can be found on the University of Kent's CS department website [here](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/help.html). 

```
pgn-extract --nocomments --notags --novars --nomovenumbers -F -#500000,100 <filename.pgn>
```

**Create the training/test data for tensorflow**
After processing the data, I now have just the moves followed by a chess position (FEN) corresponding the the final position of the game, and the result of the game (1-0, 0-1, or 1/2-1/2). Using python, I convert the FEN as a row vector. Each column corresponds to one square of the chess board. If the square is empty, the entry is 0. If the square is occupied by a piece, for example a white rook, then the entry will be a capital R. If it was black's rook, then the entry would be a lowercase r. 
If it was white's knight, then the entry will be a capital N and so on.

To create the training/test data for tensorflow, run the process.py script from the directory which contains the pgn files you wish to process. A new file will be created entitled "processed-output.csv" which will contain 67 columns (64 squares, who's move it is, the fen position, and the result of the game.

```
python process.py 
```
