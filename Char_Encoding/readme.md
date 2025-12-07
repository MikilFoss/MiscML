This a simple way of encoding a character down from a one hot vector of size 26 to a smaller vector.

The model does this through having a network architure that bottlenecks the input vector down to a small layer and then re expands it.

The model is able to be trained by passing any character through it and checking how well it was decoded.

Chart of the smallest model size I found for a given vector size (Note: parameter count includes the encoder and decoder):
| Encoded Vector Size|  Parameter Count |
|----------|----------|
| 5  | 2.1K |
| 4  | 3.9K  |
| 3  | 28.7K  |
| 2  | N/A |
