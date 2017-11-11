# deepneuralnet-chess
Given a chess position as input, predict the most likely result of the game.

**Hardware**
Due to the scale of the lichess dataset, I am using the Google Cloud Platform to do most of the legwork. For the processing of the data, I am using a moderately powerful Cloud VM (Google Compute Engine). To store the large dataset and processed output, I am using a bucket from Google Cloud Storage.

**CPU Usage**
![cpu-usage graph](cpu-usage.png)

As you can see from the graph above, pgn-extract takes much longer runtime as well as CPU usage than [process.py](deepneuralnet/process.py). This is certainly to be expected as the two are much different in terms of simplicity and operations. I am mainly displaying this graph to show that the process.py has a relatively quick runtime with low CPU usage even with millions of games. 
