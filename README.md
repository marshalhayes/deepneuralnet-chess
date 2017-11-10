# deepneuralnet-chess
Given a chess position as input, predict the most likely result of the game.

*The dataset*
There are many chess databases with enormous amounts of data that would be great for this project. I chose one of my 
favorite places to play chess, (lichess.org)[http://lichess.org]. 

lichess is an open source chess server. They compile datasets monthly from their entire user base. The most recent count 
of the entire dataset was 241,127,059 games (approximately 47.4 GB compressed). For this project, I will just the datasets from 2017.

*Processing the data*
The dataset contains information that is unnecessary, even completely useless, for my project. 
  1. clock times
  2. move counts
  3. comments
  4. evaluations
  5. header data
  
To delete this unncessary data, I am using a tool called (pgn-extract)[https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/] from the University of Kent in the United Kingdom.

I am also using this tool to find the **final** position of each game. 
