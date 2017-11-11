# deepneuralnet-chess
Given a chess position as input, predict the most likely result of the game.

**The dataset**

There are many chess databases with enormous amounts of data that would be great for this project. I chose one of my
favorite places to play chess, [lichess.org](http://lichess.org).

lichess is an open source chess server. They compile datasets monthly from their entire user base. The most recent count of the entire dataset at the time of this project was 241,127,059 games (approximately 47.4 GB compressed). For this project, I will use only the datasets from 2017.

You can download the original datasets from [database.lichess.org](https://database.lichess.org/). If you do not plan on processing the data yourself, you can skip to "Create the training/test data for @tensorflow". 

**Processing the data**

The dataset contains information that is unnecessary, even completely useless, for my project.
  1. clock times
  2. move numbers
  3. comments
  4. evaluations
  5. variations
  6. header data (tags)

To delete this unnecessary data, I am using a tool called [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) from the University of Kent in the United Kingdom. I am also using this tool to find the *final* position of each game.

The only pgn-extract command I used is below. If you want to know more about the pgn-extract tool, the documentation can be found on the University of Kent's CS department website [here](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/help.html).

```
pgn-extract --nocomments --notags --novars --nomovenumbers -F -#500000,100 <filename.pgn>
```

This command will read through <filename.pgn>, remove the unnecessary data, and output new .pgn files of 500,000 games each, starting with name 1.pgn and incrementing until there are no more matches returned from the command.

**Create the training/test data for @tensorflow**

*I have already performed this process on the 2017-01 - 2017-10 datasets. You can download those directly from my Google Cloud Storage bucket http://storage.googleapis.com/lichess/processed/<2017-month>/processed-output.csv.*

After processing the data, I now have just the moves followed by a chess position (FEN) corresponding to the final position of the game, and the result of the game (1-0, 0-1, or 1/2-1/2). Using python, I convert the FEN as a row vector. Each column corresponds to one square of the chess board. If the square is empty, the entry is 0. If the square is occupied by a piece, for example a white rook, then the entry will be a capital R. If it was black's rook, then the entry would be a lowercase r. If it was white's knight, then the entry will be a capital N and so on.

To create the training/test data, run the process.py script from the directory which contains the pgn files you wish to process. A new file will be created in the working directory entitled "processed-output.csv" which will contain 67 columns (64 squares, who's move it is, the fen position, and the result of the game). Each row corresponds to one chess position.

```
python process.py
```
