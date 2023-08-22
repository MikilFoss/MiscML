Using a dataset of grandmaster games, train a classifier to predict the next move in a chess game. \

The dataset is a collection of games from the current top 10 chess players in the world as well as kasparov and karpov. From the site https://www.pgnmentor.com/files.html

The total number of games is: 4113
The Total number of moves is: 1672046

Approach to the Problem:

Data Processing: Use one-hot encoding to encode the board state into a vector, and set the target to be the next move the player made.